from functools import lru_cache
stones = [int(c) for c in open("input.txt", "r").read().strip().split()]
@lru_cache(maxsize=None)
def blink_75(stone, blink):
    if blink == 75:
        return 1
    if stone == 0:
        return blink_75(1, blink + 1)
    elif len(str(stone)) % 2 == 0:
        orig_str = str(stone)
        left, right = orig_str[:len(orig_str)//2], orig_str[len(orig_str)//2:]
        return blink_75(int(left), blink + 1) + blink_75(int(right), blink + 1)
    else:
        return blink_75(stone*2024, blink + 1)

res = 0
for stone in stones:
    res += blink_75(stone, 0)
print(res)