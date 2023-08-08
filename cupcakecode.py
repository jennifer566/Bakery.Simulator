cupcakeArray=["vanilla","chocolate","orange","strawberry","peanut butter"] #A list of cupcake flavors that the user will choose from
costArray=[3.00,2.50,1.50,3.40,2.40] # A list of cupcake costs 
totalcost=[] #an empty list that will later hold the costs of the choosen cupcakes 

#The print functions introduce the user to the cupcake menu and cupcake costs
print("Welcome to Jennifer's Bakery!!\nCupcake Menu: ", cupcakeArray)
print("Cost: ", costArray)

def cupcakecost(num):
    '''gets an order of cupcakes from the user, returns the cupcake flavor, cost, and total cost'''
    print("You have", num, "attempts to order") 
    global totalcost1
    for i in range(num):   #This for conditional for-loop loops for a specific number of times using the function parameter
        userpick=input("choose a cupcake flavor from the menu: ")
        if userpick.lower() in cupcakeArray: #This if-statement ensures the input cupcake is in the cupcakeArray list
            index=cupcakeArray.index(userpick.lower())
            cost=float(costArray[index])
            totalcost.append(cost)
            print("Cupcake choice: ", userpick.lower(), "\nCost:", "$", cost)
        elif not(userpick.lower() in cupcakeArray):
            totalcost1=float(sum(totalcost))
            print("item not in menu")
            pass
    totalcost1=float(sum(totalcost))
    print("\t TOTAL COST $", totalcost1, "\n")

def updates(add,remove):  #the add parameter indicates the number of cupcakes that will be added, the remove parameter indicates the amount of cupcakes that will be removed from the cupcakeArray list 
    '''adds and removes cupcake flavors from the menu, and
    returns the updated menu'''
    print("Time to add", add, "new flavors to the menu!")
    for c in range(add):   #This conditional for-loop loops for a specific number of times using the int from the add variable
        additions= str(input("which cupcake flavor would you like to add to the menu: "))
        print(additions, "added")
        cost2= float(input("how much do they cost $$ (enter float or int): "))
        print("$", cost2)
        cupcakeArray.insert(0,additions)
        costArray.insert(0,cost2)
    print(add, "NEW ITEM(S)")
    print("New Menu: ", cupcakeArray,"\n")
    ogcupcakeArray=len(cupcakeArray)
    print("Time to remove", remove,"out of stock cupcakes :( ")
    while not(len(cupcakeArray)==(ogcupcakeArray-remove)):   #This conditional while-loop loops as long as the length of cupcakeArray list does not match the length of the cupcakeArray minus the number from the function parameter
        soldout=str(input("which cupcake flavor is sold out: "))
        if soldout in cupcakeArray:
            cupcakeArray.remove(soldout)
            print(soldout, "removed")
        else:
            print("not in menu, try again")
            pass

    print(remove,"SOLD OUT")
    print("New Menu: ", cupcakeArray)

def budget(): 
    '''This function calculates the difference of 
    the user input budget and the total cost of the cupcake order'''
    print("Lets make sure the order fits your budget")
    amount=float(input("what is your budget? "))  
    if totalcost1>amount: 
        '''These if-statements utilize comparison operators to decide whether
        the total cost exceeds the budget, is below the budget, or equals to the budget. '''
        less=float(totalcost1-amount)
        print("Oops. The order is $", less, "more than your budget")
    elif totalcost1<amount:
        more=float(amount-totalcost1)
        print("Good! The order is $",more,"less than your budget")
    elif totalcost1==amount:
        print("Perfect! The order matches your budget of $", amount)


cupcakecost(3)
budget()
updates(2,2)
