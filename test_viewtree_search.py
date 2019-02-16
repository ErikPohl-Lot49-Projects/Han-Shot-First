from unittest import TestCase
from viewtree_search import viewtree_search
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
             'case_count': 1
             },
            {'case_name': 'test_case6',
             'case_file': 'C:\\Users\\Richard Pendrake\\Downloads\\the_modal_nodes.json',
             'case_search_commands': ['CvarSelect', '#rate'],
             'case_count': 1
             }
        ]
        f = io.StringIO()
        with redirect_stdout(f):
            for test_case in test_cases:
                with open(test_case['case_file'], 'r') as f1:
                    z = load(f1)
                self.assertEqual(viewtree_search(z,test_case['case_search_commands'] ), test_case['case_count'])
