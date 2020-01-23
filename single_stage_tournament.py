from random import shuffle

all_players = [1, 6, 3, 5, 4, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
shuffle(all_players)

def sublist(lst, n):
    sub = []
    result = []
    for i in lst:
        sub += [i]
        if len(sub) == n:
            result += [sub]
            sub = []
    if sub:
        result += [sub]
    return result

def is_power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)

while len(all_players) != 1:

    # Creating list with the length of 2 for matching up later
    derived_list = sublist(all_players, 2)
    print('------------------')
    print('Derived List -- ', derived_list)
    print('------------------')

    if is_power_of_two(len(derived_list)):

        # Emptying all players list to insert next round players
        all_players = []
        for each_derived_list in derived_list:

            if len(each_derived_list) == 2:
                number1 = each_derived_list[0]
                number2 = each_derived_list[1]
                
                if number1 > number2:
                    all_players.append(number1)
                else:
                    all_players.append(number2)
            else:
                number3 = each_derived_list[0]
                all_players.append(number3)
    else:
        new_list = derived_list[0:len(derived_list)-1]
        # print("New list -- ", new_list)
        another_list = derived_list[(len(derived_list)-1):len(derived_list)]
        # print("Another list -- ", another_list)
        all_players = []

        for each_derived_list in new_list:
            number1 = each_derived_list[0]
            # print("Number1 -- ", number1)
            number2 = each_derived_list[1]
            # print("Number2 -- ", number2)
            
            if number1 > number2:
                all_players.append(number1)
            else:
                all_players.append(number2)

        new_list = []
        # print(new_list)
        # print("Length of another list -- ", len(another_list))

        # Counting the length of the derived list in another list
        count = 0
        for i in another_list:
            count += len(i)

        # Check if the length of the derived list has 2 items
        if count == 2:
            number1 = another_list[0][0]
            # print("Number3 --- ", number3)
            number2 = another_list[0][1]
            # print("Number4 --- ", number4)

            if number1 > number2:
                all_players.append(number1)
            else:
                all_players.append(number2)
        else:
            number1 = another_list[0][0]
            all_players.append(number1)
        another_list = []

print('=====================')
print(all_players)