class market:
    def __init__(self) -> None:
        pass
    
    # Vegetable list with prices
        self.abcd = {
        'Carrot': 1.5,
        'Broccoli': 2.0,
        'Spinach': 1.8,
        'Tomato': 1.2,
        'Cucumber': 1.0,
        'Bell Pepper': 1.5,
        'Zucchini': 2.2,
        'Onion': 1.0,
        'Potato': 0.8,
        'Garlic': 2.5,
        'Apple': 2.0,
        'Banana': 1.0,
        'Orange': 1.5,
        'Grapes': 3.0,
        'Strawberry': 2.5,
        'Mango': 2.8,
        'Pineapple': 2.5,
        'Watermelon': 1.2,
        'Peach': 2.0,
        'Kiwi': 1.8,
    }
    
    def pricechange(self):

        while True:
            choice=int(input("press 0 to change prices and 1 to exit"))    
            if choice==0:
                    print(self.abcd)
                    x=input("enter the product for which u want to change the price: ")
                    
                    if x in self.abcd:
                        newprice=float(input("enter the price in $: "))
                        self.abcd[x]=newprice
                    else:
                        print("Type from the below list correctly")
            elif choice==1:
                print("exiting.....")
                break
        
        print("Updated Prices")
        print(self.abcd)
    
    def addtocart(self):
        self.total=0
        print("welcome to the store")
        print("please select the quantity of the product(If not needed please select 0)")
        for key in self.abcd:
            x=int(input(f"{key}: "))
            if x!=0:
                y=self.abcd[key]
                self.cost = x*y
                self.total += self.cost
        print("The total amount before discount is:  ",self.total)
    
    def billgenerator(self):
        print("1.Cash\n2.Card\n3.UPI\n")
        choice=int(input("Enter the mode of payment: \n"))
        if choice==1:
            cost=self.total-self.total*0.1
        elif choice==2 or choice==3:
            cost=self.total-self.total*0.05
        else:
            print("plesar select a valid option: ")
        print("Yout Discount amount: ",cost)
        print("the total amount after discount is: ",cost)
    
instance=market()
while True:
    print("welcome to the market")
    print("enter 0 to exit the market")
    choice=int(input("Select the mode of application:\n\n1.Customer\n2.User\n"))
    if choice==1:
        print("the following list contains the product name and its pricein the format key:value\n",instance.abcd)
        instance.addtocart()
        print("Billing is under process. Please Wait.....")
        instance.billgenerator()
        print("Thank you for visiting the market")
        break
    
    elif choice==2:
        password=input("Enter the password")
        i=0
        if password!="iamadmin":
                print("ACCESS DENIED!!!!")
        else:
            instance.pricechange()

    elif choice==0:
        print("Thank you for visiting the market")     
    
            