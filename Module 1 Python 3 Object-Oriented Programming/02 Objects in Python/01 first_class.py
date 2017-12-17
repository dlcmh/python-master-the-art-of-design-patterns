# python -i 01\ first_class.py
# -i - run the code and then drop into the interactive interpreter

class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

print(a) # => <__main__.MyFirstClass object at 0x10bf233c8>
print(b) # => <__main__.MyFirstClass object at 0x10bf23470>
