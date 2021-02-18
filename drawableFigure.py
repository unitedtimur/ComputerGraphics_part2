import tkinter as tk
import numpy as np

from figure import VERTEXES, EDGES
from functionality import CKM_to_CKH, CKH_to_CKK, CKK_to_CKEi

h = 600
w = 1200
root = tk.Tk()
cv = tk.Canvas(root, width=1200, height=600, bg='white')


class Figure:
    def __init__(self):
        self.vertexes = np.array(VERTEXES)
        self.edges = np.array(EDGES)


class DrawableFigure:
    def __init__(self, WatcherPoint):
        self.figure = Figure()
        self.x = WatcherPoint[0]
        self.y = WatcherPoint[1]
        self.z = WatcherPoint[2]
        self.lines = []

        # Метод упаковки по умолчанию (по простому размещение)
        cv.pack()

        def key(event):
            if event.char == 'a':
                self.move(event, [-1, 0, 0])
            elif event.char == 'd':
                self.move(event, [1, 0, 0])
            elif event.char == 'w':
                self.move(event, [0, 1, 0])
            elif event.char == 's':
                self.move(event, [0, -1, 0])
            elif event.char == 'q':
                self.move(event, [0, 0, 1])
            elif event.char == 'e':
                self.move(event, [0, 0, -1])

        root.bind("<Key>", lambda event: key(event))

        self.s = None
        # Рисуем
        self.drawFigure()

    def move(self, event, d):
        self.x += d[0]
        self.y += d[1]
        self.z += d[2]

        M = self.figure.vertexes
        M, s = CKM_to_CKH(M, [self.x, self.y, self.z])
        M = CKH_to_CKK(M, self.s)
        M = CKK_to_CKEi(M, 10, w / 2, h / 2, 400, 400)

        self.update(M)

    def drawFigure(self) -> None:
        M = self.figure.vertexes
        M, self.s = CKM_to_CKH(M, [self.x, self.y, self.z])
        M = CKH_to_CKK(M, self.s)
        M = CKK_to_CKEi(M, 10, w / 2, h / 2, 400, 400)

        self.lines.append(cv.create_line(M[self.figure.edges[0][0], 0],
                                         M[self.figure.edges[0][0], 1],
                                         M[self.figure.edges[0][1], 0],
                                         M[self.figure.edges[0][1], 1], fill="red"))

        self.lines.append(cv.create_line(M[self.figure.edges[1][0], 0],
                                         M[self.figure.edges[1][0], 1],
                                         M[self.figure.edges[1][1], 0],
                                         M[self.figure.edges[1][1], 1], fill="green"))

        self.lines.append(cv.create_line(M[self.figure.edges[2][0], 0],
                                         M[self.figure.edges[2][0], 1],
                                         M[self.figure.edges[2][1], 0],
                                         M[self.figure.edges[2][1], 1], fill="blue"))

        for edge in self.figure.edges[3:]:
            self.lines.append(cv.create_line(M[edge[0], 0], M[edge[0], 1], M[edge[1], 0], M[edge[1], 1], width="3"))

    def update(self, M) -> None:
        for i in range(0, self.figure.edges.shape[0]):
            cv.coords(self.lines[i], M[self.figure.edges[i][0], 0],
                      M[self.figure.edges[i][0], 1], M[self.figure.edges[i][1], 0],
                      M[self.figure.edges[i][1], 1])