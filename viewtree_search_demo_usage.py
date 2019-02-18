from json import load
from viewtree_search_cli import viewtree_search_cli

modal_nodes_test_file = 'the_modal_nodes.json'
mos_eisley_test_file = 'mos_eisley.json'


def output_results(results):
    for result in results:
        print(result)
    print('{} results found'.format(len(results)))


def simple_search(
        demo_search_object,
        search
):
    search_hits = [0]*len(search)
    search_results = demo_search_object.viewtree_search(
            viewtree_search_object.json_source,
            search,
            search_hits
        )
    output_results(search_results)


def search_halt_on_match_parm(
        demo_search_object,
        search,
        halt_on_match
):
    search_hits = [0]*len(search)
    search_results = demo_search_object.viewtree_search(
            viewtree_search_object.json_source,
            search,
            search_hits,
            halt_on_match=halt_on_match
        )
    output_results(search_results)

viewtree_search_object = viewtree_search_cli()
with open(modal_nodes_test_file, 'r') as test_file_handle:
    viewtree_search_object.json_source = load(test_file_handle)

simple_search(viewtree_search_object, ['Input'])
simple_search(viewtree_search_object, ['#videoMode'])
simple_search(viewtree_search_object, ['#rate'])
simple_search(viewtree_search_object, ['#supersample'])
search_halt_on_match_parm(viewtree_search_object, ['.container'], True)

with open(mos_eisley_test_file, 'r') as test_file_handle:
    viewtree_search_object.json_source = load(test_file_handle)
search_halt_on_match_parm(viewtree_search_object, ['#System'], True)
search_halt_on_match_parm(
    viewtree_search_object,
    ['#System', '.container'],
    True
)
search_halt_on_match_parm(
    viewtree_search_object,
    ['#System', '.container'],
    False
)
search_halt_on_match_parm(
    viewtree_search_object,
    ['StackView', '.container'],
    False
)
search_halt_on_match_parm(viewtree_search_object, ['CvarCheckbox'], False)
