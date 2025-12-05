ranges, ingredients = open("input.txt", "r").read().split('\n\n')
ranges = [range(int(start), int(end)+1) for start, end in (line.split('-') for line in ranges.splitlines())]
ingredients = [int(ingredient) for ingredient in ingredients.splitlines()]
print(sum(1 for ingredient in ingredients if any(ingredient in r for r in ranges)))