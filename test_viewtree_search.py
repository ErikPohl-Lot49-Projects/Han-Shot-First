from unittest import TestCase
from JnesaisQ.viewtree_search import viewtree_search
from json import load


class TestCases(TestCase):
    
    def testcase1(self):
        with open('C:\\Users\\p636205\\workspace\\jnesaisq\\JnesaisQ\\the_modal_nodes.json','r') as f1:
            z = load(f1)
        self.assertEqual(viewtree_search(z, ["Input"]), 26)
