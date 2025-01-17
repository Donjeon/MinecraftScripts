#4 inferium makes 1 prudentium
#4 prudentium makes 1 tertium
#4 tertium makes 1 imperium
#4 imperium makes 1 supremium

dusts = ["prudentium", "tertium", "imperium", "supremium"]

def inferium_needed_to_craft(quantity, dust_type):
    inferium_needed = quantity

    if dust_type in dusts[0:]: #if dust_type is in a value of 1 and beyond
        inferium_needed *=4
        if dust_type in dusts[1:]: 
            inferium_needed *=4 
            if dust_type in dusts[2:]:
                inferium_needed *=4
                if dust_type in dusts[3:]:
                    inferium_needed *=4

    
    return inferium_needed

def inferium_for_tool(dust_type):
    total_inferium = 0

    if dust_type in dusts[0:]: #Prudentium is dust_type
        total_inferium += inferium_needed_to_craft(8, "prudentium")
        if dust_type in dusts[1:]:
            total_inferium += inferium_needed_to_craft(8, "tertium")
            if dust_type in dusts[2:]:
                total_inferium += inferium_needed_to_craft(8, "imperium")
                if dust_type in dusts[3:]:
                    total_inferium += inferium_needed_to_craft(8, "supremium")

    print(total_inferium)
    return total_inferium

#Calculate the amount of inferium dust needed to make X quantity of Y dust
#inferium_needed_to_craft(1 ,"supremium")

#Calulate inferium needed to make a tool of a certain quality
inferium_for_tool("supremium")

