print("""
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
myownmenu = []
myorder =""
while myorder != "quit":
    myorder = input('> ')
    print(" ")
    myownmenu.append(myorder)
    if myorder != "quit":  
      if myownmenu.count(myorder) == 1:  
        print(f"** {myownmenu.count(myorder)} order of {myorder} have been added to your meal ** ")
      else:
        print(f"** {myownmenu.count(myorder)} orders of {myorder} have been added to your meal ** ")
    
    print(" ")
   


