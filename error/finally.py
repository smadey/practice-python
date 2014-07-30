
import time


def readFile(path):
    try:
        f = open(path)
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            time.sleep(2)
            print(line, end = '')
    finally:
        f.close()
        print('Cleaning up...closed the file')

readFile('..\stream\poem.txt')