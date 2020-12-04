f = "sample.txt"
f = "input.txt"

def main():
    d = map(str.split, open(f, "rt").readlines())
    valid = 0
    for a, b, c in d:
        count_low, count_high = map(int, a.split('-'))
        ch = b[0]
        ct = c.count(ch)
        if count_low <= ct <= count_high:
            valid += 1

    print(f"{valid}")


if __name__ == "__main__":
    main()
