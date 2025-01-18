#4 inferium makes 1 prudentium
#4 prudentium makes 1 tertium
#4 tertium makes 1 imperium
#4 imperium makes 1 supremium

#TODO: Ask for input when running the script and walk the user through how stuff works
#TODO: Expand to growth accelerators
#TODO: Rewrite methods to be better. Use powers of 4 and something like checking the position of a string in the array. E.g "supremium" matches [3], so do 4^(3+5) or something

dusts = ["PRUDENTIUM", "TERTIUM", "IMPERIUM", "SUPREMIUM"]


def main():
    total_inferium = 0
    #Calculate the amount of inferium dust needed to make X quantity of Y dust
    #inferium_needed_to_craft(1 ,"supremium")

    #Calulate inferium needed to make a tool of a certain quality
    print("Please enter the tier of dust you want to query")
    print(f"These are: {dusts}")
    dust_selection = input().upper()
    #dust_selection = "supremium".upper()

    print("Would you like to craft a certain quantity of \"dust\", or craft a \"tool\"?")
    crafting_selection = input().upper()
    #crafting_selection = "dust".upper()


    print("How many?")
    crafting_quantity = int(input())
    #crafting_quantity = 20

    if crafting_selection == "dust".upper():
        print(inferium_needed_to_craft(crafting_quantity, dust_selection))
        
    
    if crafting_selection == "tool".upper():
        
        result = int(inferium_for_tool(dust_selection, total_inferium))
        print(result*crafting_quantity)
        
    #crafting 20 supremium dust. Expecting 5120
    





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

def inferium_for_tool(dust_type, total_inferium):
    

    if dust_type in dusts[0:]: #Prudentium is dust_type
        total_inferium += inferium_needed_to_craft(8, dusts[0])
        if dust_type in dusts[1:]:
            total_inferium += inferium_needed_to_craft(8, dusts[1])
            if dust_type in dusts[2:]:
                total_inferium += inferium_needed_to_craft(8, dusts[2])
                if dust_type in dusts[3:]:
                    total_inferium += inferium_needed_to_craft(8, dusts[3])

    #print(total_inferium)
    return total_inferium


main()

