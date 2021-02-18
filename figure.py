from typing import List, Union, Any

VERTEXES: List[Union[List[int], List[Union[int, float]]]] = [
    [0, 0, 0],
    [5, 0, 0],
    [0, 5, 0],
    [0, 0, 5],
    [0, 2, 1.5],
    [0, -2, 1.5],
    [0, -2, -1.5],
    [0, 2, -1.5],
    [2, 0, 1.5],
    [2, 0, -1.5]]

EDGES: List[Union[List[int], Any]] = [
    [0, 1],
    [0, 2],
    [0, 3],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [4, 8],
    [8, 5],
    [6, 9],
    [9, 7],
    [8, 9]]
