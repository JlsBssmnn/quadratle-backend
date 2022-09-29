import unittest
import pickle

from pathlib import Path
from SolutionFinder import SolutionFinder
from grid import Grid
from trie import Trie, TrieNode

class SolutionFinderTest(unittest.TestCase):
    def setUp(self) -> None:
        with open((Path(__file__).parent / '../wortTrie.pkl').resolve(), 'rb') as read_file:
            wordTrie = pickle.load(read_file)
        self.trie: Trie = wordTrie


    def test_solution_finder1(self):
        grid = Grid([["a","g","j","t"],
                     ["r","t","e","i"],
                     ["i","v","s","z"],
                     ["ü","x","ö","ö"]])
        finder = SolutionFinder(grid, self.trie)
        solution = finder.findSolutions()

        self.assertTrue('tage' in solution)
        self.assertTrue('zeit' in solution)
        self.assertTrue('test' in solution)
        self.assertTrue('geist' in solution)

        self.assertFalse('üxöö' in solution)
        self.assertFalse('ixsit' in solution)
        self.assertFalse('atseit' in solution)
        self.assertFalse('özitj' in solution)

    def test_solution_finder2(self):
        grid = Grid([["h","a","l","l"],
                     ["a","u","s","o"],
                     ["-","t","t","e"],
                     ["-","-","n","e"]])
        finder = SolutionFinder(grid, self.trie)
        solution = finder.findSolutions()

        self.assertTrue(
                set(['husten', 'huste', 'hallo', 'laut', 'haut', 'haus', 'hast', 'hatte',
                    'test', 'laus', 'soll', 'tust', 'hause'])
                .issubset(set(solution)))

if __name__ == '__main__':
    unittest.main()
