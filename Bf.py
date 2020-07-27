import sys
import msvcrt


def read_file(file):
    """Reads the file pointed."""

    f = open(file, "r")
    code_format(f.read())
    f.close()


class _Bf(object):
    """Holds the formatted code and the loops locations."""

    def __init__(self, code=[], braceLoop=[]):
        self.code = code
        self.braceLoop = braceLoop


def getch():
    """Gets a single character from standard input.  Does not echo to the screen."""

    return msvcrt.getch()


def code_format(code):
    """Creates the object with the formatted code."""

    bf.code = code_filter(list(code))
    bf.braceLoop = Loop_finder(code)

    return bf


def code_filter(code):
    """Fliters out non key characters."""

    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def Loop_finder(code):
    """Finds the start and end of all the loops."""

    temp, braceLoop = [], {}

    for position, command in enumerate(code):
        if command == "[":
            temp.append(position)
        if command == "]":
            start = temp.pop()
            braceLoop[start] = position
            braceLoop[position] = start

    return braceLoop


def main():
    global bf
    bf = _Bf()
    mem = [0]
    ptr, pos = 0, 0

    if len(sys.argv) == 2:
        read_file(sys.argv[1])

        while ptr < len(bf.code):
            cmd = bf.code[ptr]
            if cmd == ">":
                pos += 1
            if pos == len(mem):
                mem.append(0)
            if cmd == "<":
                pos = 0 if pos <= 0 else pos - 1
            if cmd == "+":
                mem[pos] = mem[pos] + 1 if mem[pos] < 255 else 0
            if cmd == "-":
                mem[pos] = mem[pos] - 1 if mem[pos] > 0 else 255
            if cmd == "[" and mem[pos] == 0:
                ptr = bf.braceLoop[ptr]
            if cmd == "]" and mem[pos] != 0:
                ptr = bf.braceLoop[ptr]
            if cmd == ".":
                sys.stdout.write(chr(mem[pos]))
            if cmd == ",":
                mem[pos] = ord(getch())

            ptr += 1

    else:
        print("File not detected")


if __name__ == "__main__":
    main()
