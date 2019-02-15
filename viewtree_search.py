from json import load
import logging
import sys

def viewtree_search(json_view_tree, search_commands):
    recursable_tags = ('subviews', 'contentView', 'input', 'control')
    #logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    count = 0 
    logging.info('called;', type(json_view_tree),json_view_tree)
    if isinstance(json_view_tree, str):
        logging.info('string leaf')
        return count
    if isinstance(json_view_tree, list):
        logging.info('scanning list')
        for c,i in enumerate(json_view_tree):
            logging.info('recursing list item [ ' + str(c))
            count += viewtree_search(i, search_commands)
        return count
    if isinstance(json_view_tree,dict): 
        logging.info('indict')
        for i in json_view_tree.keys():
            if isinstance(json_view_tree[i],dict) or (i != 'classNames' and isinstance(json_view_tree[i],list)):
                if i in recursable_tags:
                    logging.info(type(json_view_tree[i]), json_view_tree[i])
                    logging.info('calling')
                    count += viewtree_search(json_view_tree[i], search_commands)
            else:
                for command in search_commands:
                    if command.startswith('#'):
                        logging.info('trying identifier [' + i + ']')
                        if (i=='identifier') and (json_view_tree[i] == command[1:]):
                            print(25*'#'+i + ' : ' + json_view_tree[i])
                            count +=1
                    elif command.startswith('.'):
                        if (i == 'classNames') and (command[1:] in json_view_tree[i]):
                            logging.info(json_view_tree[i])
                            print(25*'>'+i + ' : ' + ''.join(json_view_tree[i]))
                            count +=1
                    elif  (i == 'class') and (json_view_tree[i] == command[0:]):
                        print(25*'*'+i + ' : ' + json_view_tree[i])
                        count +=1
                        
    return count


