from polymorphism_and_abstraction_06.exe.animals.project.cat import Cat
from polymorphism_and_abstraction_06.exe.animals.project.dog import Dog
from polymorphism_and_abstraction_06.exe.animals.project.kitten import Kitten
from polymorphism_and_abstraction_06.exe.animals.project.tomcat import Tomcat

dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)


kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)
