#snake water gun
import random
comp=["S", "W", "G"]
i=1
comp_sc=0
my_sc=0
while(i<=10):    
    comp_ch =  random.choice(comp)
    my_ch=input("S for snake, W for water, G for gun: ")
    ch2= my_ch.capitalize()
    if comp_ch==ch2:
        print(f"You Choose: {ch2} Computer Choose: {comp_ch}")
        print(f"Try, {i}, Draw")
    elif comp_ch=="W" and ch2=="S":
        print(f"You Choose: {ch2} Computer Choose: {comp_ch}")
        print(f"Try {i}: You Won")
        my_sc+=1
    elif comp_ch=="G" and ch2=="W":
        print(f"You Choose: {ch2} Computer Choose: {comp_ch}")
        print(f"Try {i}: You Won")
        my_sc+=1
    elif comp_ch=="S" and ch2=="G":
        print(f"You Choose: {ch2} Computer Choose: {comp_ch}")
        print(f"Try {i}: You Won")
        my_sc+=1
    else:
        print(f"You Choose: {ch2} Computer Choose: {comp_ch}")
        print("Try {i}: Computer Won")
        comp_sc+=1
    print(f"\n{10-i}, try left")  
    i+=1
print(f"Your Point:{my_sc}\nComputer Point:{comp_sc}")
if my_sc>comp_sc:
    print("You won the game")
elif my_sc==comp_sc:
    print("Draw game")
else:
    print("Computer won the game")
    print("Better Luck Next Time...")
