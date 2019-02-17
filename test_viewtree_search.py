from unittest import TestCase
from viewtree_search import viewtree_search
from viewtree_search_cli import viewtree_search_cli
from json import load
from contextlib import redirect_stdout
import io


class TestCases(TestCase):

    def test_batches_of_cases(self):
        test_cases = [
            {'case_name' : 'test_case1',
             'case_file' :  'C:\\Users\\Richard Pendrake\\Downloads\\the_modal_nodes.json',
             'case_search_commands' : ["Input"],
             'case_count' : 26
             },
            {'case_name': 'test_case2',
             'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\the_modal_nodes.json',
             'case_search_commands': ["#videoMode"],
             'case_count': 1
             },
            {'case_name': 'test_case3',
             'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\the_modal_nodes.json',
             'case_search_commands': ["#rate"],
             'case_count': 1
             },
            {'case_name': 'test_case4',
             'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\the_modal_nodes.json',
             'case_search_commands': ["#supersample"],
             'case_count': 1
             },
            {'case_name': 'test_case5',
             'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\the_modal_nodes.json',
             'case_search_commands': [".container"],
             'case_count': 6
             },
            {'case_name': 'a simple selector finds a match then does not explore inside its children',
             'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\the_modal_nodes.json',
             'case_search_commands': ['StackView'],
             'case_count': 6
             },
            {'case_name': 'embedded in wrong parent type -- label',
             'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\mos_eisley.json',
             'case_search_commands': ['CvarCheckbox'],
             'case_count': 0
             },

             {'case_name': 'a complete compound match contains another complete match-- the second is disregarded',
              'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\mos_eisley.json',
              'case_search_commands': ['#System', '.container'],
              'case_count': 2
              },
            {'case_name': 'before combinator, compound',
             'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\mos_eisley.json',
             'case_search_commands': ['StackView', '.container'],
             'case_count': 2
             }
            #,
            #{'case_name': 'with combinator, complex/chain with descendent',
            # 'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\mos_eisley.json',
            # 'case_search_commands': ['StackView', ' ', '.container'],
            # 'case_count': 2
            # }
        ]
        f = io.StringIO()
        with redirect_stdout(f):
            vts_cli = viewtree_search_cli()
            for test_case in test_cases:
                with open(test_case['case_file'], 'r') as f1:
                    vts_cli.json_source = load(f1)
                test_hits = [0]*len(test_case['case_search_commands'])
                self.assertEqual(vts_cli.viewtree_search(vts_cli.json_source,test_case['case_search_commands'], test_hits, halt_on_match=False ), test_case['case_count'])

