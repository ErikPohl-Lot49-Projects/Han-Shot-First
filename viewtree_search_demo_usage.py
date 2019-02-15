from json import load
from JnesaisQ.garindan import viewtree_search

with open('C:\\Users\\p636205\\workspace\\jnesaisq\\JnesaisQ\\the_modal_nodes.json','r') as f1:
    z = load(f1)

with open('C:\\Users\\p636205\\workspace\\jnesaisq\\JnesaisQ\\format.json','r') as f1:
    json_query_format = load(f1)
mysearch = ['Input']
output = viewtree_search(z,mysearch )
print(output)
mysearch = ['#videoMode']
output = viewtree_search(z,mysearch )
print(output)
mysearch = ['#rate']
output = viewtree_search(z,mysearch )
print(output)
mysearch = ['#supersample']
output = viewtree_search(z,mysearch )
print(output)
mysearch = ['.container']
output = viewtree_search(z,mysearch )
print(output)
