budget = int(input())
total_spend = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break
    price = int(command)
    if total_spend + price > budget:
        print("You went in overdraft!")
        break
    total_spend += price




