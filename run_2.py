#f = "sample.txt"
f = "input.txt"
import re

def check_h(v):
    unit = v[-2:]
    try:
        if unit == "in":
            return 59 <= int(v[:-2]) <= 76
        elif unit == "cm":
            return 150 <= int(v[:-2]) <= 193
    except ValueError:
        pass
    return False

ecl = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

cl_check = re.compile(r"^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$")
num_check = re.compile(r"^\d+$")

validators = {
    "byr": lambda v: len(v) == 4 and 1920 <= int(v) <= 2002,
    "iyr": lambda v: len(v) == 4 and 2010 <= int(v) <= 2020,
    "eyr": lambda v: len(v) == 4 and 2020 <= int(v) <= 2030,
    "hgt": check_h,
    "hcl": lambda v: cl_check.match(v),
    "ecl": lambda v: len(v) == 3 and v in ecl,
    "pid": lambda v: len(v) == 9 and  num_check.match(v),
}

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
        if all(k in p for k in validators.keys()):
            for key,val in p.items():
                if key == "cid":
                    continue
                if not validators[key](val):
                    break
            else:
                valid_ct += 1

    print(valid_ct)

if __name__ == "__main__":
    main()