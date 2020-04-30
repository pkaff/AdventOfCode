input = '824501'
recipes = '37'
tail = ''
ix1 = 0
ix2 = 1
while input not in tail:
    recipeSum = int(recipes[ix1]) + int(recipes[ix2])
    if recipeSum >= 10: 
        recipes += str(recipeSum // 10)
    recipes += str(recipeSum % 10)
    ix1 = (ix1 + int(recipes[ix1]) + 1) % len(recipes)
    ix2 = (ix2 + int(recipes[ix2]) + 1) % len(recipes)
    tail = recipes[-10:]
print(recipes.index(input))
