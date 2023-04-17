# Write your solution here
def recipes(recipe_filename):
    recipe_list = []
    ingredients = {"ingredients": []}
    with open(recipe_filename) as file:
        databank = []
        for data in file:
            databank.append(data.strip())
        nameinrow = False
        prepinrow = False
        for line in databank:
            if nameinrow == False:
                ingredients["name"] = line
                nameinrow = True
            elif prepinrow == False:
                ingredients["prep time"] = int(line)
                prepinrow = True
            elif len(line) > 0:
                ingredients["ingredients"].append(line)
            else:
                recipe_list.append(ingredients)
                nameinrow = False
                prepinrow = False
                ingredients = {"ingredients": []}
        recipe_list.append(ingredients)

    return recipe_list

def search_by_name(filename: str, word: str):
    recipes_list = recipes(filename)
    search_result = []
    for recipe1 in recipes_list:
        print(recipe1)
        if word.lower() in recipe1["name"].lower():
            search_result.append(recipe1["name"])
    return search_result

def search_by_time(filename: str, prep_time: int):
    recipes_list = recipes(filename)
    search_result = []
    for recipe1 in recipes_list:
        if prep_time >= recipe1['prep time']:
            search_result.append(f"{recipe1['name']}, preparation time {recipe1['prep time']} min")
    return search_result

def search_by_ingredient(filename: str, ingredient: str):
    recipes_list = recipes(filename)
    search_result = []
    for recipe1 in recipes_list:
        if ingredient in recipe1["ingredients"]:
            search_result.append(f"{recipe1['name']}, preparation time {recipe1['prep time']} min")
    return search_result

if __name__ == "__main__":
    program = False
    if program:
        filename = input("Student information: ")
        test = input("Exercises completed: ")
    else:
        # now this is the False branch, and is never executed
        filename = "recipes1.txt"
        test = "eggs"
    # filename = "recipes1.txt" #str(input("filename: "))
    # prep_time = 20 #str(input("word: "))
    found_recipes = search_by_ingredient(filename, test)
    for recipe in found_recipes:
        print(recipe)