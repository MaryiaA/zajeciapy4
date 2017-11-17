# 6. blackjack - na inpucie wejście 2 karty
#   wartości: 2-9, J Q K = 10, A = 1 lub 11
#   określ ruch jaki powinien być wykonany:
#   jeszcze jedna karta, stop,


karta1 = input("Give card 1")
karta2 = input("give card 2")


karta1 = int(karta1)
karta2 = int(karta2)


#if karta1 == "K":
    #karta1 = 10
    #return karta1

total_points = karta1 + karta2
if total_points == 21:
    print("You win")
    quit()

while total_points  < 21:
    request_next_card = input("take one morecard? (Type Yes or No)")
    if request_next_card == "Yes":
        next_card = input("Your next card")
        next_card = int(next_card)
        total_points = total_points + next_card
    elif request_next_card == "No":
         print(f"You stay with {total_points} points")
         quit()
    elif request_next_card != "Yes" or request_next_card != "No":
        print("Invalid syntax.try again")
print(f"Too bad. You have {total_points} points")

