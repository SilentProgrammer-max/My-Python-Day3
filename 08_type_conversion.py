x = 3
y = 3.3 
z = ("hello world ")

print(type(x))
print(type(z))
print(type(3.3))

# implicit conversion 
x = y//10
print(x)
print(type(x))

x = x* 10
print(type(x))
print(x)

# explicit conversion

age = input("what's your age ? ")
age=int(age)
print(type(age))

#name 
name = input("what's your name ? ")
print(name, type(name))
name = int(name) 
print(type(name)) 