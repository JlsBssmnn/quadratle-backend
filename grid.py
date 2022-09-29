import itertools
from typing import List

class Tile:
    row: int
    column: int
    content: str

    def __init__(self, row: int, column: int, content: str) -> None:
        self.row = row
        self.column = column
        self.content = content

class Grid:
    tiles: List[List[Tile]]
    dimensionality: int

    def __init__(self, field: List[List[str]]) -> None:
        fieldCount = sum([len(x) for x in field])
        assert fieldCount == 16 or fieldCount == 25
        self.tiles = []

        for row, rowContent in enumerate(field):
            self.tiles.append([])
            for column, tileContent in enumerate(rowContent):
                self.tiles[row].append(Tile(row, column, tileContent))

        self.dimensionality = len(field)

    def __repr__(self) -> str:
        s = ""
        for row in self.tiles:
            for tile in row:
                s += tile.content + " "
            s += '\n'
        return s

    def getNeighbors(self, tile: Tile) -> List[Tile]:
        tileList: List[Tile] = []
        for move in list(itertools.product([-1, 0, 1], repeat=2)):
            if move == (0, 0):
                continue
            newRow = tile.row + move[0]
            newColumn = tile.column + move[1]
            if 0 <= newRow < self.dimensionality and 0 <= newColumn < self.dimensionality:
                tileList.append(self.tiles[newRow][newColumn])

        return tileList

