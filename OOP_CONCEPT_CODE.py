# from datetime import date

# class Student:
#     no_of_students = 0

#     def __init__(self, name, age, courses):
#         self.__name = name
#         self.__age = age
#         self.__courses = courses
#         Student.no_of_students += 1

#     def describe(self):
#         print(f"My name is {self.__name} and age is {self.__age}")

#     @classmethod
#     def create_veg(cls, name, birthyear):
#         age = date.today().year - birthyear
#         return cls(name, age, ['Vegetable Course'])

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients

#     @classmethod
#     def veg(cls):
#         return cls(['tomato', 'cheese'])
        
#     def __str__ (self):
#         return f"pizza ingredients are {self.ingredients}"

# pizza_1 = Pizza(['mato', 'kf'])
# pizza_2 = Pizza.veg()
# print(pizza_1,pizza_2)








                                     # # staticmethod

#   class Dates:
#     def __init__(self, date):
#         self.__date = date

#     def getDate(self):
#         return self.__date

#     @staticmethod
#     def toDashDate(date):
#         return date.replace("/", "-")


# date = Dates("15-12-2016")
# datefromDB = "15/12/2016"
# dateWithDb = Dates.toDashDate(datefromDB)
# if date.getDate() == dateWithDb:
#     print("equal")
# else:
#     print("not equal")



    
    
    # inhertaince &polymerphithm
    
    
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def display(self):
#         return f"Name is {self.name} and age is {self.age}"
    
# class Man(Person):
#     gender = 'male'
        
#     def __init__(self, name, age, voice):
#         super().__init__(name, age)
#         self.voice = voice
        
#     def display(self):
#         string = super().display()
#         return string + f", voice is {self.voice} and gender is {self.gender}"
        
# man = Man("Ahmed", 30, "hard")
# print(man.display())




# class Women(Person) :
#     gender = 'female'
    
#     def __init__(self, name, age, hair):
#         super().__init__(name, age)
#         self.hair = hair
        
#     def display(self):
#         string = super().display()
#         return string + f" hair is {self.hair} and gender is {self.gender}"
           
# women = Women("hean", 40, "red")
# print(women.display())


# print(isinstance(women,Women))




                      #  abstraction 
                
                
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     def __init__(self, name):
#         self.name = name
    
#     @abstractmethod
#     def start(self):
#         pass
    
#     @abstractmethod
#     def stop(self):
#         pass
    
# class Car(Vehicle):
#     def start(self):
#         print(f"{self.name} is starting the engine.")
    
#     def stop(self):
#         print(f"{self.name} is stopping the engine.")

# class Motorcycle(Vehicle):
#     def start(self):
#         print(f"{self.name} is starting the ignition.")
    
#     def stop(self):
#         print(f"{self.name} is turning off the ignition.")

# car = Car("Car 1")
# motorcycle = Motorcycle("Motorcycle 1")

# car.start()
# car.stop()

# motorcycle.start()
# motorcycle.stop()


                        #   __add__        over_ride
                        # less_than -> lt 
                        
class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __add__(self, other):
        names = self.name + " and " + other.name
        ages = str(self.age) + " and " + str(other.age)
        return f"Names: {names}, Ages: {ages}"
    
    def __lt__(self,other):                     # less_than -> lt  for compare  
        return self.age <other.age
        
    
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"
        
man = Man("Ahmed",500)
man1 = Man("John",40)

# print(man + man1) 
# print(man <man1)
 
 
#  you can see alot dunder function via write  print(dir(class_name))  

print (dir(Man))  

