import random

again = True

while again:
    print(random.randint(1,6))
    another_roll=input("Roll Adain? (y/n)" )
    if another_roll.lower()=="y":
        continue
    else:
        break
