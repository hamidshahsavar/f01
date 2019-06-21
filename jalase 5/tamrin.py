#def is_triangle(a, b, c)
   # a < b+c and b < a+c and c < a+b
    #is_triangle(3, 4, 5)

def is_triangle(a, b, c):

   if a < b+c and b < a+c and c < a+b:
       return True
   return False

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

print(is_triangle(a, b, c))










