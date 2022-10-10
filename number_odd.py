#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
var_int=4567
x=var_int


x4 = x % 10
x = x // 10

x3 = x % 10
x = x // 10

x2 = x % 10
x = x // 10

x1 = x % 10
x = x // 10
print((x1)%2+(x2)%2+(x3)%2+(x4)%2)