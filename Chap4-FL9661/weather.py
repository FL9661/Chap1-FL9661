#Monthly Temp Table

temps = [[0.0 for h in range(24)] for d in range(31)]
days = 0
h = 0

for i in temps:
    print (days, i)
    days = days +1

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)