f = "sample.txt"
f = "input.txt"
target = 2020

d = set(map(int, open(f, "rt").readlines()))
dd = sorted(d)
found = False
for idx, v0 in enumerate(dd):
    for v1 in dd[idx+1:]:
        if v0+v1 > target:
            break
        if target-v0-v1 in d:
            print(f"{v0*v1*(target-v0-v1)}")
            found = True
            break
    if found:
        break
else:
    print("No solution")
