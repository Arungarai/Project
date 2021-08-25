import random
response='Y'
number = [1,2,3,4,5,6]
def shuffle1(number):
    print(random.choice(number))
while (response=='Y'):
    shuffle1(number)
    response = input("Do you want to continue? Y/N")
else:
    quit()


