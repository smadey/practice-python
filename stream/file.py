
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

def writeFile(path, content):
    f = open(path, 'w')
    f.write(content)
    f.close()

def readFile(path):
    f = open(path)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end = '')
    f.close()

fliename = 'poem.txt'
writeFile(fliename, poem)
readFile(fliename)