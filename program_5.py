#Hot Dog Price Calculator Joseph Rydberg 9/16/24

def price_calculator(cost):
    cost = 0.0
    dogType = input("HotDog or ChiliDog")
    cheeseAnswer = input("Would you like cheese?")
    peppersAnswer = input("Would you like peppers?")
    oninonsAnswer = input("Would you like grilled onions")

    if dogType == "HotDog":
        cost += 3.5
    elif dogType == "ChiliDog":
        cost += 4.5

    if cheeseAnswer == "yes":
        cost += 0.5
    else:
        pass
    if peppersAnswer == "yes":
        cost += 0.75
    else:
        pass
    if oninonsAnswer == "yes":
        cost += 1.00
    else:
        pass

    cost = cost + (cost * 0.07)

    return cost

def sell_hotdog():
    cost = 0

    purchasedHotDog = price_calculator(cost)

    print("Your total is $" + str(purchasedHotDog))

sell_hotdog()