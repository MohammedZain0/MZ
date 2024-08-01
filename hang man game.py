import random

hang_man = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




#اختيار كلمة عشوائيا
words = ["bad","orange","moon","shocelt", "sleep"]
random_words = random.choice(words)

#وضع خطوط في العبة
display = ["_"] * len(random_words)
print(" ".join(display))

#قائمة لتخزين الاحرف 
gussed_latters = []

attampet = 6

while "_" in display and attampet >0:
    
    gussed = input("Pleas Guess the letter:  ").lower()

    if gussed in gussed_latters:
        print("you alredy gessed that")
        print(f"you have {attampet} more tries")

        continue

    gussed_latters.append(gussed)

    if gussed not in random_words:
        attampet -=1
        print(hang_man[6-attampet])
    else:
        for position in range(len(random_words)):
            if random_words[position]==gussed:
                display[position]=gussed
    print(" ".join(display))
    print(f"you have {attampet} more tries")

if attampet == 0:
    print("""
          you lose
          """)
    print(hang_man[-1])
else:
    print("""
     you win
     """)