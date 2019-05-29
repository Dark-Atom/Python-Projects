def game():
    a1=input("%s,what you want to choose(rock,scissors,paper):"%a)
    b1=input("%s,what you want to choose(rock,scissors,paper):"%b)
    if a1=='rock' and b1=='rock':
        print("match was tai!!")
    elif a1=='rock' and b1=='paper':
        print("%s, win!"%b)
    elif a1=="rock" and b1=="scissors":
        print("%s, win!"%a)
    elif a1=="paper" and b1=="paper":
        print("match tai!")
    elif a1=="paper" and b1=="rock":
        print("%s,win!"%a)
    elif a1=="paper" and b1=="scissors":
        print("%s,Win!"%b)
    elif a1=="scissors" and b1=="scissors":
        print("mach tai!")
    elif a1=="scissors" and b1=="paper":
        print("%s,Win!"%a)
    elif a1=="scissors" and b1=="rock":
        print("%s,Win!"%b)
    else:
        print("please, enter valid output")
    print("You want to continue this game?(Y/N)")
 

a=input("Enter your name:")
b=input("Enter your name:")
game()
c=input()
while c[0]=="y" or c[0]=="Y":
    game()
    c=input()
input()
    
    
    

