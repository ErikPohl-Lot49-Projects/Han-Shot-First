from json import load, loads
from viewtree_search import viewtree_search
import urllib
import urllib.request

#command_string = input(">>")

class viewtree_search_cli:

    def __init__(self):
        self.delims = ('#', '.', '!', '@')
        self.json_source = None
        print("ViewTree Search")
        print("Type 'help' for instructions for use.")

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


    def prompt(self):
        while True:
            command_string = input(">>")
            if command_string.startswith('!'):
                with open(command_string[1:], 'r') as f1:
                    self.json_source = load(f1)
                print('loaded source from ', command_string[1:])
            elif command_string.startswith('@'):
                s = urllib.request.urlopen(command_string[1:])
                data = s.read()
                encoding = s.info().get_content_charset('utf-8')
                self.json_source = loads(data.decode(encoding))
                print('loaded source from ', command_string[1:])
                print(self.json_source)
            elif command_string.lower() == 'help':
                print('help')
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
                    zx = viewtree_search(self.json_source, command_list, command_hits)
                    print("Found {} entries".format(zx))



z = viewtree_search_cli()
z.prompt()
