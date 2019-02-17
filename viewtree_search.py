from json import load
import logging
import sys


def viewtree_search(json_view_tree, search_commands, search_hits, halt_on_match=False):
    recursable_tags = ('subviews', 'contentView', 'input', 'control')
    search_commands2 = search_commands[:]
    search_hits2 = search_hits[:]
    #logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
    count = 0
    logging.info('called;'+str(type(json_view_tree)) + str(json_view_tree))
    if isinstance(json_view_tree, str):
        logging.info('string leaf')
        return count
    if isinstance(json_view_tree, list):
        logging.info('scanning list')
        for index, json_list_element in enumerate(json_view_tree):
            logging.info('recursing list item [ ' + str(index))
            count += viewtree_search(json_list_element, search_commands2, search_hits2, halt_on_match=halt_on_match)
        return count
    if isinstance(json_view_tree, dict):
        logging.info('indict')
        for json_list_element in json_view_tree.keys():
            if isinstance(json_view_tree[json_list_element], dict) or (json_list_element != 'classNames' and isinstance(json_view_tree[json_list_element], list)):
                if json_list_element in recursable_tags:
                    logging.info(str(type(json_view_tree[json_list_element]))+ str(json_view_tree[json_list_element]))
                    logging.info('calling')
                    count += viewtree_search(json_view_tree[json_list_element], search_commands2, search_hits2, halt_on_match=halt_on_match)
            else:
                for command_index, command in enumerate(search_commands2):
                    if command.startswith('#'):
                        logging.info('trying identifier [' + json_list_element + ']')
                        if (json_list_element == 'identifier') and (json_view_tree[json_list_element] == command[1:]):
                            search_hits2[command_index] +=1
                            if len([x for x in search_hits2 if x > 0])  == len(search_hits2):
                                print(str(json_view_tree))
                                count+=1
                                if halt_on_match:
                                    return 1
                    elif command.startswith('.'):
                        if (json_list_element == 'classNames') and (command[1:] in json_view_tree[json_list_element]):
                            search_hits2[command_index] +=1
                            logging.info('found in '+ str(json_view_tree[json_list_element]))
                            if len([x for x in search_hits2 if x > 0])  == len(search_hits2):
                                print(json_view_tree)
                                count+=1
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
