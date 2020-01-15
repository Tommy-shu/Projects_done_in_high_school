# Food suggestion bot
#Author: Tommy Shu
#Date: Feb 06,2019

#Description: A bot to ask me about my favourite food in Vancouver. Then it chould suggest a restaurants with that dish!

#Ask the user for a favourite dish, e.g. tempura
print ("What is your favourite dish?")
#Get the dish name, e.g. tempure
dish = input(). lower(). strip("!.")

#Make a category such as Japanese, with a list of possible sishes
japanese_foods = ["tempura", "sushi", "sashimi", "Ramen"]
Italian_foods =["spaghetti", "pasta"]
Chinese_foods = ["fired rice", "chow mein", "Ma Po Tofu", "Dumplings", "spring rolls"]

#Then suggest a Japanese restuarant if the user's favourite dish is tempura, or sushi, or sashimi
if dish in japanese_foods:
    print("Oh, you should try Suchi Garden Metrotown.")
elif dish in Italian_foods:
    print("Oh, you should try Jimoco on Austin road.")
elif dish in Chinese_foods:
    print("Oh, you should go to J's Wok on Austin road.")
else:
    print ("I don't know what to do with you.")