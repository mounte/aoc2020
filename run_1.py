f = "sample.txt"
f = "input.txt"
from collections import defaultdict

def main():
    for l in open(f, "rt"):
        l = l.strip().split()
        expected = None
        if len(l) == 2:
            # Has expected value
            expected = int(l[1])
        l = list(map(int, l[0].split(',')))

        if expected:
            print(f"{l} ==> {expected}")
        else:
            print(l)

        n = 2020
        out = []
        used = defaultdict(list)
        for i in range(1, n+1):
            #print()
            #print(f"Turn: {i}")
            if i-1 < len(l):
                print(f"Starting num: {l[i-1]}")
                out.append(l[i-1])
                used[l[i-1]].append(i)
            else:
                consider = out[-1]
                #print(f"Considering {consider}")
                usage = used.get(consider)

                
                if usage is None or len(usage) == 1:
                    #print("Was first! => 0")
                    out.append(0)
                    used[0].append(i)
                else:
                    #print(f"{used[consider]}")
                    age = used[consider][-1] - used[consider][-2]
                    #print(age)
                    out.append(age)
                    used[age].append(i)
        if expected:
            print(f"Expected {expected} got: {out[-1]}")
        else:
            print(out[-1])




if __name__ == "__main__":
    main()