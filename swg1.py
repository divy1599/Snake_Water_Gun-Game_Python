import random

user=input("Enter your choice: ")

computer= random.choice([-1,0,1])

yourstr={
    "s":-1,"w":0,"g":1
}
revdict={
    -1:"Snake",0:"Water",1:"Gun"
}
you=yourstr[user]
print(f"Your choice: {revdict[you]} and computer choice: {revdict[computer]}")

if(you==computer):
    