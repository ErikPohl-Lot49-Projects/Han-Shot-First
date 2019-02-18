from json import load
from viewtree_search_cli import viewtree_search_cli


def perform_search(
        demo_search_object,
        search,
        halt_on_match
):
    '''This is a wrapper for the viewtree search method call'''
    search_hits = [0]*len(search)
    search_results = demo_search_object.viewtree_search(
            viewtree_search_object.json_source,
            search,
            search_hits,
            halt_on_match=halt_on_match
        )
    demo_search_object.output_results(search_results)
    return True

if __name__ == "__main__":
    ''' Main demo usage functionality'''

    '''Create an object for use in searching'''
    viewtree_search_object = viewtree_search_cli()

    modal_nodes_test_file = 'the_modal_nodes.json'
    mos_eisley_test_file = 'mos_eisley.json'

    viewtree_search_object.load_json_from_file(modal_nodes_test_file)

    perform_search(viewtree_search_object, ['Input'], False)
    perform_search(viewtree_search_object, ['#videoMode'], False)
    perform_search(viewtree_search_object, ['#rate'], False)
    perform_search(viewtree_search_object, ['#supersample'], False)
    perform_search(viewtree_search_object, ['.container'], False)

    viewtree_search_object.load_json_from_file(mos_eisley_test_file)
    perform_search(viewtree_search_object, ['#System'], True)
    perform_search(
        viewtree_search_object,
        ['#System', '.container'],
        True
    )
    perform_search(
        viewtree_search_object,
        ['#System', '.container'],
        False
    )
    perform_search(
        viewtree_search_object,
        ['StackView', '.container'],
        False
    )
    perform_search(viewtree_search_object, ['CvarCheckbox'], False)
