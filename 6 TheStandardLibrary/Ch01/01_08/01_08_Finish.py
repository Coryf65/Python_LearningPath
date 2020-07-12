# type()
# class type(o: object)
# type(object_or_name, bases, dict) type(object) -> the object's type type(name, bases, dict) -> a new type

# isinstance()
# Return whether an object is an instance of a class or of a subclass thereof.
# A tuple, as in isinstance(x, (A, B, ...)), may be given as the target to check against. This is equivalent to isinstance(x, A) or isinstance(x, B) or ... etc.

r = range(0, 30)
print(type(r))
print(type(10))
print(type('a'))
print(type("Hi there"))

class Car:
    pass

class Truck():
    pass

class Pickup(Car):
    pass

c = Car()
convert = Car()
t = Truck()
p = Pickup()
print(type(c))
print(type(t))
print(type(c) == type(t)) # type does not look into inheritence
print(type(c) == type(convert)) # these are both direct instances

print(isinstance(c, Car))
print(isinstance(p, Car)) # isinstance, Accounts for Inheritance! they are equal here
print(isinstance(t, Car))


# if the number is in range it will print
if isinstance(r, range):
    print(list(r))