#f = "sample.txt"
f = "input.txt"

required_fields = (
"byr",
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid")
#"cid")

def parse_line(s:str):
    r = {}
    for fields in s.split():
        k, v = fields.split(":")
        r[k] = v
    return r


def main():
    cl = []
    passports = []
    for l in open(f, "rt").readlines():
        l = l.rstrip()
        if l:
            cl.append(l.rstrip())
        else:
            passports.append(parse_line(" ".join(cl)))
            cl = []

    valid_ct = 0
    for p in passports:
        if all(k in p for k in required_fields):
            valid_ct += 1

    print(valid_ct)

if __name__ == "__main__":
    main()