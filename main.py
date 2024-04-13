import random
import os


cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

numbers_of_cards=2

you_lose=r'''

                     _                
                    | |               
 _   _  ___  _   _  | | ___  ___  ___ 
| | | |/ _ \| | | | | |/ _ \/ __|/ _ \
| |_| | (_) | |_| | | | (_) \__ \  __/
 \__, |\___/ \__,_| |_|\___/|___/\___|
  __/ |                               
 |___/                                
'''

you_wim=r'''

                              _       
                             (_)      
 _   _  ___  _   _  __      ___ _ __  
| | | |/ _ \| | | | \ \ /\ / / | '_ \ 
| |_| | (_) | |_| |  \ V  V /| | | | |
 \__, |\___/ \__,_|   \_/\_/ |_|_| |_|
  __/ |                               
 |___/                                
'''

game_over=r'''

  ___   __   _  _  ____     __   _  _  ____  ____ 
 / __) / _\ ( \/ )(  __)   /  \ / )( \(  __)(  _ \
( (_ \/    \/ \/ \ ) _)   (  O )\ \/ / ) _)  )   /
 \___/\_/\_/\_)(_/(____)   \__/  \__/ (____)(__\_)
'''

draw=r'''

.------..------..------..------.
|D.--. ||R.--. ||A.--. ||W.--. |
| :/\: || :(): || (\/) || :/\: |
| (__) || ()() || :\/: || :\/: |
| '--'D|| '--'R|| '--'A|| '--'W|
`------'`------'`------'`------'
'''

card_dict={
11:r'''
 ┌─────────┐
 │ A       │
 │         │
 │         │
 │    A    │
 │         │
 │         │
 │       A │
 └─────────┘''',
    2:r'''
 ┌─────────┐
 │ 2       │
 │         │
 │         │
 │    2    │
 │         │
 │         │
 │       2 │
 └─────────┘''',
    3:r'''
 ┌─────────┐
 │3        │
 │         │
 │         │
 │    3    │
 │         │
 │         │
 │       3 │
 └─────────┘''',
    4:r'''
 ┌─────────┐
 │4        │
 │         │
 │         │
 │    4    │
 │         │
 │         │
 │       4 │
 └─────────┘''',
    5:r'''
 ┌─────────┐
 │5        │
 │         │
 │         │
 │    5    │
 │         │
 │         │
 │       5 │
 └─────────┘''',
    6:r'''
 ┌─────────┐
 │6        │
 │         │
 │         │
 │    6    │
 │         │
 │         │
 │       6 │
 └─────────┘''',
    7:r'''
 ┌─────────┐
 │7        │
 │         │
 │         │
 │    7    │
 │         │
 │         │
 │       7 │
 └─────────┘''',
    8:r'''
 ┌─────────┐
 │8        │
 │         │
 │         │
 │    8    │
 │         │
 │         │
 │       8 │
 └─────────┘''',
    9:r'''
 ┌─────────┐
 │9        │
 │         │
 │         │
 │    9    │
 │         │
 │         │
 │       9 │
 └─────────┘''',
    10:random.choice([r'''
 ┌─────────┐
 │10       │
 │         │
 │         │
 │    10   │
 │         │
 │         │
 │       10│
 └─────────┘''',
    r'''
 ┌─────────┐
 │K        │
 │         │
 │         │
 │    K    │
 │         │
 │         │
 │       K │
 └─────────┘''',
    r'''
 ┌─────────┐
 │Q        │
 │         │
 │         │
 │    Q    │
 │         │
 │         │
 │       Q │
 └─────────┘''',
    r'''
 ┌─────────┐
 │J        │
 │         │
 │         │
 │    J    │
 │         │
 │         │
 │       J │
 └─────────┘'''])
}
def print_crad(cards):
    card_str = []
    if type(cards)==int:
        print(card_dict[cards])
    else:
        # Get the number of rows in the ASCII art
        num_rows = len(card_dict[2].split('\n'))
        for i in range(num_rows):
            row = ''
            for x in cards:
                # Split the ASCII art of the card into lines
                lines = card_dict[x].split('\n')
                # Concatenate the corresponding row of each card
                row += lines[i] + '  '  # Add space between cards
            card_str.append(row)
        # Print the concatenated rows
        for row in card_str:
            print(row)
    return '\n'






print("Welcome to the blackjack game :::::::--------\n\n")

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def random_card():
    return random.choice(cards)

def computer_turn(cards):
    while sum(cards)<21:
        return random.choice(cards)

    return 0
def blackjack(user,computer):
    print(f"Your cards : {user}", print_crad(user))
    print(f"Computer's cards: {computer[0]}",print_crad(computer[0]))
    choice=input("Hit or deal type 'y' for deal and 'n' to hit !: ")
    if choice =='y':
        computer.append(computer_turn(cards=computer))
        if 11 in computer and sum(computer)>21:
            computer[computer.index(11)]=1
        elif 11 in user and sum(user)>21:
            user[user.index(11)]=1
        print(f"computer cards : {computer}",print_crad(computer),"\n")
        print(f"your cards : {user}", print_crad(user))
        if sum(user)>21:
            print(f"{you_lose}!")
        elif sum(computer)>21:
            print(f"{you_wim}!")
        elif sum(user)>sum(computer):
            print(f"{you_wim}!")
        elif sum(user)<sum(computer):
            print(f"{you_lose}!")
        else:
            print(f"{draw}!")
    elif choice =='n':
        user.append(random_card())
        if 11 in computer and sum(computer)>21:
            computer[computer.index(11)]=1
        elif 11 in user and sum(user)>21:
            user[user.index(11)]=1
        if sum(user) > 21:
            print(f"computer cards : {computer}", print_crad(computer), "\n")
            print(f"your cards : {user}", print_crad(user))
            print(f"{you_lose}!")
        else:
            blackjack(user,computer)
while True:
    print(r'''

__________.__                 __          __               __    
\______   \  | _____    ____ |  | __     |__|____    ____ |  | __
 |    |  _/  | \__  \ _/ ___\|  |/ /     |  \__  \ _/ ___\|  |/ /
 |    |   \  |__/ __ \\  \___|    <      |  |/ __ \\  \___|    < 
 |______  /____(____  /\___  >__|_ \ /\__|  (____  /\___  >__|_ \
        \/          \/     \/     \/ \______|    \/     \/     \/
''')
    blackjack(random.choices(cards, k=numbers_of_cards), random.choices(cards, k=numbers_of_cards))
    if input("You want to play again? press 'y' or 'n' : ") == 'y':
        clear_screen()
        continue
    else:
        clear_screen()
        print(f"{game_over}")
        break
