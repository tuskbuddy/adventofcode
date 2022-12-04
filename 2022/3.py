import string

priority_index = string.ascii_letters

with open("3_data.txt", "r", encoding="utf-8") as fo:
    rucksack = fo.read().splitlines()

# Part 1
priority_sum = 0
for contents in rucksack:

    split_index = int(len(contents) / 2)
    str_1, str_2 = contents[:split_index], contents[split_index:]
    common_item = set(str_1).intersection(set(str_2)).pop()
    priority = priority_index.find(common_item) + 1
    priority_sum += priority

print(priority_sum)

# Part 2
priority_sum = 0
group_rucksacks = zip(rucksack[0::3], rucksack[1::3], rucksack[2::3])
for rucksack_1, rucksack_2, rucksack_3 in group_rucksacks:

    common_item = set(rucksack_1).intersection(set(rucksack_2), set(rucksack_3)).pop()
    priority = priority_index.find(common_item) + 1
    priority_sum += priority

print(priority_sum)
