import mymodule

mymodule.sayHi()

print('Version', mymodule.version)

from mymodule import sayHi, version

sayHi()

print('Version', version)