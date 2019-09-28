import sys

print("NOTHING BUT CHICKEN")
print ("MENU CARD")

lst_choice = []
lst_qty = []
dict_menu = {1:'Naan', 2:'Chicken Tikka', 3:'Butter Chicken', 4:'Ice Cream'}
dict_price = {1:10, 2:200, 3:500, 4:20}

while(1):
    print('1: Naan Rs.10/piece \n2: Chicken Tikka Rs.200/plate \n3: Butter Chicken Rs.500/plate \n4: Ice Cream Rs. 20/serving')
    try:
        a = input('Do you want to order?(y/n)')

    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        continue

    if(a == 'y' or a == 'Y'):
        try:
            choice = int(input('Enter choice'))

        except:
            print("Oops!",sys.exc_info()[0],"occured.")
            continue
        
        if(choice >= 1 and choice <= 4):
            try:
                qty = int(input('How much qty do you need:'))

            except:
                print("Oops!",sys.exc_info()[0],"occured.")
                continue
            
            if(qty >= 1):
                lst_choice.append(choice)
                lst_qty.append(qty)
                print('\n')
                
            else:
                print('Wrong Input \n')
                continue
            
        else:
            print('Wrong Input \n')
            continue

    elif(a == 'n' or a == 'N'):
        print('\n\nBILL:')
        total = 0
        length = len(lst_choice)
        
        for i in range(0, length):
            val = lst_choice[i]
            print(dict_menu[val])
            print('Qty: ', lst_qty[i])
            print('Rs.', dict_price[val], 'per unit')
            print('\n')
            total = total + (dict_price[val] * lst_qty[i])
            
        print('total = Rs.', total)
        print('Thank you')
        break

    else:
        print("Wrong input \n")
        continue


