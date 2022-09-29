from typing import Set
from grid import Grid, List, Tile

class TileSet:
    tiles: Set[Tile]

    def __init__(self, *initalTiles: Tile) -> None:
        self.tiles = set(initalTiles)

    def add(self, tile: Tile) -> 'TileSet':
        if not self.has(tile):
            self.tiles.add(tile)
        return self

    def has(self, tile: Tile) -> bool:
        return any([otherTile.row == tile.row and otherTile.column == tile.column for otherTile in self.tiles])

class SolutionFinder:
    solution: Set[str]

    def __init__(self, grid: Grid, trie):
        self.solution = set()
        self.grid = grid
        self.trie = trie

    def findSolutions(self) -> List[str]:
        for tileRow in self.grid.tiles:
            for tile in tileRow:
                self.dfs(tile, tile.content, TileSet(tile))

        return [x for x in self.solution if len(x) > 3]

    def dfs(self, tile: Tile, currentWord: str, currentPath: TileSet):
        trieResult =  self.trie.searchString(currentWord)
        if trieResult == 0:
            # there is no word which starts with currentWord
            return
        elif trieResult == 1:
            self.solution.add(currentWord)

        for nextTile in self.grid.getNeighbors(tile):
            if not currentPath.has(nextTile):
                self.dfs(nextTile, currentWord + nextTile.content, currentPath.add(nextTile))
