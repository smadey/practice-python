def sayHi():
    print('Hi, this is mymodule speaking.')

version = '0.1'

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')