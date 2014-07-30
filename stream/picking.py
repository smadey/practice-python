import pickle

showlistfile = 'shoplist.data'

showlist = ['apple', 'mango', 'carrot']

f = open(showlistfile, 'wb')
pickle.dump(showlist, f)
f.close()

del showlist

f = open(showlistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)