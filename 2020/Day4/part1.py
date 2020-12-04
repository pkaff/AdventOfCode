def validPassport(passport):
    return len(passport) == 8 or (len(passport) == 7 and "cid" not in passport.keys())

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