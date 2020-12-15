f = "sample.txt"
f = "input.txt"


def main():
    instructions = []
    for line in open(f, "rt"):
        instr, para = line.rstrip().split()
        para = int(para)
        instructions.append((instr, para))

    ip = 0
    reg = 0
    processed_instructions = set()

    while 0 <= ip < len(instructions):
        op, param = instructions[ip]
        if ip in processed_instructions:
            break
        processed_instructions.add(ip)

        if op == "jmp":
            ip += (param - 1)
        elif op == "acc":
            reg += param
        ip += 1
    print(reg)


if __name__ == "__main__":
    main()
