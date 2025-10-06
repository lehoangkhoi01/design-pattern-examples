# What is it ?
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

# Problem
1. We may create many instances of a class, which is not necessary
2. We may overwrite global "access point" unexpectedly

**=> Use singleton**

# Solution
Implements:

1. Make default constructor private -> prevent other objects create new instance using 'new' keyword
2. Create static creation method as 'constructor'. This method calls the private constructor to create an object and saves it. All following calls to this method return the cached object.

**=> So whenever that method is called, the same object is always returned.**




