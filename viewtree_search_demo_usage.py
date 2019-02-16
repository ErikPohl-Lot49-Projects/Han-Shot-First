from json import load
from viewtree_search import viewtree_search

with open('C:\\Users\\Richard Pendrake\\Downloads\\the_modal_nodes.json','r') as f1:
    z = load(f1)

search_hits = [0]
mysearch = ['Input']
output = viewtree_search(z,mysearch , search_hits)
print(output)
mysearch = ['#videoMode']
output = viewtree_search(z,mysearch , search_hits )
print(output)
mysearch = ['#rate']
output = viewtree_search(z,mysearch , search_hits )
print(output)
mysearch = ['#supersample']
output = viewtree_search(z,mysearch , search_hits )
print(output)
mysearch = ['.container']
output = viewtree_search(z,mysearch , search_hits, halt_on_match=True )
print(output)


with open('C:\\Users\\Richard Pendrake\\Downloads\\mos_eisley.json','r') as f1:
    z = load(f1)
search_hits = [0,0]
mysearch = ['#System', '.container']
output = viewtree_search(z,mysearch , search_hits, halt_on_match=True )
print(output)
mysearch = ['#System', '.container']
output = viewtree_search(z,mysearch , search_hits, halt_on_match=False)
print(output)
