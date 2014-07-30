def make_repeater(n):
    return lambda s: s * n

twice = make_repeater(2)

print(twice('Word'))
print(twice(5))

exec_print = exec('print("Hello World!")')
eval_print = eval('print("Hello World!")')
assert exec_print == eval_print

exec_calc = eval('2 * 3')
eval_calc = exec('2 * 3')
assert exec_calc != eval_calc

i = []
i.append('item')

print(repr(i))