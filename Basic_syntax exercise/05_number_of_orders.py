orders = int(input())
total_order = 0
final_total = 0

for orders in range(orders):
    capsule_price = float(input())
    days_number = int(input())
    capsules_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue

    elif days_number < 1 or days_number > 31:
        continue

    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    total_order = capsule_price * days_number * capsules_per_day
    final_total += total_order
    print(f"The price for the coffee is: ${total_order:.2f} ")
print(f"Total: ${final_total:.2f}")





