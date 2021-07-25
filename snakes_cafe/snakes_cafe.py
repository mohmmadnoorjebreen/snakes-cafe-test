print('**************************************\n','**    Welcome to the Snakes Cafe!   **\n','**    Please see our menu below.    **\n','**\n','** To quit at any time, type "quit" **\n','**************************************')



menu  = [
    {
        "name": "Appetizers",
        "hints": [
            "Wings",
            "Cookies",
            "Spring Rolls",
        ],
    },
    {
        "name": "Entrees",
        "hints": [
            "Salmon",
            "Steak",
            "Meat Tornado",
            "A Literal Garden",
        ],
    },
     {
        "name": "Desserts",
        "hints": [
            "Ice Cream",
            "Cake",
            "Pie",
        ],
    },
      {
        "name": "Drinks",
        "hints": [
            "Coffee",
            "Tea",
            "Unicorn Tears",
        ],
    },
]

for i in menu :
    print(i['name'],'\n----------')
    
    for j in i['hints']:
        print(j)
        
orderMsg = '***********************************\n** What would you like to order? **\n,***********************************'

repeatOrder=[]
customerOrder =  input(orderMsg)

while customerOrder.lower() != 'quit':
    repeatOrder.append(customerOrder)
    repeatOrderCount =0
    for i in repeatOrder:
        if i == customerOrder:
            repeatOrderCount+=1
    print(f'** {(repeatOrderCount)} order of {customerOrder} have been added to your meal **')
    customerOrder=input(orderMsg)             
          
    
   