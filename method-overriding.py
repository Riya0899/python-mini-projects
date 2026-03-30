#--------ABSTRACTION--------------
from abc import ABC, abstractmethod

class Vehicle(ABC): # Inherits from ABC to become an abstract class
    @abstractmethod
    def drive(self): # Abstract method with no implementation
        pass

    @abstractmethod
    def stop(self): # Another abstract method
        pass
    
    def refuel(self): # Concrete method (has implementation)
        print("Refueling the vehicle.")

class Car(Vehicle): # Concrete class must implement abstract methods
    def drive(self):
        print("Car is driving.")
        
    def stop(self):
        print("Car has stopped.")

# Attempting to instantiate the abstract class raises a TypeError
# vehicle = Vehicle() 

# Instantiate the concrete subclass
my_car = Car()
my_car.drive()
my_car.refuel() # Can use concrete methods from the abstract base class

# ---- 1 ---

class Vehicle(ABC):
    @abstractmethod
    def __init__(self,distance,capacity):
        self.distance=distance
        self.capacity=capacity
    def fuel_efficiency(self):
        pass
class Car(Vehicle):
    def __init__(self, distance, capacity):
        super().__init__(distance, capacity)
    def fuel_efficiency(self):
        return f"fuel efficiency of car is {self.distance/self.capacity}"
class Bike(Vehicle):
    def __init__(self, distance, capacity):
        super().__init__(distance, capacity)
    def fuel_efficiency(self):
        return f"fuel efficiency of bike is {self.distance/self.capacity}"
class Truck(Vehicle):
    def __init__(self, distance, capacity):
        super().__init__(distance, capacity)
    def fuel_efficiency(self):
        return f"fuel efficiency of truck is {self.distance/self.capacity}"
    
carr=Car(2300,677)
bikee=Bike(1200,67)
truckk=Truck(3400,987)

print(carr.fuel_efficiency())
print(bikee.fuel_efficiency())
print(truckk.fuel_efficiency())


# ---2---

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class C_card(Payment):
    def pay(self,amount):
        print(f"amount {amount} is paid using credit card")

class D_card(Payment):
    def pay(self,amount):
        print(f"amount {amount} is paid using debit card")
        
class UPI(Payment):
    def pay(self,amount):
        print(f"amount {amount} is paid using UPI")
credit=C_card()
debit=D_card()
upi=UPI()

credit.pay(34000)
debit.pay(34000)
upi.pay(34000)

# --- 3 ---

class Shape(ABC):
        
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return f"Area of circle is {3.14*self.radius*self.radius}"
class Rect(Shape):
    def __init__(self, l, b):
        self.l=l
        self.b=b
    def area(self):
        return f"Area of rectangle is {self.l*self.b}"
class triangle(Shape):
    def __init__(self,l):
        self.l=l
    def area(self):
        return f"Area of triangle is {0.43*self.l*self.l}"

c=Circle(32)
r=Rect(12,45)
t=triangle(32)

print(c.area())
print(r.area())
print(t.area())

# --- 4 ---
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Full_time(Employee):
    def __init__(self,salary):
        self.salary=salary
    def calculate_salary(self):
        print(f"salary for full time employee is {self.salary}")
class Part_time(Employee):
    def __init__(self,hours,salary):
        self.salary=salary
        self.hours=hours
    def calculate_salary(self):
        print(f"salary for part time employee is {self.hours*self.salary}")
f=Full_time(34000)
p=Part_time(6,460)

f.calculate_salary()
p.calculate_salary()
        
# --- 5 ---

class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass
class SBI(Bank):
    def interest_rate(self):
        print("interest rate of SBI is 6%")
class HDFC(Bank):
    def interest_rate(self):
        print("interest rate of HDFC is 6.5%")
class ICICI(Bank):
    def interest_rate(self):
        print("interest rate of ICICI is 7%")
s=SBI()
h=HDFC()
i=ICICI()

s.interest_rate()
h.interest_rate()
i.interest_rate()

# --- 6 ---
class Course(ABC):
    @abstractmethod
    def start_course(self):
        pass
class Video_course(Course):
    def start_course(self):
        print("this type offers course in video format")
class Text_course(Course):
    def start_course(self):
        print("this type offers course in text format")
class Live_course(Course):
    def start_course(self):
        print("this type offers live classes")

v=Video_course()
t=Text_course()
l=Live_course()

v.start_course()
t.start_course()
l.start_course()

# --- 7 ---

class Notification(ABC):
    @abstractmethod
    def send_msgs(self):
        pass
class Email_N(Notification):
    def send_msgs(self):
        print("notifications send via email")
class SMS_N(Notification):
    def send_msgs(self):
        print("notifications send via SMS")
class Push_N(Notification):
    def send_msgs(self):
        print("notifications send via push notification")

e=Email_N()
s=SMS_N()
p=Push_N()

e.send_msgs()
s.send_msgs()
p.send_msgs()

# ---8---

class Delievery(ABC):
    @abstractmethod
    def delievery_charges(self,distance):
        pass
class Bike_D(Delievery):
    def delievery_charges(self,distance):
        print(f"delievery charges for bike is {200*distance}")
class Car_D(Delievery):
    def delievery_charges(self,distance):
        print(f"delievery charges for car is {200*distance}")
b=Bike_D()
c=Car_D()

b.delievery_charges(239)
c.delievery_charges(100)
