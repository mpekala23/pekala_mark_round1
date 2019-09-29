from bs4 import BeautifulSoup
import requests
from PyDictionary import PyDictionary
import random

# a dictionary to get synonyms of words in the menu
dictionary=PyDictionary()

# a function to return the daily menu in dictionary {'lunch': ..., 'dinner': ...} form
def get_menu():
    site_response = requests.get("https://www.thecrimson.com/flyby/", timeout=10)
    site_content = BeautifulSoup(site_response.content, "html.parser")
    whole_list = list(site_content.find(text="Today's Menu").parent.parent.parent.descendants)
    result = {
        "lunch": [],
        "dinner": []
    }
    meal = None
    for element in whole_list:
        if element.string == None or element.string == "\n" or element.string == "See full Harvard Today →":
            continue
        if element.string == "Lunch" or element.string == "Dinner":
            meal = element.string.lower()
        elif meal and element.string not in result[meal]:
            result[meal].append(element.string)
    return result

def main():
    menu_items = get_menu()
    modified = {
        "lunch": [],
        "dinner": []
    }
    for (meal,foods) in menu_items.items():
        for food in foods:
            result = ""
            for word in food.split():
                meaning = dictionary.meaning(word)
                if not meaning:
                    result += word + " "
                else:
                    word_type = random.choice(list(meaning.keys()))
                    try:
                        result += meaning[word_type][0] + " "
                    except:
                        result += word + " "
            modified[meal].append(result[:-1].capitalize()+".")
    with open("output.txt", "w") as fout:
        fout.write("Lunch Menu:\n")
        for food in modified["lunch"]:
            fout.write(food + "\n")
        fout.write("\nDinner Menu:\n")
        for food in modified["dinner"]:
            fout.write(food + "\n")

if __name__ == "__main__":
    main()
