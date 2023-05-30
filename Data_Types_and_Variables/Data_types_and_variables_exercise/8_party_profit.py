from math import ceil, floor
group_size = int(input())
adventure_days = int(input())

total_coins = 0

for days in range(1, adventure_days + 1):
    if days % 10 == 0:
        group_size -= 2
    if days % 15 == 0:
        group_size += 5
    if days % 3 == 0:
        total_coins -= 3 * group_size
    if days % 5 == 0:
        total_coins += 20 * group_size
        if days % 3 == 0:
            total_coins -= 2 * group_size

    total_coins += 50
    total_coins -= 2 * group_size
total_coins = floor(total_coins)
print(f"{group_size} companions received {total_coins // group_size} coins each.")
