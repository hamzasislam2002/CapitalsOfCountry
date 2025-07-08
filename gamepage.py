import northamerica, random
score = 0

print("                           Welcome to Country\'s Capitals                      ")
print("-------------------------------------------------------------------------------")
print("|                1.  North America        |               2.  South America   |")
print("-------------------------------------------------------------------------------")
print("|                3.  Europe               |               6.  Africa          |")
print("-------------------------------------------------------------------------------")
print("|                5.  Asia                 |               6.  Exit            |")
print("-------------------------------------------------------------------------------")
print("NOTE: Any number less than 1 or greater than 6 will also quit the game as well.")

answer = int(input("Which continent do you want to explore: "))
na_list = []
for x in northamerica.north_america_capitals.keys():
    na_list.append(x)

print(na_list)
random_answer = random.choice(na_list)
answerz = input(f"What is the capital of {random_answer}")
if answerz == northamerica.north_america_capitals[random_answer]:
    print("YAY")
else:
    print("NAY")



