"""
Write a method which can calculate square value of number
"""
class Square():
    def sq_num(self,number):
        print(number ** 2)
        
number = int(input("A number: "))
calc = Square()
calc.sq_num(number) 
