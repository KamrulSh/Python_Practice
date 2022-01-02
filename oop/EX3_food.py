'''
𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻:
Design Vegetable class and Fruit class which inherit from Food class so 
that the following code provides the expected output.

[Assume, the price for a vegetable or a fruit per kg is the same 
irrespective of its size. The add_Vegetables() and add_fruits methods in 
both child classes should work for any number of parameters and any size of 
the fruit/vegetable ]

class Food:
     def init(self, name, rich_in):
         self.name = name
         self.rich_in = rich_in

     def str(self):
         s = f"Name: {self.name}\nRich in {self.rich_in}"
         return s

# Write your codes here.
# Do not change the following lines of code.
g1 = Vegetable("Tomato", "folate, vitamin C, and potassium", 60)
g1.add_Vegetables("Red large Tomato - 5kg","Green small tomato - 2kg","red 
Medium Tomato - 3kg","green Large tomato - 2kg","Yellow Medium Tomato - 
1kg")
print('====================================')
g1.show_Cost()
print('====================================')
print(g1)
print('====================================')
g2 = Fruit("Apple", "fiber, vitamin C, and various antioxidants", 90)
g2.add_Fruits("Red small Apple - 9kg", "Green small Apple - 5kg", "red 
Large Apple - 9kg")
print('====================================')
g2.show_Cost()
print('====================================')
print(g2)

OUTPUT:
====================================
Tomato , total cost: 780 BDT
====================================
Name: Tomato
Rich in folate, vitamin C, and potassium
Price: 60 BDT per kg
Vegetable Details:
Red : ['large-5kg', 'Medium-3kg']
Green : ['small-2kg', 'Large-2kg']
Yellow : ['Medium-1kg']
====================================
====================================
Apple , total cost: 2070 BDT
====================================
Name: Apple
Rich in fiber, vitamin C, and various antioxidants
Price: 90 BDT per kg
Fruit Details:
Red : ['small-9kg', 'Large-9kg']
Green : ['small-5kg']
'''


class Food:
    def __init__(self, name, rich_in):
        self.name = name
        self.rich_in = rich_in

    def str(self):
        s = f"Name: {self.name}\nRich in {self.rich_in}"
        return s


class Vegetable(Food):

    def __init__(self, name, rich_in, price):
        super().__init__(name, rich_in)
        self.price = price
        self.color = {}
        self.total = 0

    def add_Vegetables(self, *infos):
        infos = list(infos)
        items = []
        for info in infos:
            items.append(info.split())

        for item in items:
            item[0] = item[0].title()
            if item[0] not in self.color:
                self.color[item[0]] = []
            str = item[1] + item[3] + item[4]
            self.color[item[0]].append(str)
            self.total += int(item[-1][-3]) * self.price

    def show_Cost(self):
        print(f"{self.name}, total cost: {self.total} BDT")

    def __str__(self):
        s = f"Name: {self.name}\nRich in {self.rich_in}\n"
        p = f"Price: {self.price} BDT per kg\nVegetable Details:"
        f = ""
        for key, val in self.color.items():
            f += "\n" + str(key) + " : " + str(val)
        all = s+p + f
        return all


class Fruit(Food):

    def __init__(self, name, rich_in, price):
        super().__init__(name, rich_in)
        self.price = price
        self.color = {}
        self.total = 0

    def add_Fruits(self, *infos):
        infos = list(infos)
        items = []
        for info in infos:
            items.append(info.split())

        for item in items:
            item[0] = item[0].title()
            if item[0] not in self.color:
                self.color[item[0]] = []
            str = item[1] + item[3] + item[4]
            self.color[item[0]].append(str)
            self.total += int(item[-1][-3]) * self.price

    def show_Cost(self):
        print(f"{self.name}, total cost: {self.total} BDT")

    def __str__(self):
        s = f"Name: {self.name}\nRich in {self.rich_in}\n"
        p = f"Price: {self.price} BDT per kg\nFruit Details:"
        f = ""
        for key, val in self.color.items():
            f += "\n" + str(key) + " : " + str(val)
        all = s+p + f
        return all


# Do not change the following lines of code.
g1 = Vegetable("Tomato", "folate, vitamin C, and potassium", 60)
g1.add_Vegetables("Red large Tomato - 5kg", "Green small tomato - 2kg",
                  "red Medium Tomato - 3kg", "green Large tomato - 2kg", "Yellow Medium Tomato - 1kg")
print('====================================')
g1.show_Cost()
print('====================================')
print(g1)
print('====================================')
g2 = Fruit("Apple", "fiber, vitamin C, and various antioxidants", 90)
g2.add_Fruits("Red small Apple - 9kg",
              "Green small Apple - 5kg", "red Large Apple - 9kg")
print('====================================')
g2.show_Cost()
print('====================================')
print(g2)
