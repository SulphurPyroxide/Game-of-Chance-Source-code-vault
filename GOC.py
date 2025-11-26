import random
#setting a class for a weapon, including attributes and a function for the chance of a critical hit
class Item_SolarGreatSword:
    def   __init__(self,Damage,SwingSpeed,StaminaUsage,CritChance):
        self.Damage = Damage
        self.SwingSpeed = SwingSpeed
        self.StaminaUsage = StaminaUsage
        self.CritChance = CritChance
    def CritCheck(self):
        if self.CritChance == 5:
            self.Damage *= 3
            
        
#setting variables
SolarGreatSword = Item_SolarGreatSword(random.randint(55,65),2,25,random.randint(1,5))
Enemy_health = 150
EnemyStatusAlive = True
EscapeChance = random.randint(1,2)
#defining functions
def Function_EnemyDeathCheck():
    global EnemyStatusAlive
    if Enemy_health <= 0:
        EnemyStatusAlive = False
def Function_EscapeCheck():
    print("You...")
    if EscapeChance == 2:
        print("Got Away!!!")
    else:
        print("Failed to escape! Your head comes clean off from a spell!!!")



    

print("The goblin king approaches you with a devious smirk...")
while True:
    Player_Choice = input("What will you do?").lower()
    if Player_Choice in ["fight","run"]:
        break
    else:
        print("Nice try, you may only fight or try to run")

#Checks for player input to determine what they do, inputting anything other than fight or run should cause an error
if Player_Choice == "fight":
    print("you decided to Fight!")
    #coin flip mechanic to add chance into the mix
    while EnemyStatusAlive:
        Coin_guess = input("Heads or tails?").capitalize()
        for i in range(1):
           Coinflip = random.choice(["Heads","Tails"])
           print(Coinflip)
        #If the coin flip succeeds you attack the enemy successfully, the only way to defeat them is rolling into a critical hit

        if Coin_guess == Coinflip:
             SolarGreatSword.CritCheck()
             Enemy_health -= SolarGreatSword.Damage
             print(Enemy_health)
             Function_EnemyDeathCheck()
      #checks if the enemy is dead
             if not EnemyStatusAlive:
                 print("The goblin king has been slain!")
                 break
             else:
                 continue
        else:
           print("The goblin king Casts a spell... your head comes clean off!")
           break
#if the player chooses to run, it will run a check that has a 50% chance to succeed if it fails, you die
elif Player_Choice == "run":
    Function_EscapeCheck()

endmessage = input("end of program")