class product1:
    def __init__(self,id,name,size,price):
        self.id=id
        self.name=name
        self.size=size
        self.price=price

    def showprice(self):
        return self.price

    def show(self):
        print('name of product= ',self.name)
        print('size of product= ',self.size)
        print('price of product= ',self.price)

class product2(product1):
    def __init__(self,id,name,size,price,color):
        product1.__init__(self,id,name,size,price)
        self.color=color

    def showprice(self):
        return 0.9*self.price

    def show(self):
        product1.show(self)
        print('color of product= ',self.color)

class Customer:
    def __init__(self,id,name,family,address):
        self.id=id
        self.name=name
        self.family=family
        self.address=address

    def show(self):
        print('name=',self.name)
        print('family=',self.family)

    def shopping(self,p):
        print('shopping---------------------')
        p.show()
        n=int(input('Enter money: '))
        if(n>=p.showprice()):
            print('Congratulations , You bought it')
        else:
            print('Oops,I am sorry')


Lp1=[]
print('product1')
for i in range(1):
    name=input('Enter name: ')
    size=input('Enter size: ')
    price=int(input('Enter price: '))
    id=int(input('Enter id: '))
    p=product1(id,name,size,price)
    Lp1.append(p)

Lp2=[]
print('product2')
for i in range(1):
    name=input('Enter name: ')
    size=input('Enter size: ')
    color=input('Enter color: ')
    price=int(input('Enter price: '))
    id=int(input('Enter id: '))
    p=product2(id,name,size,price,color)
    Lp2.append(p)

c1=Customer('1','laptop','ipad','ddd')
c1.shopping(Lp2[0])