

#TODO: Rewrite calculation methods to use immutable values. Use powers of 4 and something like checking the position of a string in the array. E.g "supremium" matches [3], so do 4^(3+5) or something



dusts = ["PRUDENTIUM", "TERTIUM", "IMPERIUM", "SUPREMIUM"]
crafting_options = ["DUST", "TOOL"]



def main():

    total_inferium = 0
    

    print(f"Please enter the tier of dust you want to query, These are: {dusts}")
    dust_selection = check_user_valid_string_input(input().upper(), dusts)

    print(f"Would you like to craft a certain quantity of {crafting_options[0]}, or craft a {crafting_options[1]}?")
    crafting_selection = check_user_valid_string_input(input().upper(), crafting_options)

    print("How many?")
    crafting_quantity = check_user_valid_int_input(input())
    
    if crafting_selection == crafting_options[0].upper():
        print(f"{inferium_needed_to_craft(crafting_quantity, dust_selection)} inferium needed to craft {crafting_quantity} piles of {dust_selection.lower()} dust")
        
    
    if crafting_selection == crafting_options[1].upper():
        print(f"{int(inferium_for_tool(dust_selection, total_inferium))*crafting_quantity} inferium needed to craft {crafting_quantity} {dust_selection} tool(s)")
        
    

def check_user_valid_int_input(user_quantity):
    if user_quantity.isdigit():
        return int(user_quantity)
    else:
        print("Invalid input, please enter a valid number")
        repeat_input = input()
        check_user_valid_int_input(repeat_input)


def check_user_valid_string_input(user_input, valid_input):
    if user_input not in valid_input:
        print("Invalid input, please enter your selection again")
        repeat_input = input().upper()
        check_user_valid_string_input(repeat_input, valid_input)
    else: 
        return user_input






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


