#!/usr/bin/env python

'''
Provides a CLI for a user to load JSON from files
or URLs and then search it with selectors
'''

import logging
import sys
import re
import urllib.request
from json import load, loads, dumps

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Code Review"


class viewtree_search_cli:
    '''
    Provides a CLI for a user to load JSON from files
    or URLs and then search it with selectors
    '''

    def _output_welcome_message(self):
        '''
        Output a welcome message for the viewtree CLI
        '''
        print("ViewTree Search")
        print("ViewTree Search CLI is a CLI which allows a user to "
              "load ViewTree JSON scripts from files or from URLs and"
              " then perform selector searches on it.")
        print("Type 'help' for instructions for use.")
        return True

    def __init__(self):
        '''
        Set up important attributes for the viewtree
        search CLI, and output a welcome message
        '''

        self.json_source = None
        self.debug_mode = False
        self.check_full_search_match = lambda hits: all(
            [hit_or_miss for hit_or_miss in hits]
        )
        self.recursable_tags = ('subviews', 'contentView', 'input', 'control')
        self.delims = ('#', '.', '!', '@')
        self.combinators = (' ', '>', '+', '~')
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        self._output_welcome_message()

    def _set_logging(self):
        '''
        set logging on or off for info
        logging based on debug_mode
        method
        '''
        logging.disable(logging.NOTSET) \
            if self.debug_mode \
            else logging.disable(logging.INFO)

    def _split_string_command(self,
                              string_command
                              ):
        '''
        Break apart a string command which is a set of selectors
        into a command useful for the search function
        '''
        self._set_logging()
        logging.info('string command: ' + str(string_command))
        command_list = [string_command]
        split_list = re.split(r"([\.#])", string_command)
        logging.info(split_list)
        logging.info(set(string_command[1:]).intersection(self.delims))
        if set(string_command[1:]).intersection(self.delims):
            command_list = [''.join(prefix_pair) for prefix_pair in list(
                zip(split_list[1::2], split_list[2::2]))]
            if string_command[0] not in self.delims:
                command_list = split_list[0:1] + command_list
        logging.info('command list' + str(command_list))
        return command_list

    def viewtree_search(
            self,
            json_view_tree,
            search_commands,
            search_hits,
            halt_on_match=False,
            debug_mode=False,
            allow_double_matching=False,
            level=0
    ):
        '''
        perform a viewtree search on a json_view_tree using search_commands
        output the list of findings of that search
        '''
        self._set_logging()
        logging.info('Level' + str(level))
        local_search_commands = search_commands[:]
        local_search_hits = search_hits[:]
        results = []
        logging.info('called:' +
                     str(type(json_view_tree)) +
                     str(json_view_tree)
                     )
        '''
        are we at a string leaf?
        '''
        if isinstance(json_view_tree, str):
            logging.info('string leaf.  ending the search.')
            return results
        '''
        is the json_view_tree at a list?
        iterate over it
        '''
        if isinstance(json_view_tree, list):
            logging.info('found a list.  searching it.')
            for index, json_list_element in enumerate(json_view_tree):
                logging.info('recursing list item [ ' + str(index))
                results.extend(
                    self.viewtree_search(
                        json_list_element,
                        local_search_commands,
                        local_search_hits,
                        halt_on_match=halt_on_match,
                        debug_mode=debug_mode,
                        allow_double_matching=allow_double_matching,
                        level=level + 1
                    )
                )
            return results
        '''
        is the json view tree at a dict?
        iterate over the keys
        '''
        if isinstance(json_view_tree, dict):
            logging.info('found a dictionary.  searching it.')
            match = False
            for current_json_key in json_view_tree:
                '''
                let's see if the value of the json_key
                warrants further recursion
                '''
                current_json_value = json_view_tree[current_json_key]
                '''
                if the key is a recursable tag (dict, list)
                which is not classNames
                '''
                if (current_json_key in self.recursable_tags) and \
                        current_json_key != 'classNames':
                    log_message = 'recursing into ' + str(type(
                        current_json_value)) + str(current_json_value)
                    logging.info(log_message)
                    results.extend(
                        self.viewtree_search(
                            current_json_value,
                            local_search_commands,
                            local_search_hits,
                            halt_on_match=halt_on_match,
                            debug_mode=debug_mode,
                            allow_double_matching=allow_double_matching,
                            level=level + 1
                        )
                    )
                else:
                    '''
                    this entry in the JSON dictionary
                    is not recursable.
                    check it for matches with
                    the selectors
                    '''
                    if (allow_double_matching) or (not match):
                        for command_index, command in \
                                enumerate(local_search_commands):
                            if (
                                    (
                                            command.startswith('#') and
                                            (current_json_key ==
                                             'identifier') and
                                            (current_json_value ==
                                             command[1:])
                                    ) or
                                    (
                                            command.startswith('.') and
                                            (current_json_key ==
                                             'classNames') and
                                            (command[1:] in
                                             current_json_value)
                                    ) or
                                    (
                                            not command.startswith('#') and
                                            not command.startswith('.') and
                                            (current_json_key == 'class') and
                                            (current_json_value ==
                                             command[0:])
                                    )
                            ):
                                local_search_hits[command_index] += 1
                                if self.check_full_search_match(
                                        local_search_hits
                                ):
                                    result = json_view_tree
                                    match = True
                                    results.append(result)
                                    if halt_on_match:
                                        return results
        return results

    def output_results(self, results):
        '''
        format the output of
        the search results
        '''
        for finding_number, result in enumerate(results):
            print('Finding {}'.format(finding_number + 1))
            print('-' * 80)
            print(dumps(result, indent=4))
            print('-' * 80)
        print("Found 1 entry") \
            if len(results) == 1 \
            else print("Found {} entries".format(len(results)))
        return len(results)

    def viewtree_search_wrapper(self, command_string):
        command_list = self._split_string_command(command_string)
        command_hits = len(command_list) * [0]
        search_results = self.viewtree_search(
            self.json_source,
            command_list,
            command_hits,
            debug_mode=self.debug_mode
        )
        self.output_results(list(search_results))
        return search_results

    def _json_source_status(self):
        '''
        Is there JSON source data available for searching?
        This outputs the status.
        '''
        print("JSON source data is still loaded from before") \
            if self.json_source else \
            print("No JSON source data exists for viewtree searching.")
        return self.json_source is not None

    def _toggle_debug_mode(self):
        '''
        Turns off and on debug mode for the viewtree search cli
        '''
        self.debug_mode = not self.debug_mode
        print("Debug mode enabled.") if self.debug_mode else \
            print("Debug mode disabled.")
        return self.debug_mode

    def load_json_from_file(self,
                            json_file_name
                            ):
        '''
        Loads json from a file starting with ! and ending with the file name
        '''
        windowsed_file_name = json_file_name.replace('\\', '\\\\')
        try:
            with open(windowsed_file_name, 'r') as json_file_handle:
                self.json_source = load(json_file_handle)
            print('Loaded source from ', json_file_name)
            if self.debug_mode:
                print('Source: ', dumps(self.json_source, indent=4))
            success = True
        except:
            print("Error loading file: ", json_file_name)
            print("Please review the file path and name and try again.")
            self._json_source_status()
            success = False
        return success

    def print_help(self):
        '''
        Prints the help statement for viewtree_search
        '''
        print('ViewTree Search Help')
        print(
            "ViewTree Search is a CLI which allows you to load JSON "
            "from a file or from a URL and search it for various selectors.")
        print("? toggles debug mode")
        print("help-- outputs the help instructions [these]")
        print("exit-- exits the CLI")
        print("source-- outputs the current JSON source "
              "available for viewtree searching")
        print("![file name]-- allows you to load a file of "
              "JSON named file name-- don't use the brackets.  ")
        print("@[URL]-- allows you to load a URL of JSON "
              "using the specified URL-- don't use the brackets.  ")
        print("[Simple selector]-- Searches loaded JSON "
              "using the simple selector")
        print("[Compound selector]-- Searches loaded "
              "JSON using the compound selector")
        return True

    def load_json_from_url(self,
                           command_url
                           ):
        '''
        Loads json from a command string
        starting with @ and ending with the URL
        '''
        try:
            url_request = urllib.request.urlopen(command_url)
            data = url_request.read()
            encoding = url_request.info().get_content_charset('utf-8')
            self.json_source = loads(data.decode(encoding))
            print('Loaded source from ', command_url)
            if self.debug_mode:
                print('Source: ', dumps(self.json_source, indent=4))
            success = True
        except:
            print("Error loading URL ", command_url)
            print("Please review the URL/internet connection and try again.")
            self._json_source_status()
            success = False
        return success

    def _attempt_cli_exit(self):
        '''
        Confirms exit from the CLI and then exits if sure
        '''
        command_string = input("Are you sure?")
        if command_string.lower().startswith('y'):
            exit()
        else:
            print("Exit attempt cancelled.  Resuming CLI")
            self._json_source_status()
        return True

    def prompt(self):
        '''
        Prompts for command inputs and
        redirects to the appropriate functionality
        '''
        while True:
            command_string = ''
            while command_string == '':
                command_string = input(">>")
            if command_string.startswith('!'):
                self.load_json_from_file(command_string[1:])
            elif command_string == '?':
                self._toggle_debug_mode()
            elif command_string.startswith('@'):
                self.load_json_from_url(command_string[1:])
            elif command_string.lower() == 'help':
                self.print_help()
            elif command_string.lower() == 'exit':
                self._attempt_cli_exit()
            elif command_string.lower() in (
                    'easter egg', 'uuddlrlrba'):
                print("Obi-Wan: Mos Eisley spaceport. "
                      "You will never find a more wretched hive "
                      "of scum and villainy. We must be cautious.")
            elif command_string.lower() == 'source':
                print(dumps(self.json_source, indent=4)) \
                    if self.json_source \
                    else print("No JSON source has been loaded "
                               "for viewtree searching")
            else:  # this code is used to perform a viewtree
                # search since all other command options are not in play
                if not self.json_source:
                    print("No JSON source is loaded.  "
                          "Please load one from file or URL.")
                    print("Remember: typing 'help' will get you "
                          "instructions to use this CLI.")
                else:
                    self.viewtree_search_wrapper(command_string)
