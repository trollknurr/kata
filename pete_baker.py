def cakes(recipe, available):
    for key in recipe:
        if key not in available:
            return 0
    counts = 0
    while True:
        for ing, amount in recipe.iteritems():
            if available[ing] >= amount:
                available[ing] -= amount
            else:
                break
        else:
            counts += 1
            continue
        break
    return counts

print cakes(
    {'cocoa': 77, 'nuts': 46, 'sugar': 62},
    {'butter': 1460, 'crumbles': 7303, 'flour': 614, 'eggs': 2890, 'nuts': 5860, 'pears': 6512, 'chocolate': 8234, 'cocoa': 523, 'oil': 5933, 'apples': 772, 'sugar': 6011, 'milk': 7951, 'cream': 5694}
)
