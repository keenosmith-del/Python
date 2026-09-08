def cakes(recipe, available):
    return min(available.get(ingredient, 0) // amount
               for ingredient, amount in recipe.items())


# Test
print(cakes(
    {"flour": 500, "sugar": 200, "eggs": 1},
    {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
))  # 2

print(cakes(
    {"apples": 3, "flour": 300, "sugar": 150, "milk": 100},
    {"flour": 500, "sugar": 200, "milk": 100}
))  # 0
