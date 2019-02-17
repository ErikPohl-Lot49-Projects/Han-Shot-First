from json import load, loads
import urllib
import urllib.request
import logging
import sys

#command_string = input(">>")

class viewtree_search_cli:

    def __init__(self):
        self.delims = ('#', '.', '!', '@')
        self.json_source = None
        self.debug_mode = False
        print("ViewTree Search")
        print("Type 'help' for instructions for use.")
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)

    def split_string_command(self,string_command):
        command_list = []
        cur_str = ''
        for x in string_command:
            if x not in self.delims:
                cur_str+=x
            else:
                if cur_str:
                    command_list.append(cur_str)
                cur_str = x
        if cur_str:
            command_list.append(cur_str)
        return command_list

    def viewtree_search(self,json_view_tree, search_commands, search_hits, halt_on_match=False, debug_mode = False):
        recursable_tags = ('subviews', 'contentView', 'input', 'control')
        search_commands2 = search_commands[:]
        search_hits2 = search_hits[:]
        logging.disable(logging.NOTSET) if debug_mode else logging.disable(logging.INFO)
        count = 0
        logging.info('called;' + str(type(json_view_tree)) + str(json_view_tree))
        if isinstance(json_view_tree, str):
            logging.info('string leaf')
            return count
        if isinstance(json_view_tree, list):
            logging.info('scanning list')
            for index, json_list_element in enumerate(json_view_tree):
                logging.info('recursing list item [ ' + str(index))
                count += self.viewtree_search(json_list_element, search_commands2, search_hits2, halt_on_match=halt_on_match, debug_mode=debug_mode)
            return count
        if isinstance(json_view_tree, dict):
            logging.info('indict')
            for json_list_element in json_view_tree.keys():
                if isinstance(json_view_tree[json_list_element], dict) or (
                        json_list_element != 'classNames' and isinstance(json_view_tree[json_list_element], list)):
                    if json_list_element in recursable_tags:
                        logging.info(
                            str(type(json_view_tree[json_list_element])) + str(json_view_tree[json_list_element]))
                        logging.info('calling')
                        count += self.viewtree_search(json_view_tree[json_list_element], search_commands2, search_hits2,
                                                 halt_on_match=halt_on_match, debug_mode = debug_mode)
                else:
                    for command_index, command in enumerate(search_commands2):
                        if command.startswith('#'):
                            logging.info('trying identifier [' + json_list_element + ']')
                            if (json_list_element == 'identifier') and (
                                    json_view_tree[json_list_element] == command[1:]):
                                search_hits2[command_index] += 1
                                if len([x for x in search_hits2 if x > 0]) == len(search_hits2):
                                    print(str(json_view_tree))
                                    count += 1
                                    if halt_on_match:
                                        return 1
                        elif command.startswith('.'):
                            if (json_list_element == 'classNames') and (
                                    command[1:] in json_view_tree[json_list_element]):
                                search_hits2[command_index] += 1
                                logging.info('found in ' + str(json_view_tree[json_list_element]))
                                if len([x for x in search_hits2 if x > 0]) == len(search_hits2):
                                    print(json_view_tree)
                                    count += 1
                                    if halt_on_match:
                                        return 1
                        elif (json_list_element == 'class') and (json_view_tree[json_list_element] == command[0:]):
                            search_hits2[command_index] += 1
                            if len([x for x in search_hits2 if x > 0]) == len(search_hits2):
                                print(json_view_tree)
                                count += 1
                                if halt_on_match:
                                    return 1

        return count

    def prompt(self):
        while True:
            command_string = input(">>")
            if command_string.startswith('!'):
                fname = command_string[1:]
                use_fname = fname.replace('\\', '\\\\')
                with open(use_fname, 'r') as f1:
                    self.json_source = load(f1)
                print(self.json_source)
                print('loaded source from ', fname, use_fname)
            elif command_string == '?':
                self.debug_mode = not self.debug_mode
                print("Debug mode enabled.") if self.debug_mode else print("Debug mode disabled.")
            elif command_string.startswith('@'):
                s = urllib.request.urlopen(command_string[1:])
                data = s.read()
                encoding = s.info().get_content_charset('utf-8')
                self.json_source = loads(data.decode(encoding))
                print('loaded source from ', command_string[1:])
                print(self.json_source)
            elif command_string.lower() == 'help':
                print('ViewTree Search Help')
                print("ViewTree Search is a CLI which allows you to load JSON from a file or from a URL and search it for various selectors.")
                print("? toggles debug mode")
                print("help outputs the help instructions [these]")
                print("exit exits the CLI")
                print("![file name] allows you to load a file of JSON named file name-- don't use the brackets.  ")
                print("@[URL] allows you to load a URL of JSON using the specified URL-- don't use the brackets.  ")
                print("Simple selector")
                print("Compound selector")
            elif command_string.lower() == 'exit':
                command_string = input("Are you sure?")
                if command_string.lower().startswith('y'):
                    exit()
            else:
                if not self.json_source:
                    print("No JSON source is loaded.  Please load one from file or URL.")
                    print("Remember: typing 'help' will get you instructions to use this CLI.")
                else:
                    command_list = self.split_string_command(command_string)
                    #print(command_list)
                    command_hits = [0]*len(command_list)
                    #print('evaluating ',self.z)
                    #print('using ', command_list)
                    #print('and ', command_hits)
                    zx = self.viewtree_search(self.json_source, command_list, command_hits, debug_mode = self.debug_mode)
                    print("Found {} entries".format(zx))



z = viewtree_search_cli()
z.prompt()
