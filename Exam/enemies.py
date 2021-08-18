class Enemy:
    enemy = input("Enter the strengths of enemies(include spaces between each of them): ")
    if (enemy.find(",") > 0): #Custom made exception
        raise Exception("Delimiter error: use space between the values")
    enemy_energy = list(map(int, enemy.split(" "))) #Convert given data into list for ease of development
    enemy_energy.sort()
    list2 = enemy_energy