number_of_persons = int(input())
lift_capacity = int(input())

trips = number_of_persons // lift_capacity
if number_of_persons % lift_capacity != 0:
    trips += 1

print(trips)