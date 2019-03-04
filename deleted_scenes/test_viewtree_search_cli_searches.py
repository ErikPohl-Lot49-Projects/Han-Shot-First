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
                         "case_file, "
                         "case_search_commands, "
                         "expected_count",
                         [
                             ('simple selector case: Input class : 26 count',
                              'the_modal_nodes.json',
                              ["Input"],
                              26
                              ),
                             (
                                     'simple selector case: '
                                     'videoMode identifier',
                                     'the_modal_nodes.json',
                                     ["#videoMode"],
                                     1
                             ),
                             (
                                     'simple selector case: rate identifier',
                                     'the_modal_nodes.json',
                                     ["#rate"],
                                     1
                             ),
                             (
                                     'simple selector case: '
                                     'supersample identifier',
                                     'the_modal_nodes.json',
                                     ["#supersample"],
                                     1
                             ),
                             (
                                     'simple selector case: '
                                     'classNames container',
                                     'the_modal_nodes.json',
                                     [".container"],
                                     6
                             ),
                             (
                                     'a simple selector finds a match '
                                     'then does not explore inside '
                                     'its children',
                                     'the_modal_nodes.json',
                                     ['StackView'],
                                     6
                             ),
                             (
                                     'embedded in wrong parent type -- label',
                                     'mos_eisley.json',
                                     ['CvarCheckbox'],
                                     0
                             ),
                             (
                                     'a complete compound match contains '
                                     'another complete match-- '
                                     'the second is disregarded',
                                     'mos_eisley.json',
                                     ['#System', '.container'],
                                     2
                             ),
                             (
                                     'before combinator, compound',
                                     'mos_eisley.json',
                                     ['StackView', '.container'],
                                     2
                             ),
                             (
                                     'before combinator, compound',
                                     'mos_eisley.json',
                                     ['Ponda_Baba', '.Doctor_Evazan'],
                                     2  # this is a case I'd like to discuss
                             ),
                             (
                                     'reserved words test',
                                     'mos_eisley.json',
                                     ['source', '.help', '.exit'],
                                     1  # this is a case I'd like to discuss
                             )
                         ])
def test_eval(case_name, case_file, case_search_commands, expected_count):
    viewtree_search_object = viewtree_search_cli.viewtree_search_cli()
    viewtree_search_object.load_json_from_file(
        case_file
    )
    assert len(
        viewtree_search_object.viewtree_search(
            viewtree_search_object.json_source,
            case_search_commands,
            halt_on_match=False
        )
    ) == expected_count
