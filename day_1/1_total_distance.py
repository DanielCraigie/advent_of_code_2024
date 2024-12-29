import csv

listOne = []
listTwo = []

# read incoming data into two arrays to compare
with open('input.csv') as input:
    reader = csv.reader(input)
    for row in reader:
        listOne.append(row[0])
        listTwo.append(row[1])

# ensure both lists are the same length
if len(listOne) != len(listTwo):
    raise Exception("List lengths do not match")

# sort both lists in ascending numerical order
listOne.sort()
listTwo.sort()

total_distance = 0

for i in range(len(listOne)):
    # sum numeric difference of each pair
    total_distance += abs(int(listOne[i]) - int(listTwo[i]))

print(total_distance)
