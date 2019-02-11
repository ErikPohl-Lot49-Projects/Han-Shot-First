from json import loads, load
from JnesaisQ import JnesaisQ, jnesaisq_compare

with open('C:\\the_modal_nodes.json','r') as f1:
    z = load(f1)

with open('C:\\format.json','r') as f1:
    json_query_format = load(f1)

print(z)
print(json_query_format)

JNSQ = JnesaisQ(json_query_format)
result = JNSQ.compare_verbose(z, debug_mode=1)
