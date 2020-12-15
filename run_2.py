f = "sample.txt"
f = "input.txt"


def main():
    instructions = []
    fudge_index = [-1]
    for idx, line in enumerate(open(f, "rt")):
        instr, para = line.rstrip().split()
        para = int(para)
        if instr in ("nop", "jmp"):
            fudge_index.append(idx)

        instructions.append((instr, para))

    def run_prog(program):
        ip = 0
        reg = 0
        processed_instructions = set()
        while 0 <= ip < len(program):
            op, param = program[ip]
            if ip in processed_instructions:
                return False

            processed_instructions.add(ip)
            if op == "jmp":
                ip += (param-1)
            elif op == "acc":
                reg += param
            ip += 1

        print(reg)
        return True

    for fi in fudge_index:
        the_prog = instructions[:]
        if fi >= 0:
            old_instr, param = the_prog[fi]
            if old_instr == "jmp":
                new_instr = "nop", param
            else:
                new_instr = "jmp", param
            the_prog[fi] = new_instr

        if run_prog(the_prog):
            break

if __name__ == "__main__":
    main()
