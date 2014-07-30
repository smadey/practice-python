class ShortInputExpection(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = input('Enter something --> ')
    if len(s) < 3:
        raise ShortInputExpection(len(s), 3)
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputExpection as ex:
    print('ShortInputExpection: The input was {0} long, was excepting at least {1}'.format(ex.length, ex.atleast))
else:
    print('No exception war raised.')