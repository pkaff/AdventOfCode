stones = [int(c) for c in open("input.txt", "r").read().strip().split()]
for i in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            orig_str = str(stone)
            left, right = orig_str[:len(orig_str)//2], orig_str[len(orig_str)//2:]
            new_stones.append(int(left))
            new_stones.append(int(right))
        else:
            new_stones.append(stone*2024)
    stones = new_stones[:]
print(len(stones))