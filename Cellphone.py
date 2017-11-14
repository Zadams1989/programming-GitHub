class CellPhone:
    def __init__(self, man, model, price):
        self.manufact = man
        self.model = model
        self.retail_price = price

    def set_manufact(self, man):
        self.manufact = man

    def set_model(self, model):
        self.model = model

    def set_retail_price(self, price):
        self.retail_price = price

    def get_manufact(self):
        return self.manufact

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return self.retail_price

man = input('Enter the manufacturer: ')
model = input('Enter the model number: ')
price = float(input('Enter the retail price: '))
phone = CellPhone(man, model, price)
print('Here is the data that you have entered')
print('Manufacturer: ' + phone.get_manufact())
print('Model Number: ' + phone.get_model())
print('Retail Price: $' + '%.2f' % phone.get_retail_price())

