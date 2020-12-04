def validField(key, value):
    if key == "byr":
        val = int(value)
        return val >= 1920 and val <= 2002
    if key == "iyr":
        val = int(value)
        return val >= 2010 and val <= 2020
    if key == "eyr":
        val = int(value)
        return val >= 2020 and val <= 2030
    if key == "hgt":
        try:
            hgt = int(value[:-2])
        except ValueError:
            return False
        if "cm" in value:
            return hgt >= 150 and hgt <= 193
        elif "in" in value:
            return hgt >= 59 and hgt <= 76
        else:
            return False
    if key == "hcl":
        if len(value) != 7:
            return False
        try:
            return value[0] == "#" and int(value[1:7], 16)
        except ValueError:
            return False
    if key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if key == "pid":
        try:
            return len(value) == 9 and int(value)
        except ValueError:
            return False
    if key == "cid":
        return True

def validPassport(passport):
    if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport.keys()):
        for key, value in passport.items():
            if not validField(key, value):
                return False
        return True
    return False

passports = [dict()]
validPassports = 0
myinput = [l.strip() for l in open("input.txt", "r").readlines()]
for line in myinput:
    if not line:
        validPassports += validPassport(passports[-1])
        passports.append(dict())
    else:
        for key, value in [kv.split(":") for kv in line.split()]:
            passports[-1][key] = value
validPassports += validPassport(passports[-1])
print(validPassports)