from pathlib import Path
from trie import Trie, TrieNode
from grid import Grid, List
from SolutionFinder import SolutionFinder
import random
import string
import pickle
import argparse
from datetime import datetime
from hashlib import sha256

def createTrie(filePath: str, destination: str):
    with open(filePath, 'r', encoding='utf8') as words:
        words = words.readlines()

    trie = Trie()
    for word in words:
        word = word.replace("\n", "").lower()
        trie.insertString(word)

    with open(destination, 'wb') as write_file:
        pickle.dump(trie, write_file)

def createGrid(dimensionality):
    grid: List[List[str]] = []

    for _ in range(dimensionality):
        grid.append([])
        for _ in range(dimensionality):
            grid[-1].append(random.choice(string.ascii_lowercase + 'äöü'))
    return Grid(grid)

def createTodaysSquaredle(dimensionality: int, wordTrieFile: str, minLen: int = 10):
    with open((Path(__file__).parent / wordTrieFile).resolve(), 'rb') as read_file:
        wordTrie = pickle.load(read_file)

    random.seed(sha256(datetime.today().strftime('%d/%m/%y').encode("utf8")).hexdigest())

    while True:
        grid = createGrid(dimensionality)
        solver = SolutionFinder(grid, wordTrie)
        solution = solver.findSolutions()
        if len(solution) > 10:
            return grid, solution

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    createTrieParser = subparsers.add_parser('create_trie', help='Creates a trie datastructure out of a file of words')
    createTrieParser.add_argument('-f', '--file', required=True, help='The path to the file with the words')
    createTrieParser.add_argument('-o', '--output', required=True, help='The path where the trie datastructure shall be written to')

    createGridParser = subparsers.add_parser('create_grid', help='Creates a random grid')
    createGridParser.add_argument('-d', '--dimensionality', default=4, help='The dimensionality')

    todaysSquaredleParser = subparsers.add_parser('squaredle', help='Shows todays squaredle')
    todaysSquaredleParser.add_argument('-d', '--dimensionality', default=4, help='The dimensionality')
    todaysSquaredleParser.add_argument('-t', '--trie', default='./wortTrie.pkl', help='The file to the word trie')
    todaysSquaredleParser.add_argument('-l', '--len', default=10, help='The minimum number of solutions in the squaredle')

    args = parser.parse_args()

    if args.command == 'create_trie':
        createTrie(args.file, args.output)
    elif args.command == 'create_grid':
        print(createGrid(args.dimensionality))
    elif args.command == 'squaredle':
        squaredle = createTodaysSquaredle(args.dimensionality, args.trie, args.len)
        print(squaredle[0])
        print(squaredle[1])

