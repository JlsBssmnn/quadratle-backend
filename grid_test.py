import unittest
from grid import Grid

class GridTest(unittest.TestCase):
    def test_get_neighboors(self):
        grid = Grid([['a', 'b', 'c', 'd'],
                     ['e', 'f', 'g', 'h'],
                     ['i', 'j', 'k', 'l'],
                     ['m', 'n', 'o', 'p']])
        self.assertEqual(len(grid.getNeighbors(grid.tiles[0][0])), 3)
        self.assertEqual(set(grid.getNeighbors(grid.tiles[0][0])),
                set([grid.tiles[0][1], grid.tiles[1][0], grid.tiles[1][1]]))

        self.assertEqual(len(grid.getNeighbors(grid.tiles[1][1])), 8)
        self.assertEqual(set(grid.getNeighbors(grid.tiles[1][1])),
                set([grid.tiles[0][0], grid.tiles[0][1], grid.tiles[0][2],
                     grid.tiles[1][0], grid.tiles[1][2],
                     grid.tiles[2][0], grid.tiles[2][1], grid.tiles[2][2]]))

        self.assertEqual(len(grid.getNeighbors(grid.tiles[2][3])), 5)
        self.assertEqual(set(grid.getNeighbors(grid.tiles[2][3])),
                set([grid.tiles[1][2], grid.tiles[1][3],
                     grid.tiles[2][2],
                     grid.tiles[3][2], grid.tiles[3][3]]))

        self.assertEqual(len(grid.getNeighbors(grid.tiles[3][1])), 5)
        self.assertEqual(set(grid.getNeighbors(grid.tiles[3][1])),
                set([grid.tiles[2][0], grid.tiles[2][1], grid.tiles[2][2],
                     grid.tiles[3][0], grid.tiles[3][2]]))

        self.assertEqual(len(grid.getNeighbors(grid.tiles[3][3])), 3)
        self.assertEqual(set(grid.getNeighbors(grid.tiles[3][3])),
                set([grid.tiles[2][2], grid.tiles[2][3], grid.tiles[3][2]]))

if __name__ == '__main__':
    unittest.main()
