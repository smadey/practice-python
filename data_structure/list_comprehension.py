listone = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listtwo = [ str(i * 10) + '%' for i in listone if i % 2 == 0]
print(listtwo)