lines_number = int(input())

tank_capacity = 255
total_water = 0
for liters in range(lines_number):
    poured_water = int(input())
    if tank_capacity - poured_water < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= poured_water
    total_water += poured_water

print(total_water)


