# Hello world!
print("Hello, world!")

# define a number and string variables
num = 1
string = "Hello, "

# print the string and number variables
print(string + str(num) + "!")
# Will print "Hello, 1!"

# get input from user and convert to integer
number = int(input())

# if number is even, print "Even!"
if number % 2 == 0:
  print("Even!")
# otherwise, print "Odd"
else:
  print("Odd")


# define a list
li = [1, 2, 3]

# print each element in the list plus 1
for element in li:
  print(element + 1)
