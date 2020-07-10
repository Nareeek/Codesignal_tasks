def groupingDishes(dishes):
    d = {}
    
    for i in range(len(dishes)):
        for j in range(1, len(dishes[i])):
            if dishes[i][j] not in d:
                d[dishes[i][j]] = [dishes[i][0]]
            else:
                d[dishes[i][j]] += [dishes[i][0]]
                
    di = {key:sorted(val) for key, val in d.items() if len(val) > 1}
    
    keys = [k for k in di]
    dish = [[k] + di[k] for k in sorted(keys)]
    
    return dish

print(groupingDishes([["Salad","Tomato","Cucumber","Salad","Sauce"], 
                      ["Pizza","Tomato","Sausage","Sauce","Dough"], 
                      ["Quesadilla","Chicken","Cheese","Sauce"], 
                      ["Sandwich","Salad","Bread","Tomato","Cheese"]]))