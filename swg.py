#snake water gun game 
#s & w : s
# w & g : w
# g & s : g
import random

user=input("Enter your choice:")
comp_choice=random.choice([-1,0,1])
your_dict={"s":-1,"w":0,"g":1}
you=your_dict[user]
rev_dict={-1:"Snake",0:"Water",1:"Gun"}
print(f"You have choosen {rev_dict[you]} computer has choosen {rev_dict[comp_choice]}")
if(comp_choice==you):
    print("Match draws")
elif(comp_choice==-1 and you==0):
    print("computer wins")
elif(comp_choice==-1 and you==1):
    print("you wins")
elif(comp_choice==1 and you==0):
    print("you wins")
elif(comp_choice==1 and you==-1):
    print("computer wins")
elif(comp_choice==0 and you==-1):
    print("you wins")
elif(comp_choice==0 and you==1):
    print("computer wins")