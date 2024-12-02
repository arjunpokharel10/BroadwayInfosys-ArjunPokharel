def cost_of_project(engraving, solid_gold):
    base_cost = 100 if solid_gold else 50
    engraving_cost = (len(engraving) * 10) if solid_gold else (len(engraving) * 7)

    total_cost = base_cost + engraving_cost

    return total_cost


result = cost_of_project('this is a dummy test', False)
print(result)