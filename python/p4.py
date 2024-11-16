import random

deneme = []
turns = 12
i=0

name = input("What is your name? ")
print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
kelimeler=list(word)




while i<=turns :
    print(word)
    deneme=input("kenemek istediğiniz harfi yazın")
    for char in word:
        if char in deneme:
            print(deneme)

        else:
            print("boş")    

    