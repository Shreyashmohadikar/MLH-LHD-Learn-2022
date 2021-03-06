grocery_item = {} 
grocery_history = [] 

stop = False 

while not stop:
    item_name = input("Item name:\n")   
    quantity = input("Quantity purchased:\n")   
    cost = input("Price per item:\n")
    grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)}
    grocery_history.append(grocery_item)
    user_input = input("Enter another item?\nType 'c' for continue or 'q' to quit:\n")
    if user_input == 'q':
      stop = True

grand_total = 0  

for index, item in enumerate(grocery_history):
    item_total = item['number'] * item['price']
    grand_total = grand_total + item_total
    print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
    item_total = 0

print('Grand total: $%.2f' % grand_total)
