input = 824501
recipes = [3, 7]
ix1 = 0
ix2 = 1
while len(recipes) < input + 10:
    recipeSum = recipes[ix1] + recipes[ix2]
    if recipeSum >= 10: 
        recipes.append(recipeSum // 10)
    recipes.append(recipeSum % 10)
    ix1 = (ix1 + recipes[ix1] + 1) % len(recipes)
    ix2 = (ix2 + recipes[ix2] + 1) % len(recipes)
print([recipes[x] for x in range(input, input + 10)])