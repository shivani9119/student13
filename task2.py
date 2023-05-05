class Dog:#Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")

dog1 = Dog("Buddy", 3)#Objects
dog2 = Dog("Max", 5)

print(dog1.name) #Attributes
print(dog2.name)

dog1.bark() #Methods

#Inheritance
class ServiceDog(Dog):
    def __init__(self, name, age,service):
        super().__init__(name, age)
        self.service = service
    def perform_service(self):
        print(f"{self.name} is performing {self.service} service.")

dog1 = ServiceDog("Buddy", 3, "bath")
dog2 = ServiceDog("Max", 5, "grooming")
print(dog2.service)

dog1.perform_service()

#Encapsulation
class Students:
   def __init__(self, name, rank):
      self.name = name
      self.rank = rank
   def demofunc(self):
      print("I am "+self.name)
      print("I got Rank ",+self.rank)

# 2 objects created
st1 = Students("shivani", 1)
st2 = Students("mango", 2)

# calling the functions using the objects created above
st1.demofunc()
st2.demofunc()


#Polymorphism
class cat:
    def make_sound(self):
        print("Meow!")
class Duck:
    def make_sound(self):
        print("Quack!")
def make_animal_sound(animal):
    animal.make_sound()
cat1 = cat()
duck1 = Duck()

make_animal_sound(cat1)
make_animal_sound(duck1)

#Exception Handling
try:
    x = 1/0
except ZeroDivisionError:
    print("Cannot divide by zero.")

a = input("enter data for string type:")

#Handling Multiple Exceptions
try:
    num = int(input("enter data for integer type:"))
    print(a+num)
except (TypeError, ValueError) as e:
    print(e)

#Handling Exceptions using finally block
try:
    k = 5 // 0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print('This is always executed')

#Loggings and Examination of Debug Logs
import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
def add(x,y):
    logging.info(f"Adding {x} and {y}")
    return x + y
def subtract(x,y):
    logging.info(f"Subtracting {x} and {y}")
    return x - y
def divide(x,y):
    logging.info(f"Dividing {x} and {y}")
    try:
        return x / y
    except ZeroDivisionError as ex:
        logging.error(f"Error occurres: {ex}")
        return None
x = 10
y = 0
c = add(x,y)
d = subtract(x,y)
e = divide(x,y)
logging.debug(f"c={c}, d={d}, e={e}")