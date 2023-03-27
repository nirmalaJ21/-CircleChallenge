import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def calculate_diameter(self):
        dia = 2 * self.radius
        return dia
    def calculate_circumference(self):
        circum = 2 * math.pi  * self.radius
        return circum
    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return(area)
    def grow(self):
        self.radius = self.radius + 1
        # return(self.radius )
    def get_radius(self):
        return(self.radius)

print('Welcome to the Circle Tester')
while True:
    try:
         user_input = float(input('Please enter a  radius'))
         if(user_input > 0):  #Check for postive number else ask to re-enter
          break
    except ValueError:
         print("Invalid input. Please enter a valid  number.")

circle1 = Circle(user_input)
while True:
    print('Diameter',circle1.calculate_diameter())
    print('Circumference',circle1.calculate_circumference())
    print('Area',circle1.calculate_area())
    print('Would you like your circle to grow?(y/n)')
    choice =input()
    if choice =='y':
        circle1.grow()
        circle1.get_radius()
        continue
    elif choice == 'n':
        print('Goodbye')
        break
    else:
        print('Please enter correct choice')
        continue


#######
# import math
#
#
# class Validator:
#     @staticmethod
#     def is_positive_number(num):
#         try:
#             return float(num) > 0
#         except ValueError:
#             return False
#
#     @staticmethod
#     def is_float(num):
#         try:
#             float(num)
#             return True
#         except ValueError:
#             return False
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_diameter(self):
#         dia = 2 * self.radius
#         return (dia)
#
#     def calculate_circumference(self):
#         circum = 2 * math.pi * self.radius
#         return (circum)
#
#     def calculate_area(self):
#         area = area = math.pi * (self.radius ** 2)
#         return (area)
#
#     def grow(self):
#         self.radius = self.radius + 1
#         return (self.radius)
#
#     def get_radius(self):
#         return (self.radius)
#
#
# print('Welcome to the Circle Tester')
# while True:
#     user_input = input('Please enter a radius: ')
#     if Validator.is_float(user_input) and Validator.is_positive_number(user_input):
#         circle1 = Circle(float(user_input))
#         break
#     else:
#         print("Invalid input. Please enter a positive number.")
#
# while True:
#     print('Diameter', circle1.calculate_diameter())
#     print('Circumference', circle1.calculate_circumference())
#     print('Area', circle1.calculate_area())
#     print('Would you like your circle to grow?(y/n)')
#     choice = input()
#     if choice == 'y':
#         circle1.grow()
#         circle1.get_radius()
#         continue
#     elif choice == 'n':
#         print('Goodbye')
#         break
#     else:
#         print('Please enter correct choice')
#         continue

