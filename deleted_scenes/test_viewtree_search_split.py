#!/usr/bin/env python

'''Regression tests for use when refactoring viewtree_search_cli
and to prove functionality works
'''

import pytest
import viewtree_search_cli

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Code Review"


@pytest.mark.parametrize("case_name, "
                         "case_command_string, "
                         "expected_command_list,",
                         [
                             (
                                     'simple selector: class',
                                     'Input',
                                     ['Input']
                             ),
                             (
                                     'compound selector: class identifier',
                                     'Input#identifier',
                                     [
                                         'Input', '#identifier'
                                     ]
                             ),
                             (
                                     'compound selector: class className',
                                     'Input.container',
                                     [
                                         'Input', '.container'
                                     ]
                             ),
                             (
                                     'compound selector: class identifier className',
                                     'Input#identifier.container',
                                     [
                                         'Input', '#identifier', '.container'
                                     ]
                             ),
                             (
                                     'simple selector: identifier',
                                     '#identifier',
                                     ['#identifier']
                             ),
                             (
                                     'compound selector: identifier className',
                                     '#identifier.container',
                                     ['#identifier', '.container']
                             ),
                             (
                                     'simple selector: className',
                                     '.container',
                                     ['.container']
                             )
                         ]
                         )
def test_eval(case_name, case_command_string, expected_command_list):
    viewtree_search_object = viewtree_search_cli.viewtree_search_cli()
    assert viewtree_search_object._split_string_command(case_command_string) == expected_command_list
