#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int"
# .#To'rt xonali butun son berilgan. Undagi juft raqamlar sonini toping.

#"var_int" o'zgaruvchisini yarating va unga to'rt xonali butun son qiymatini belgilang.

#"var_int" o'zgaruvchisidagi juft raqamlar sonini chop eting.
var_int=1397
x = var_int

x4 = x % 10
x = x // 10

x3 = x % 10
x = x // 10

x2 = x % 10
x = x // 10

x1 = x % 10
x = x // 10

print((x1+1)%2 + (x2+1)%2 + (x3+1)%2 + (x4+1)%2)