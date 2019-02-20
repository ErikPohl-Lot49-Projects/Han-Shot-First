#!/usr/bin/env python

'''Regression tests for use when refactoring viewtree_search_cli
and to prove functionality works
'''

from unittest import TestCase
from json import load
from contextlib import redirect_stdout
import io
from viewtree_search_cli import viewtree_search_cli  

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Code Review"


class TestCases(TestCase):
    '''Test cases for the most complicated part of the ViewTree CLI'''

    def test_batches_of_cases(self):
        ''''Repeatedly call tests based on a list of test dictionaries'''
        self.modal_nodes_test_file = 'the_modal_nodes.json'
        self.mos_eisley_test_file = 'mos_eisley.json'
        test_cases = [
            {
                'case_name': 'simple selector case with user story results for class : 26 count',
                'case_file':
                    self.modal_nodes_test_file,
                'case_search_commands': ["Input"],
                'case_count': 26
            },
            {
                'case_name': 'simple selector case: videoMode identifier',
                'case_file':
                    self.modal_nodes_test_file,
                'case_search_commands': ["#videoMode"],
                'case_count': 1
            },
            {
                'case_name': 'simple selector case: rate identifier',
                'case_file':
                    self.modal_nodes_test_file,
                'case_search_commands': ["#rate"],
                'case_count': 1
            },
            {
                'case_name': 'simple selector case: supersample identifier',
                'case_file':
                    self.modal_nodes_test_file,
                'case_search_commands': ["#supersample"],
                'case_count': 1
            },
            {
                'case_name': 'simple selector case: classNames container',
                'case_file':
                    self.modal_nodes_test_file,
                'case_search_commands': [".container"],
                'case_count': 6
            },
            {
                'case_name': 'a simple selector finds a match '
                             'then does not explore inside its children',
                'case_file':
                    self.modal_nodes_test_file,
                'case_search_commands': ['StackView'],
                'case_count': 6
            },
            {
                'case_name': 'embedded in wrong parent type -- label',
                'case_file':
                    self.mos_eisley_test_file,
                'case_search_commands': ['CvarCheckbox'],
                'case_count': 0
            },
            {
                'case_name':
                    'a complete compound match contains '
                    'another complete match-- the second is disregarded',
                'case_file':
                    self.mos_eisley_test_file,
                'case_search_commands': ['#System', '.container'],
                'case_count': 2
            },
            {
                'case_name': 'before combinator, compound',
                'case_file':
                    self.mos_eisley_test_file,
                'case_search_commands': ['StackView', '.container'],
                'case_count': 2
            },
            {
                'case_name': 'before combinator, compound',
                'case_file':
                    self.mos_eisley_test_file,
                'case_search_commands': ['Ponda_Baba'],
                'case_count': 2
            }
        ]
        output_redirect = io.StringIO()
        with redirect_stdout(output_redirect):
            viewtree_search_object = viewtree_search_cli.viewtree_search_cli()
            for test_case in test_cases:
                with open(test_case['case_file'], 'r') as test_file_handle:
                    viewtree_search_object.json_source = load(test_file_handle)
                    test_hits = [0]*len(test_case['case_search_commands'])
                    self.assertEqual(
                        len(
                            viewtree_search_object.viewtree_search(
                                viewtree_search_object.json_source,
                                test_case['case_search_commands'],
                                test_hits,
                                halt_on_match=False
                            )
                        ),
                        test_case['case_count']
                    )
                    
    def test_json_source_status(self):
        viewtree_search_object = viewtree_search_cli.viewtree_search_cli()
        self.assertEqual(viewtree_search_object._json_source_status(), False)
        viewtree_search_object.json_source = 'x'
        self.assertEqual(viewtree_search_object._json_source_status(), True)

    def test_split_string_command(self):
        viewtree_search_object = viewtree_search_cli.viewtree_search_cli()
        self.assertEqual(viewtree_search_object._split_string_command('Input'), ['Input'])
        self.assertEqual(viewtree_search_object._split_string_command('Input#identifier'), ['Input', '#identifier'])
        self.assertEqual(viewtree_search_object._split_string_command('Input#identifier.container'), ['Input', '#identifier', '.container'])
        self.assertEqual(viewtree_search_object._split_string_command('#identifier'), ['#identifier'])
        self.assertEqual(viewtree_search_object._split_string_command('#identifier.container'), ['#identifier', '.container'])
