import northamerica, random, southamerica
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
sa_list = []
for x in northamerica.north_america_capitals.keys():
    na_list.append(x)
for y in southamerica.south_america_capitals.keys():
    sa_list.append(y)
print(na_list)
print(sa_list)
print(africa_list)

if answer == 1:
    random_answer_na = random.choice(na_list)
    answer_na = input(f"What is the capital of {random_answer_na}: ")
    if answer_na == northamerica.north_america_capitals[random_answer_na]:
        print("YAY")
    else:
        print("NAY")
elif answer == 2:
    random_answer_sa = random.choice(sa_list)
    answer_sa = input(f"What is the capital of {random_answer_sa}: ")
    if answer_sa == southamerica.south_america_capitals[random_answer_sa]:
        print("YAY")
    else:
        print("NAY")
elif answer == 3:
    random_answer_sa = random.choice(sa_list)
    answer_sa = input(f"What is the capital of {random_answer_sa}: ")
    if answer_sa == southamerica.south_america_capitals[random_answer_sa]:
        print("YAY")
    else:
        print("NAY")
elif answer == 4:
    random_answer_sa = random.choice(sa_list)
    answer_sa = input(f"What is the capital of {random_answer_sa}: ")
    if answer_sa == southamerica.south_america_capitals[random_answer_sa]:
        print("YAY")
    else:
        print("NAY")
elif answer == 5:
    random_answer_af = random.choice(af_list)
    answer_af = input(f"What is the capital of {random_answer_af}: ")
    if answer_af == southamerica.south_america_capitals[random_answer_af]:
        print("YAY")
    else:
        print("NAY")
else:
    print("GAME OVER")




