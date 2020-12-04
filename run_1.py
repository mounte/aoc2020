f = "input.txt"
target = 2020

d = set(map(int, open(f, "rt").readlines()))
for v in d:
    if target-v in d:
        print(f"{v*(target-v)}")
        break
else:
    print("No solution")
