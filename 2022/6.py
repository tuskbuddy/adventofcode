with open("6_data.txt", "r") as fo:
    buffer = fo.read().strip()

chunk_length = 4   # Part 1
chunk_length = 14  # Part 2
chunk_start = 0
chunk_end = chunk_start + chunk_length

for ii in range(chunk_start, len(buffer) - chunk_length):
    chunk = buffer[ii+chunk_start:ii+chunk_end]
    if len(set(chunk)) == chunk_length:
        break

print(chunk_end+ii)
