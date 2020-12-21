from collections import defaultdict, Counter
from functools import reduce

menu = [line.rstrip(")\n").split(" (") for line in open("testinput.txt", "r").readlines()]
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

nonAllergenIngredients = allIngredients - reduce(lambda a, b: a | b, ingredientsThatMightContainAllergen.values())
print(sum([ingredientsCount[ingredient] for ingredient in nonAllergenIngredients]))