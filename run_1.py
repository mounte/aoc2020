f = "sample.txt"
f = "input.txt"

def check_trees(r):
    return [1 if ch == "#" else 0 for ch in r]

def main():
    lines = open(f, "rt").readlines()
    rows = list(map(check_trees, lines))
    col = 3
    stride = len(rows[0])-1
    step_size = 3
    # step 3 right, one down
    ct = 0
    for r in rows[1:]:
        ct += r[col]
        col += step_size
        col %= stride

    print(ct)



if __name__ == "__main__":
    main()