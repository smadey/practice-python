def powersum(power, **args):
    '''Return the sum of each argument rasied to specified power.'''
    total = 0
    for key, value in args.items():
        total += pow(value, power)
    return total

print(powersum(power = 2, num1 = 3, num2 = 4))

print(powersum(power = 2, num1 = 10))