name = input("Please type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ('left' / 'right') ").lower()

if answer == "left":
    q1 = input("You've come to a river, you can walk around it, or swim across it. Type 'walk' to walk around, or 'swim' to swim across. ").lower()
    
    if q1 == "swim":
        print("Oh no! You decided to try to swim across the river but were eaten by a huge alligator! You lose. ")
    elif q1 == "walk":
        print("You decided to try to walk around but you've been walking for miles and ran out of food and have died! You lose. ")
    else:
        print("Not a valid option. You lose. ")
    
    
    
elif answer == "right":
    q2 = input("You've come to a bridge, it looks very old and wobbly, do you want to cross it? ('cross' / 'go back') ").lower()
    
    if q2 == "cross":
        q3 = input("You've crossed the bridge successfully! There is a stranger on the other side, they are eager to speak to you, do you talk to them? ('yes' / 'no') ")
        
        if q3 == "yes":
            print("Because of your manners and curiosity, the starnger has given you many gold coins! You've won this adventure! ")
        elif q3 == "no":
            print("Because you ignored the stranger, they casted a spell onto you and you perish. You lose. ")
        else: 
            print("Not a valid option. You lose. ")
        
    elif q2 == "go back":
        print("You went back to the main road and get hit by a hippo. You lose. ")
    else:
        print("Not a valid option. You lose. ")
        
else: 
    print("Not a valid option. You lose. ")
