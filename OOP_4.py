class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def apply_discount(self,percentage):
        self.percentage = percentage
        self.discount = int((self.price*self.percentage)/100)
        self.discount_price = self.price-self.discount
        print(f'{self.name} after {self.percentage}% discount: {self.discount_price} yen')

itm = input("Enter Item: ")
price = int(input("Enter Price: "))
Items = Item(itm,price)
dis = int(input("Enter Discount: "))
Items.apply_discount(dis)