from functools import reduce

with open("4_data.txt", "r", encoding="utf-8") as fo:
    assignment_pair_list = fo.read().splitlines()

# Part 1
fully_contained_count = 0
for assignment_pairs in assignment_pair_list:

    assignments = assignment_pairs.split(",")
    sections = {}
    for assignment in assignments:
        begin, end = assignment.split("-")
        sections[assignment] = set(range(int(begin), int(end) + 1))

    # Find the intersection of this pair of assignments
    overlap = reduce(set.intersection, sections.values())
    if overlap in sections.values():
        fully_contained_count += 1

print(fully_contained_count)

# Part 2
partly_contained_count = 0
for assignment_pairs in assignment_pair_list:

    assignments = assignment_pairs.split(",")
    sections = {}
    for assignment in assignments:
        begin, end = assignment.split("-")
        sections[assignment] = set(range(int(begin), int(end) + 1))

    overlap = reduce(set.intersection, sections.values())
    if overlap:
        partly_contained_count += 1

print(partly_contained_count)
