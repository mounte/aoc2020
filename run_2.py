import math

f = "sample.txt"
f = "input.txt"

def check_trees(r):
    return [1 if ch == "#" else 0 for ch in r]

def main():
    lines = open(f, "rt").readlines()
    rows = list(map(check_trees, lines))
    
    stride = len(rows[0])-1
    vals = []
    for step_size, row_jumps in ((1,1), (3,1), (5,1), (7,1), (1,2)):
        # step 3 right, one down
        print(f"testing step_size={step_size}, row_jump={row_jumps}")
        ct = 0
        col = 0
        for r in rows[::row_jumps]:
            ct += r[col]
            col += step_size
            col %= stride
        vals.append(ct)
        print(ct)
    print(math.prod(vals))


if __name__ == "__main__":
    main()