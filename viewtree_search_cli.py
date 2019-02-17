from json import load, loads
import urllib
import urllib.request
import logging
import sys
import string

class viewtree_search_cli:

    def output_welcome_message(self):
        print("ViewTree Search")
        print("Type 'help' for instructions for use.")

    def __init__(self):
        self.delims = ('#', '.', '!', '@')
        self.combinators = (' ', '>')
        self.json_source = None
        self.debug_mode = False
        self.check_hits = lambda hits: len([hit_or_miss for hit_or_miss in hits if hit_or_miss > 0]) == len(hits)
        self.recursable_tags = ('subviews', 'contentView', 'input', 'control')
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        self.output_welcome_message()

    def split_string_command(self,string_command):
        command_list = []
        current_command = ''
        for char in string_command:
            if char not in self.delims:
                current_command+=char
            else:
                if current_command:
                    command_list.append(current_command)
                current_command = char
        if current_command:
            command_list.append(current_command)
        return command_list


    def viewtree_search(
            self,
            json_view_tree,
            search_commands,
            search_hits,
            halt_on_match=False,
            debug_mode = False,
            max_descendent_level = None,
            sibling_descendent_level = None,
            max_finds = None,
            level = 0
    ):
        print('Level', level)
        local_search_commands = search_commands[:]
        local_search_hits = search_hits[:]
        results = []
        logging.disable(logging.NOTSET) if debug_mode else logging.disable(logging.INFO)
        logging.info('called;' + str(type(json_view_tree)) + str(json_view_tree))
        if isinstance(json_view_tree, str):
            logging.info('string leaf.  ending the search.')
            return results
        if isinstance(json_view_tree, list):
            logging.info('found a list.  searching it.')
            for index, json_list_element in enumerate(json_view_tree):
                logging.info('recursing list item [ ' + str(index))
                results.extend( self.viewtree_search(
                    json_list_element,
                    local_search_commands,
                    local_search_hits,
                    halt_on_match=halt_on_match,
                    debug_mode=debug_mode,
                    level=level+1
                ))
            return results
        if isinstance(json_view_tree, dict):
            logging.info('found a dictionary.  searching it.')
            for json_list_element in json_view_tree.keys():
                if isinstance(json_view_tree[json_list_element], dict) or (
                        json_list_element != 'classNames' and isinstance(json_view_tree[json_list_element], list)):
                    if json_list_element in self.recursable_tags:
                        logging.info(
                            str(type(json_view_tree[json_list_element])) + str(json_view_tree[json_list_element]))
                        logging.info('calling')
                        results.extend(self.viewtree_search(
                            json_view_tree[json_list_element],
                            local_search_commands,
                            local_search_hits,
                            halt_on_match=halt_on_match,
                            debug_mode = debug_mode,
                            level=level+1
                        ))
                else:
                    for command_index, command in enumerate(local_search_commands):
                        if (
                                (command.startswith('#')
                                and (json_list_element == 'identifier')
                                and (json_view_tree[json_list_element] == command[1:])
                                ) or
                                (command.startswith('.')
                                 and (json_list_element == 'classNames')
                                 and (command[1:] in json_view_tree[json_list_element])
                                ) or
                                (not command.startswith('#') and not command.startswith('.')
                                 and (json_list_element == 'class')
                                 and (json_view_tree[json_list_element] == command[0:])
                                )
                        ):
                                local_search_hits[command_index] += 1
                                if self.check_hits(local_search_hits):
                                    result = str(json_view_tree)
                                    results.append(result)
                                    if halt_on_match:
                                        return results
        return results

    def output_results(self, results):
        for result in results:
            print(result)
        print("Found 1 entry") if len(results) == 1 else print("Found {} entries".format(len(results)))

    def viewtree_search_with_combinators(self, command_string):
        command_list = self.split_string_command(command_string)
        current_search_command = []
        for search_command in command_list:
            if search_command not in self.combinators:
                current_search_command.append(search_command)
        command_hits = [0] * len(command_list)
        search_results = self.viewtree_search(self.json_source, current_search_command, command_hits, debug_mode=self.debug_mode)
        self.output_results(search_results)
        return True

    def json_source_status(self):
        print("JSON source data is still loaded from before") if self.json_source else print(
            "No JSON source data exists for viewtree searching.")

    def toggle_debug_mode(self):
        self.debug_mode = not self.debug_mode
        print("Debug mode enabled.") if self.debug_mode else print("Debug mode disabled.")

    def load_json_from_file(self,command_string):
        json_file_name = command_string[1:]
        windowsed_file_name = json_file_name.replace('\\', '\\\\')
        try:
            with open(windowsed_file_name, 'r') as json_file_handle:
                self.json_source = load(json_file_handle)
            print('Loaded source from ', json_file_name)
            if self.debug_mode:
                print('Source: ', self.json_source)
        except:
            print("Error loading file ", json_file_name)
            print("Please review the file path and name and try again.")
            self.json_source_status()

    def print_help(self):
        print('ViewTree Search Help')
        print(
            "ViewTree Search is a CLI which allows you to load JSON from a file or from a URL and search it for various selectors.")
        print("? toggles debug mode")
        print("help outputs the help instructions [these]")
        print("exit exits the CLI")
        print("source outputs the current json source available for viewtree searching")
        print("![file name] allows you to load a file of JSON named file name-- don't use the brackets.  ")
        print("@[URL] allows you to load a URL of JSON using the specified URL-- don't use the brackets.  ")
        print("Simple selector")
        print("Compound selector")

    def load_json_from_url(self,command_string):
        try:
            command_url = command_string[1:]
            url_request = urllib.request.urlopen(command_url)
            data = url_request.read()
            encoding = url_request.info().get_content_charset('utf-8')
            self.json_source = loads(data.decode(encoding))
            print('Loaded source from ', command_url)
            if self.debug_mode:
                print('Source: ', self.json_source)
        except:
            print("Error loading URL ", command_url)
            print("Please review the URL/internet connection and try again.")
            self.json_source_status()

    def attempt_exit(self):
        command_string = input("Are you sure?")
        if command_string.lower().startswith('y'):
            exit()
        else:
            print("Exit attempt cancelled.  Resuming CLI")
            self.json_source_status()

    def prompt(self):
        while True:
            command_string = input(">>")
            if command_string.startswith('!'):
                self.load_json_from_file(command_string)
            elif command_string == '?':
                self.toggle_debug_mode()
            elif command_string.startswith('@'):
                self.load_json_from_url(command_string)
            elif command_string.lower() == 'help':
                self.print_help()
            elif command_string.lower() == 'exit':
                self.attempt_exit()
            elif command_string.lower() == 'source':
                print(self.json_source) if self.json_source else print("No JSON source has been loaded for viewtree searching")
            else: # this code is used to perform a viewtree search since all other command options are not in play
                if not self.json_source:
                    print("No JSON source is loaded.  Please load one from file or URL.")
                    print("Remember: typing 'help' will get you instructions to use this CLI.")
                else:
                    self.viewtree_search_with_combinators(command_string)
