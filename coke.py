def coke():
    price = 50
    due = 0
    amount = 0
    valid_coins = [5, 10, 25]

    while True:
        coin = get_input()

        if coin in valid_coins:
            amount = amount + coin
            due = price - amount
            if due <= 0:
                change = amount - price
                print("Change Owed:",change)
                break
            else:
                print("Amount Due:",due)
                
        elif coin not in valid_coins:
            due = 50
            print("Amount Due:",due)
            continue

def get_input():
    coin = int(input("Insert Coin: "))
    return coin

coke()
