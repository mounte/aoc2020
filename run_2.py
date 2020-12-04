f = "sample.txt"
f = "input.txt"

def main():
    d = map(str.split, open(f, "rt").readlines())
    valid = 0
    for a, b, c in d:
        pos_low, pos_high = map(int, a.split('-'))
        ch = b[0]
        ct = 0
        if c[pos_low-1] == ch:
            ct += 1
        if c[pos_high-1] == ch:
            ct += 1

        if ct == 1:
            valid += 1

    print(f"{valid}")


if __name__ == "__main__":
    main()
