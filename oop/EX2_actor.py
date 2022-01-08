"""
𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻:
Design TomCruise class and DulquerSalman class which inherit from Actor 
class so that the following code provides the expected output.
You can not change any of the given code. Do not modify the given parent 
class.
Note: add_movie() method in both child classes should work for any number 
of parameters and assume parameters will be even numbers.

class Actor:
   def __init__(self, name, rating, industry):
     self.name = name
     self.rating = rating
     self.industry = industry

   def add_movie(self, *info):
     pass

   def __str__(self):
     s = f"Name: {self.name}\nRating: {self.rating}\nIndustry: {self.industry}"
     return s

# Write your codes here.
tom_cruise = TomCruise("Tom Cruise", 9.5, "Hollywood", 0)
tom_cruise.add_movie("Knight & Day", "Action", "Top Gun", "Action", "Jerry Maguire", "Romance", "Jack Reacher", "Thriller", "The Firm", "Thriller")
print('1.------------------------------------')
print(tom_cruise.oscar_status())
print('2.------------------------------------')
print(tom_cruise)
print('3.====================================')
dulquer_salman = DulquerSalman("Dulquer Salman", 9, "Malayalam", 5)
dulquer_salman.add_movie("Thriller", "Bangalore Days", "Romance", "Ustad Hotel", "Thriller", "Charlie", "Action", "Kurup", "Action", "Vikramadithyan")
print('4.------------------------------------')
print(dulquer_salman.award_status())
print('5.------------------------------------')
print(dulquer_salman)

OUTPUT:
1.------------------------------------
Tom Cruise has won 0 Oscar(s)!!!
2.------------------------------------
Actor Details:
Name: Tom Cruise
Rating: 9.5
Industry: Hollywood
Oscar Win: 0
Movies:
Action: ['Knight & Day', 'Top Gun']
Romance: ['Jerry Maguire']
Thriller: ['Jack Reacher', 'The Firm']
3.====================================
4.------------------------------------
Dulquer Salman has won 5 award(s)!!!
5.------------------------------------
Actor Details:
Name: Dulquer Salman
Rating: 9
Industry: Malayalam
Award Win: 5
Movies:
Thriller: ['Bangalore Days', 'Charlie']
Romance: ['Ustad Hotel']
Action: ['Kurup', 'Vikramadithyan']
"""


class Actor:
    def __init__(self, name, rating, industry):
        self.name = name
        self.rating = rating
        self.industry = industry

    def add_movie(self, *info):
        pass

    def __str__(self):
        s = f"Name: {self.name}\nRating: {self.rating}\nIndustry: {self.industry}"
        return s


class TomCruise(Actor):
    def __init__(self, name, rating, industry, oscar):
        super().__init__(name, rating, industry)
        self.movies = {}
        self.oscar = oscar

    # def add_movie(self, *info):
    #     info = list(info)
    #     for i in range(len(info)):
    #         if i == 0:
    #             self.movies[info[i+1]].append(info[0])
    #         elif i % 2 != 0 and i < len(info)-1:
    #             self.movies[info[i]].append(info[i+1])
    #         else:
    #             continue

    def add_movie(self, *info):
        info = list(info)
        for i in range(1, len(info), 2):
            if info[i] not in self.movies:
                self.movies[info[i]] = []
            self.movies[info[i]].append(info[i - 1])

    def oscar_status(self):
        return f"{self.name} has won {self.oscar} Oscar(s)!!!"

    def __str__(self):
        thriller = self.movies["Thriller"]
        action = self.movies["Action"]
        romance = self.movies["Romance"]
        s = f"Name: {self.name}\nRating: {self.rating}\nIndustry: {self.industry}\nAwards: {self.oscar}"
        m = f"\nMovies: \nThriller: {thriller}\nAction: {action}\nRomantic: {romance}"
        a = s + m
        return a


class DulquerSalman(Actor):
    def __init__(self, name, rating, industry, award):
        super().__init__(name, rating, industry)
        # self.movies = {
        #     'Action': [], 'Romance': [], 'Thriller': []
        # }
        self.movies = {}
        self.award = award

    # def add_movie(self, *info):
    #     info = list(info)
    #     for i in range(len(info)):
    #         if i == 0:
    #             self.movies[info[0]].append(info[1])
    #         elif i % 2 == 0 and i < len(info)-1:
    #             self.movies[info[i]].append(info[i+1])
    #         else:
    #             continue

    def add_movie(self, *info):
        info = list(info)
        for i in range(0, len(info), 2):
            if info[i] not in self.movies:
                self.movies[info[i]] = []
            self.movies[info[i]].append(info[i + 1])

    def award_status(self):
        return f"{self.name} has won {self.award} Awards(s)!!!"

    def __str__(self):
        thriller = self.movies["Thriller"]
        action = self.movies["Action"]
        romance = self.movies["Romance"]
        s = f"Name: {self.name}\nRating: {self.rating}\nIndustry: {self.industry}\nAwards: {self.award}"
        m = f"\nMovies: \nThriller: {thriller}\nAction: {action}\nRomantic: {romance}"
        a = s + m
        return a


tom_cruise = TomCruise("Tom Cruise", 9.5, "Hollywood", 0)
tom_cruise.add_movie(
    "Knight & Day",
    "Action",
    "Top Gun",
    "Action",
    "Jerry Maguire",
    "Romance",
    "Jack Reacher",
    "Thriller",
    "The Firm",
    "Thriller",
)
print("1.------------------------------------")
print(tom_cruise.oscar_status())
print("2.------------------------------------")
print(tom_cruise)
print("3.====================================")
dulquer_salman = DulquerSalman("Dulquer Salman", 9, "Malayalam", 5)
dulquer_salman.add_movie(
    "Thriller",
    "Bangalore Days",
    "Romance",
    "Ustad Hotel",
    "Thriller",
    "Charlie",
    "Action",
    "Kurup",
    "Action",
    "Vikramadithyan",
)
print("4.------------------------------------")
print(dulquer_salman.award_status())
print("5.------------------------------------")
print(dulquer_salman)
