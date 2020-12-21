from collections import defaultdict, Counter
from functools import reduce

menu = [line.rstrip(")\n").split(" (") for line in open("input.txt", "r").readlines()]
allIngredients = set()
allergenToLinesOfIngredients = defaultdict(list)
ingredientsCount = Counter()
for ingredients, allergens in menu:
    ingredientsList = ingredients.split()
    allergensList = allergens.split("contains ")[1].split(", ")
    allIngredients.update(ingredientsList)
    ingredientsCount.update(ingredientsList)
    for allergen in allergensList:
        allergenToLinesOfIngredients[allergen].append(ingredientsList)

ingredientsThatMightContainAllergen = defaultdict(lambda : allIngredients.copy())
for allergen, ingredientsLists in allergenToLinesOfIngredients.items():
    for ingredients in ingredientsLists:
        ingredientsThatMightContainAllergen[allergen] &= set(ingredients)

visited = []
while not all(list(map(lambda kv: len(kv[1]) == 1, ingredientsThatMightContainAllergen.items()))):
    for allergen, ingredients in ingredientsThatMightContainAllergen.items():
        if len(ingredients) == 1 and ingredients not in visited:
            visited.append(ingredients)
            for otherAllergen, otherAllergenIngredients in ingredientsThatMightContainAllergen.items():
                if allergen != otherAllergen:
                    otherAllergenIngredients -= ingredients
            break
print(",".join([ingredient.pop() for allergen, ingredient in sorted(ingredientsThatMightContainAllergen.items(), key=lambda kv: kv[0])]))