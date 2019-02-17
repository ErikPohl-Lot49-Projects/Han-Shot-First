from json import load, loads
import urllib
import urllib.request
import logging
import sys

class viewtree_search_cli:

    def __init__(self):
        self.delims = ('#', '.', '!', '@')
        self.combinators = (' ', '>')
        self.json_source = None
        self.debug_mode = False
        print("ViewTree Search")
        print("Type 'help' for instructions for use.")
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)

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

    def viewtree_search(self,json_view_tree, search_commands, search_hits, halt_on_match=False, debug_mode = False):
        check_hits = lambda hits: [hit_or_miss for hit_or_miss in hits if hit_or_miss > 0]
        recursable_tags = ('subviews', 'contentView', 'input', 'control')
        local_search_commands = search_commands[:]
        local_search_hits = search_hits[:]
        logging.disable(logging.NOTSET) if debug_mode else logging.disable(logging.INFO)
        match_count = 0
        logging.info('called;' + str(type(json_view_tree)) + str(json_view_tree))
        if isinstance(json_view_tree, str):
            logging.info('string leaf.  ending the search.')
            return match_count
        if isinstance(json_view_tree, list):
            logging.info('found a list.  searching it.')
            for index, json_list_element in enumerate(json_view_tree):
                logging.info('recursing list item [ ' + str(index))
                match_count += self.viewtree_search(
                    json_list_element,
                    local_search_commands,
                    local_search_hits,
                    halt_on_match=halt_on_match,
                    debug_mode=debug_mode
                )
            return match_count
        if isinstance(json_view_tree, dict):
            logging.info('found a dictionary.  searching it.')
            for json_list_element in json_view_tree.keys():
                if isinstance(json_view_tree[json_list_element], dict) or (
                        json_list_element != 'classNames' and isinstance(json_view_tree[json_list_element], list)):
                    if json_list_element in recursable_tags:
                        logging.info(
                            str(type(json_view_tree[json_list_element])) + str(json_view_tree[json_list_element]))
                        logging.info('calling')
                        match_count += self.viewtree_search(
                            json_view_tree[json_list_element],
                            local_search_commands,
                            local_search_hits,
                            halt_on_match=halt_on_match,
                            debug_mode = debug_mode
                        )
                else:
                    for command_index, command in enumerate(local_search_commands):
                        if command.startswith('#'):
                            logging.info('trying identifier [' + json_list_element + ']')
                            if (json_list_element == 'identifier') and (
                                    json_view_tree[json_list_element] == command[1:]):
                                local_search_hits[command_index] += 1
                                if len(check_hits(local_search_hits)) == len(local_search_hits):
                                    print(str(json_view_tree))
                                    match_count += 1
                                    if halt_on_match:
                                        return 1
                        elif command.startswith('.'):
                            className = command[1:]
                            if (json_list_element == 'classNames') and (
                                    className in json_view_tree[json_list_element]):
                                local_search_hits[command_index] += 1
                                logging.info('found in ' + str(json_view_tree[json_list_element]))
                                if len(check_hits(local_search_hits)) == len(local_search_hits):
                                    print(json_view_tree)
                                    match_count += 1
                                    if halt_on_match:
                                        return 1
                        elif (json_list_element == 'class') and (json_view_tree[json_list_element] == command[0:]):
                            local_search_hits[command_index] += 1
                            if len(check_hits(local_search_hits)) == len(local_search_hits):
                                print(json_view_tree)
                                match_count += 1
                                if halt_on_match:
                                    return 1
        return match_count

    def viewtree_search_with_combinators(self, search_commands):
        return True

    def prompt(self):
        def json_source_status():
            print("JSON source data is still loaded from before") if self.json_source else print(
                "No JSON source data exists for viewtree searching.")

        while True:
            command_string = input(">>")
            if command_string.startswith('!'):
                json_file_name = command_string[1:]
                windowsed_file_name = json_file_name.replace('\\', '\\\\')
                try:
                    with open(windowsed_file_name, 'r') as json_file_handle:
                        self.json_source = load(json_file_handle)
                    print('Loaded source from ', json_file_name)
                    if self.debug_mode:
                        print('Source: ',self.json_source)
                except:
                    print("Error loading file ", json_file_name)
                    print("Please review the file path and name and try again.")
                    json_source_status()
            elif command_string == '?':
                self.debug_mode = not self.debug_mode
                print("Debug mode enabled.") if self.debug_mode else print("Debug mode disabled.")
            elif command_string.startswith('@'):
                try:
                    command_url = command_string[1:]
                    url_request = urllib.request.urlopen(command_url)
                    data = url_request.read()
                    encoding = url_request.info().get_content_charset('utf-8')
                    self.json_source = loads(data.decode(encoding))
                    print('Loaded source from ', command_url)
                    if self.debug_mode:
                        print('Source: ',self.json_source)
                except:
                    print("Error loading URL ", command_url)
                    print("Please review the URL/internet connection and try again.")
                    json_source_status()
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
                    print("Exit attempt cancelled.  Resuming CLI")
                    json_source_status()
            else: # this code is used to perform a viewtree search since all other command options are not in play
                if not self.json_source:
                    print("No JSON source is loaded.  Please load one from file or URL.")
                    print("Remember: typing 'help' will get you instructions to use this CLI.")
                else:
                    command_list = self.split_string_command(command_string)
                    command_hits = [0]*len(command_list)
                    search_results = self.viewtree_search(self.json_source, command_list, command_hits, debug_mode = self.debug_mode)
                    print("Found 1 entry") if search_results == 1 else print("Found {} entries".format(search_results))



