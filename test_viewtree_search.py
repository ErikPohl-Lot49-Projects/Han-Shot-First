#!/usr/bin/env python

'''Regression tests for use when refactoring viewtree_search_cli
and to prove functionality works
'''

from unittest import TestCase
from json import load
from contextlib import redirect_stdout
import io
import viewtree_search_cli

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

    def test_viewtree_searches_case_sensitive(self):
        '''
        For a list of test cases,
        load a test file, run a selector search against it using
        the viewtree search method, and compare
        the result against expected results
        '''
        self.modal_nodes_test_file = 'the_modal_nodes.json'
        self.mos_eisley_test_file = 'mos_eisley.json'
        test_cases = [
            {
                'case_name': 'simple selector case: Input class : 26 count',
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
                'case_search_commands': ['Ponda_Baba', '.Doctor_Evazan'],
                'case_count': 2  # this is a case I'd like to discuss
            },
            {
                'case_name': 'reserved words test',
                'case_file':
                    self.mos_eisley_test_file,
                'case_search_commands': ['source', '.help', '.exit'],
                'case_count': 1  # this is a case I'd like to discuss
            }
        ]
        last_loaded_file = None
        output_redirect = io.StringIO()
        with redirect_stdout(output_redirect):
            viewtree_search_object = viewtree_search_cli.viewtree_search_cli()
            for test_case in test_cases:
                if test_case['case_file'] != last_loaded_file:
                    viewtree_search_object.load_json_from_file(
                        test_case['case_file']
                    )
                    last_loaded_file = test_case['case_file']
                self.assertEqual(
                    len(
                        viewtree_search_object.viewtree_search(
                            test_case['case_search_commands']
                        )
                    ),
                    test_case['case_count'],
                    msg='Testing case [' + test_case['case_name'] + ']'
                )

    def test_viewtree_searches_case_insensitive(self): 
            '''
            For a list of test cases,
            load a test file, run a selector search against it using
            the viewtree search method, and compare
            the result against expected results
            '''
            self.modal_nodes_test_file = 'the_modal_nodes.json'
            self.mos_eisley_test_file = 'mos_eisley.json'
            test_cases = [
                {
                    'case_name': 'reserved words test',
                    'case_file':
                        self.mos_eisley_test_file,
                    'case_search_commands': ['source'],
                    'case_count': 1  
                },
                {
                    'case_name': 'reserved words test',
                    'case_file':
                        self.mos_eisley_test_file,
                    'case_search_commands': ['.exit'],
                    'case_count': 1  
                },
                {
                    'case_name': 'reserved words test',
                    'case_file':
                        self.mos_eisley_test_file,
                    'case_search_commands': ['.help'],
                    'case_count': 1  
                }
            ]
            last_loaded_file = None
            output_redirect = io.StringIO()
            with redirect_stdout(output_redirect):
                viewtree_search_object = viewtree_search_cli.viewtree_search_cli()
                viewtree_search_object.case_sensitive_search = False
                for test_case in test_cases:
                    if test_case['case_file'] != last_loaded_file:
                        viewtree_search_object.load_json_from_file(
                            test_case['case_file']
                        )
                        last_loaded_file = test_case['case_file']
                    self.assertEqual(
                        len(
                            viewtree_search_object.viewtree_search(
                                test_case['case_search_commands']
                            )
                        ),
                        test_case['case_count'],
                        msg='Testing case [' + test_case['case_name'] + ']'
                    )
    
    def test_json_source_status(self):
            '''
            these tests confirm the source status check
            works as expected
            '''
            output_redirect = io.StringIO()
            with redirect_stdout(output_redirect):
                viewtree_search_object = viewtree_search_cli.viewtree_search_cli()
                self.assertEqual(
                    False,
                    viewtree_search_object._json_source_status(),
                    msg="Has No JSON: JSON Source Status Test"
                )
                viewtree_search_object.json_source = 'x'
                self.assertEqual(
                    True,
                    viewtree_search_object._json_source_status(),
                    msg="Has JSON: JSON Source Status Test"
                )
    
    def test_split_string_command(self):
            '''
            For a list of test cases,
            split a command string using the
            split method
            and compare against expected list results
            '''
            output_redirect = io.StringIO()
            test_cases = [
                {
                    'case_name': 'simple selector: class',
                    'case_command_string': "Input",
                    'case_command_list': ['Input']
                },
                {
                    'case_name': 'compound selector: class identifier',
                    'case_command_string': 'Input#identifier',
                    'case_command_list': [
                        'Input', '#identifier'
                    ]
                },
                {
                    'case_name': 'compound selector: class className',
                    'case_command_string': 'Input.container',
                    'case_command_list': [
                        'Input', '.container'
                    ]
                },
                {
                    'case_name': 'compound selector: class identifier className',
                    'case_command_string': 'Input#identifier.container',
                    'case_command_list': [
                        'Input', '#identifier', '.container'
                    ]
                },
                {
                    'case_name': 'simple selector: identifier',
                    'case_command_string': '#identifier',
                    'case_command_list': ['#identifier']
                },
                {
                    'case_name': 'compound selector: identifier className',
                    'case_command_string': '#identifier.container',
                    'case_command_list': ['#identifier', '.container']
                },
                {
                    'case_name': 'simple selector: className',
                    'case_command_string': '.container',
                    'case_command_list': ['.container']
                }
            ]
            with redirect_stdout(output_redirect):
                viewtree_search_object = viewtree_search_cli.viewtree_search_cli()
                for test_case in test_cases:
                    self.assertEqual(
                        test_case['case_command_list'],
                        viewtree_search_object._split_string_command(
                            test_case['case_command_string']
                        ),
                        msg=test_case['case_name']
                    )
