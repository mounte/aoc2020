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

        n = 30000000
        last_out = -1
        used = defaultdict(list)
        for i in range(1, n+1):
            #print()
            #print(f"Turn: {i}")
            if i-1 < len(l):
                print(f"Starting num: {l[i-1]}")
                last_out = l[i-1]
                used[l[i-1]].append(i)
            else:
                #print(f"Considering {consider}")
                usage = used.get(last_out)

                
                if usage is None or len(usage) == 1:
                    #print("Was first! => 0")
                    last_out = 0
                else:
                    #print(f"{used[consider]}")
                    age = used[last_out][-1] - used[last_out][-2]
                    #print(age)
                    last_out = age
                used[last_out].append(i)

        if expected:
            print(f"Expected {expected} got: {last_out}")
        else:
            print(last_out)




if __name__ == "__main__":
    main()