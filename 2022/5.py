indices = {
    "how_many": 1,
    "from": 3,
    "to": 5,
}


def build_proc(commands):

    keys = ["how_many", "from", "to"]
    proc = {key: [] for key in keys}
    for command in commands:
        words = command.split(" ")
        for key in ("how_many", "from", "to"):
            # Subtract one if key is location-based to account for zero-indexing
            instruction = (
                int(words[indices[key]]) - 1 if key != "how_many"
                else int(words[indices[key]])
            )
            proc[key].append(instruction)

    return proc


def execute_proc(stacks, commands, proc, part):

    if part == 1:
        for ii, _ in enumerate(commands):
            how_many = proc['how_many'][ii]
            from_, to = proc['from'][ii], proc['to'][ii]
            pickup_stack = [stacks[from_].pop() for _ in range(how_many)]
            stacks[to] += pickup_stack
    else:
        for ii, _ in enumerate(commands):
            how_many = proc['how_many'][ii]
            from_, to = proc['from'][ii], proc['to'][ii]
            pickup_stack = [stacks[from_].pop() for jj in range(how_many)][::-1]
            stacks[to] += pickup_stack

    return stacks


def find_stack_tops(stacks):

    return ''.join([stack[-1] for stack in stacks])


if __name__ == "__main__":

    fn = "5_data.txt"

    for part in (1, 2):
        if "test" in fn:
            stacks = [
                ['Z', 'N'],
                ['M', 'C', 'D'],
                ['P'],
            ]
        else:
            stacks = [
                ['H', 'T', 'Z', 'D'],
                ['Q', 'R', 'W', 'T', 'G', 'C', 'S'],
                ['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H'],
                ['L', 'C', 'N', 'F', 'H', 'Z'],
                ['G', 'L', 'F', 'Q', 'S'],
                ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S'],
                ['Z', 'F', 'J'],
                ['D', 'L', 'V', 'Z', 'R', 'H', 'Q'],
                ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D'],
            ]

        with open(fn, 'r') as fo:
            commands = fo.read().splitlines()

        proc = build_proc(commands)
        stacks = execute_proc(stacks, commands, proc, part=part)
        print(find_stack_tops(stacks))
