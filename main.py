import random
#####opems home page
f = open("homescreen.txt")
print(f.read())

#sign in
UserandPass = {                     #lkist of accounts
    "LB16": "1234",
    "q": "q",
    "IH7": "abcd",
    "Kysan": "ilikemen",
    "Albert": "ILikeCakes"
}

# Player 1 login###############

user1 = input("Enter player1 username: ")
password1 = input("Enter your password: ")   # ENTERUSER
if user1 in UserandPass and UserandPass[user1] == password1:
    print(f"Welcome {user1}!")
else:
    print("Wrong username or password.")
    bb = 3
    while bb == 3:
        print("Wrong username idiot")
    exit()
print()

# Player 2 login###############
user2 = input("Enter player2 username: ")
password2 = input("Enter your password: ")

if user2 in UserandPass and UserandPass[user2] == password2:
    print(f"Welcome {user2}!")           #skips code if right
else:
    print("Wrong username or password.")
    bb=3
    while bb == 3:
        print("Wrong username idiot")
    exit()
#deck building##########
deck = []
colours = ["red", "black", "yellow"] #allpossiblecolours

for colour in colours:
    for num in range(1, 11):  # 1–10       #buildsdeck
        deck.append((colour, num))    #gives it number and colour

random.shuffle(deck)           #shuffle sit as in prder
#RULEZ###########
Rules = {
    ("red", "black"): "red",
    ("black", "yellow"): "black",
    ("yellow", "red"): "yellow"
}


#variables###############
player1_pile = []
player2_pile = []
Hack = 0
v = 10
#gameloop
print()
input("𝗲𝗻𝘁𝗲𝗿 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝘁𝗼 𝘀𝘁𝗮𝗿𝘁")
print()
while len(deck) >= 2:           #so it ends
    player1_card = deck.pop(0)         #takes top card
    player2_card = deck.pop(0)
                                 #pops and gives cards
    colour1, num1 = player1_card
    colour2, num2 = player2_card

    print(f"\n{user1} got {colour1} {num1}")
    print(f"{user2} got {colour2} {num2}")

    # Same colour orrr highest number wins
    if colour1 == colour2:
        if num1 > num2:
            print(f"{user1} wins the round")
            player1_pile.extend([player1_card, player2_card])
        else:
            print(f"{user2} wins the round")
            player2_pile.extend([player1_card, player2_card])

    # Different colours use rulez
    elif (colour1, colour2) in Rules and Rules[(colour1, colour2)] == colour1:
        print(f"{user1} wins the round")
        player1_pile.extend([player1_card, player2_card])
    else:
        print(f"{user2} wins the round")
        player2_pile.extend([player1_card, player2_card])

    hack = input("Press Enter for next round...")#hacks ssshhhhh
    if hack == "OpenHacks":          #figres out whatcommand
       f = open("hackclient.txt")
       print(f.read())
    elif hack == "SetWinner":
        realwin = input("enter ur winner")
        Hack = 1
    elif hack == "SeeCards":
        print(f"{user1} has {player1_pile} and {user2} has {player2_pile}")
    elif hack == "SkillIssue":
        f = open("skillissue.txt")
        print(f.read())
    elif hack == "Crashout":
        crashuser = input("enter username")
        while v > 1:
            print(f"{crashuser} won frick you")
            print(f"{crashuser} is better then u")     
            print(f"{crashuser} knows ur dumb")
    else:
        print("")
#main winner
print("\n--- GAME OVER ---")

if Hack == 1: #setwinneer or be normal
    winner = realwin
elif len(player1_pile) > len(player2_pile):
    winner = user1
    winning_cards = player1_pile
    loser = user2                       #sll possible
else:
    winner = user2
    winning_cards = player2_pile
    loser = user1

print(f"Winner is {winner}")                          #prints winners name
print(f"Total cards: {len(winning_cards)}")
print("Winning cards:")

for card in winning_cards:
    print(card) 
print(f"and {loser} lost L Bozo")
print("")
wait = input("Press anything to continue.")
print("")
inp = input("enter yes to see leaderboard! and L to see loserboard!")
if inp == "yes":
    f = open("winners.txt")  #displays leaderboard
    print(f.read())
    f = open("line.txt")
    print(f.read())
elif inp == "L":
    f = open("losers.txt")
    print(f.read())
    f = open("line.txt")
    print(f.read())
else:
    print()
down = input("Just enter Download for FRee Robux!!!!!")

#saves the winner to winners.txt
with open("winners.txt", "a") as file:
    file.write(f"{winner} with {len(winning_cards)}\n")
with open("losers.txt", "a") as file:
    file.write(f"{loser} lost agienst {winner}\n")


#makes it save top 5 scroes
scores = {}

with open("winners.txt", "r") as file:
    for line in file:
        name, score = line.strip().split(",")
        score = int(score)

        if name not in scores or score > scores[name]:
            scores[name] = score

top5 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 players:")                  #DISPOLAYS IT
for name, score in top5:
    print(name, score)
