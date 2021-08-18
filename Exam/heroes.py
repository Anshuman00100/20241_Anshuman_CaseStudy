class Hero:     # initializing class
    hero = input("Enter the strengths of heroes(include spaces between each of them): ")
    if (hero.find(",") > 0):  # Custom made exception
        raise Exception("Delimiter error: use space between the values")
    hero_energy = list(map(int, hero.split(" "))) #Converting the data into list for ease of comparision
    hero_energy.sort()
    list1 = hero_energy