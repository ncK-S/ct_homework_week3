# this is the code from last week's assingment
# myItems = []
# cartTotal = 0

# def addItem(itemName, itemPrice):
#     myItems.append(itemName)
#     return(itemPrice)

# cartTotal += addItem('DJI Mini 2 Drone', 220.87)
# cartTotal += addItem('Shoes', 51.23)
# cartTotal += addItem('Jeans', 39.89)
# cartTotal += addItem('How To Grow A Moustache Like Ryan - Paperback Edition', 28.87)
# cartTotal += addItem('RYAN TIME Official Soundtrack', 10.28)
# cartTotal += addItem('Becoming An Ethical Hacker: The Basics - Hardcover Edition', 20.98)
# cartTotal += addItem('Cracking the Coding Interview - Paperback Edition', 34.17)

# cartSummary = dict((item,myItems.count(item))for item in myItems)

# print(cartSummary)
# print(cartTotal)

# below is the OOP version
class myCart():
    def __init__(self):
        self.total = 0
        self.items = {}
    def addItem(self,item_name,quantity,price):
        self.total += price*quantity
        self.items.update({item_name:quantity})
        return self.total,self.items
    def removeItem(self,item_name,quantity,price):
        if item_name in self.items:
            if quantity < self.items[item_name] and quantity > 0:
                self.items[item_name] -= quantity
                self.total -= price*quantity
            elif quantity >= self.items[item_name]:
                self.total -= price*self.items[item_name]
                del self.items[item_name]
            return self.items,self.total
    def checkout(self,cash_paid):
            if cash_paid >= self.total:
                return cash_paid - self.total
            else:
                return "you need more money"

        
        
Shop = myCart()
Shop.addItem("Golf Balls",20,1.00)
Shop.addItem("Basketball",1,25.00)
print(Shop.addItem("Golf Balls",20,1.00))
print(Shop.removeItem("Basketball",1,25.00))
print(Shop.checkout(200))


# ddddd