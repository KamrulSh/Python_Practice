'''
𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻:
Implement the design of the Pasta class so that the following output is 
produced:

print("Pasta Plate Count:", Pasta.pasta_plate_count)
print("=======================")
s1 = Pasta("Chicken")
s1.set_ingredients("Farfalle",250, 11, 40, 10)
s1.display_all_info()
print("------------------------------------")
s2 = Pasta("Beef")
s2.set_ingredients("Pipe Rigate",150, 10.5, 10, 10)
s2.display_all_info()
print("------------------------------------")
s3 = Pasta("Mushrooms")
s3.set_ingredients("Spaghetti",500, 50, 20, 10)
s3.display_all_info()
print("=======================")
print("Pasta Plate Count:", Pasta.pasta_plate_count)

Output:
Pasta Plate Count: 0
=======================
Pasta Type: Chicken
Shape: Farfalle
Cal: 250 g
Fat: 11 g
Protein: 40 g
Carbohydrate: 10 g
------------------------------------
Pasta Type: Beef
Shape: Pipe Rigate
Cal: 150 g
Fat: 10.5 g
Protein: 10 g
Carbohydrate: 10 g
------------------------------------
Pasta Type: Mushrooms
Shape: Spaghetti
Cal: 500 g
Fat: 50 g
Protein: 20 g
Carbohydrate: 10 g
=======================
Pasta Plate Count: 3
'''


class Pasta:

    pasta_plate_count = 0

    def __init__(self, name):
        self.name = name
        Pasta.pasta_plate_count += 1

    def set_ingredients(self, type, cal, fat, prot, carb):
        self.type = type
        self.cal = cal
        self.fat = fat
        self.prot = prot
        self.carb = carb

    def display_all_info(self):
        s1 = f"Pasta Type: {self.name}\n"
        s2 = f"Shape: {self.type}\n"
        s3 = f"Cal: {self.cal} g\n"
        s4 = f"Fat: {self.fat} g\n"
        s5 = f"Protein: {self.prot} g\n"
        s6 = f"Carbohydrate: {self.carb} g"
        s = s1 + s2 + s3 + s4 + s5 + s6
        print(s)


print("Pasta Plate Count:", Pasta.pasta_plate_count)
print("=======================")
s1 = Pasta("Chicken")
s1.set_ingredients("Farfalle", 250, 11, 40, 10)
s1.display_all_info()
print("------------------------------------")
s2 = Pasta("Beef")
s2.set_ingredients("Pipe Rigate", 150, 10.5, 10, 10)
s2.display_all_info()
print("------------------------------------")
s3 = Pasta("Mushrooms")
s3.set_ingredients("Spaghetti", 500, 50, 20, 10)
s3.display_all_info()
print("=======================")
print("Pasta Plate Count:", Pasta.pasta_plate_count)
