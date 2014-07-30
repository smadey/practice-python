zoo = ('wolf', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'dolphin', zoo)
print('Number of animals in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[len(new_zoo) - 1])
print('Last animal brought from old zoo is %s' % new_zoo[len(new_zoo) - 1][len(zoo) - 1])