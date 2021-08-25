import random
words = ["cat","dog","rabbit","horse","pig","rat","mat","good","goon"]
#words=["good","goon"]
random_word=random.choice(words)
length_random= len(random_word)
count=1
#print("The random word is" + " " + random_word)
while count<=5:
    pos = 0
    user_input = input("Please guess the words from the following"+str(words))
    length_user = len(user_input)
    if user_input == random_word:
        print("The random word is" + " " + random_word)
        print("Your guess is right and the word is"+" "+user_input)
        quit()
    else:
        min_length=min(length_random,length_user)
        for item in range(min_length-1):
            if (random_word[item] == user_input[item]):
                print("Position {} is correct".format(item))
                pos=pos+1
        if pos==0:
            print("No characters are in correct position")
    count=count+1
if count==6:
    print("Sorry! You didn't guess the word right")



