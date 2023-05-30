budget = float(input())
flour_price_1kg = float(input())

eggs_price = flour_price_1kg * 0.75
milk_price = flour_price_1kg + (flour_price_1kg * 0.25)
bread_cost = flour_price_1kg + eggs_price + (milk_price * 0.25)
bread_count = 0
coloured_eggs = 0


while budget > bread_cost:
    bread_count += 1

    budget -= bread_cost
    if budget < 0:
        break
    coloured_eggs += 3
    if bread_count % 3 == 0:
        eggs_lost = bread_count - 2
        coloured_eggs -= eggs_lost
        if coloured_eggs <= 0:
            break

print(f"You made {bread_count} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f} BGN left.")


