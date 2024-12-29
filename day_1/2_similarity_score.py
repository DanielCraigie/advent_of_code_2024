import csv

list_one = []
list_two = []

# read incoming data into two arrays
with open('input.csv') as input_file:
    file_reader = csv.reader(input_file)
    for row in file_reader:
        list_one.append(row[0])
        list_two.append(row[1])

def num_matches(needle, haystack):
    """Returns number of matches of needle in the haystack"""
    matches = 0
    for i in range(len(haystack)):
        if haystack[i] == needle:
            matches += 1
    return matches

similarity_score = 0
matches_cache = {} # local cache to save having to repeat num_matches() loop

for i in range(len(list_one)):
    if list_one[i] in list_two:
        if list_one[i] in matches_cache:
            matches_count = matches_cache[list_one[i]]
        else:
            matches_count = num_matches(list_one[i], list_two)
            matches_cache[list_one[i]] = matches_count

        similarity_score += int(list_one[i]) * matches_count

print(similarity_score)
