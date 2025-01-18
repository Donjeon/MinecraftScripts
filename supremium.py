#4 inferium makes 1 prudentium
#4 prudentium makes 1 tertium
#4 tertium makes 1 imperium
#4 imperium makes 1 supremium



#TODO: Rewrite methods to be better. Use powers of 4 and something like checking the position of a string in the array. E.g "supremium" matches [3], so do 4^(3+5) or something
#TODO: Account for user input being unexpected (error handling and default values)

dusts = ["PRUDENTIUM", "TERTIUM", "IMPERIUM", "SUPREMIUM"]
crafting_options = ["DUST", "TOOL"]


def main():
    total_inferium = 0
    #Calculate the amount of inferium dust needed to make X quantity of Y dust
    #inferium_needed_to_craft(1 ,"supremium")

    #Calulate inferium needed to make a tool of a certain quality
    print("Please enter the tier of dust you want to query")
    print(f"These are: {dusts}")
    dust_selection = input().upper()
    check_user_valid_input(dust_selection, dusts)

    
    #How do I get the user to input a value until its valid
    #No loops



    print("Would you like to craft a certain quantity of \"DUST\", or craft a \"TOOL\"?")
    crafting_selection = input().upper()
    #crafting_selection = "dust".upper()
    check_user_valid_input(crafting_selection, crafting_options)


    print("How many?")
    crafting_quantity = int(input())
    

    if crafting_selection == crafting_options[0].upper():
        print(f"{inferium_needed_to_craft(crafting_quantity, dust_selection)} inferium needed to craft {crafting_quantity} piles of {dust_selection.lower()} dust")
        
    
    if crafting_selection == crafting_options[1].upper():
        
        result = int(inferium_for_tool(dust_selection, total_inferium))
        print(f"{result*crafting_quantity} inferium needed to craft {crafting_quantity} {dust_selection} tool(s)")
        
    #crafting 20 supremium dust. Expecting 5120
    

def check_user_valid_input(user_input, valid_input):
    if user_input not in valid_input:
        print("Invalid selection, please enter your selection again")
        repeat_input = input().upper()
        check_user_valid_input(repeat_input, valid_input)





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

