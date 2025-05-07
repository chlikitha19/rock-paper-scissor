import random
yourscore = 0
computerscore = 0
option = ["rock","paper","scissors"]
while True:
    youroption= input("what is your option:")
    
    if youroption in option:
        print(f" your selected option is :{youroption}")
        computeroption=random.choice(option)
        print(f"computer selected option is :{computeroption}")
        if youroption == computeroption:
            print("tie")
           
            
            
        elif((youroption == "rock" and computeroption == "scissors") or
             (youroption == "paper" and computeroption == "rock") or
             (youroption == "scissors" and computeroption == "paper")):
            print("you win")
            yourscore = yourscore +1
           
            
        else:
            print("computer win")
            computerscore = computerscore+1
        print(f"your score is {yourscore}")
        print(f"computerscore is {computerscore}")  
        
        
    else:
        print("you didn't selected the correct option ")
        print("YOUR GAME IS ENDED")
        break
if yourscore > computerscore:
        print("YOU WON THE MATCH")
else:
        print("COMPUTER WON THE MATCH")
