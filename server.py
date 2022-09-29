from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from collections import Counter
from hashlib import sha256
import socketserver
from typing import Dict

from utils import createTodaysSquaredle
from grid import Grid, List
from trie import Trie, TrieNode
from os import environ
from flask import Flask
from flask_cors import CORS, cross_origin

hostName = "0.0.0.0"
serverPort = int(environ.get('PORT', '8080'))

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class CachedSquaredle:
    day: str
    grid: Grid
    solution: List[str]
    wordCounts: Dict[int, int]

    def __init__(self) -> None:
        self.updateCache()

    def updateCache(self):
        self.day = datetime.today().strftime('%d/%m/%y')
        
        grid, solution = createTodaysSquaredle(4, './wortTrie.pkl')
        self.grid = grid
        self.solution = solution
        self.counts = Counter([len(x) for x in solution])

    def createFrontendRes(self):
        if self.day != datetime.today().strftime('%d/%m/%y'):
            self.updateCache()
        
        return {"grid": [[tile.content for tile in row] for row in self.grid.tiles],
                "counts": self.counts,
                "solution": [sha256(x.encode("utf8")).hexdigest() for x in self.solution]}

cache = CachedSquaredle() 

@app.route('/')
def getGrid():
    return cache.createFrontendRes()

if __name__ == "__main__":        
    app.secret_key = ''
    app.run(host=hostName, port=serverPort)
