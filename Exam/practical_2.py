import heroes #importing heroes class
import enemies  #importing enemies class




def winner(list1, list2):  # Using Function
    if (sorted(list1) == sorted(list2)): #check if the sorted list are equal
        print("Equal Energy!")
    else:
        list3 = [] #Making another mock list just to check for unequality of list
        for element in range(0, len(heroes.Hero.list1)):
            if list1[element] >= list2[element]: #To check if heroes won
                list3.append("Won") #Adds "Heroes won" to the mock list
            else:
                list3.append("lost") #Adds "Enemies won to the mock list
        if "lost" in list3:
            print("MAXI: LOSE")
        else:
            print("MAXI: WIN")


winner(heroes.Hero.list1, enemies.Enemy.list2)
print(heroes.Hero.list1)
print(enemies.Enemy.list2)

