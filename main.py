import random


class Genre():
    def __init__(self, name: str, restaurants: {}):
        self.name = name
        self.restaurants = restaurants

    def print(self):
        print(self.name)
        print("-" * 60)
        for restaurant in self.restaurants:
            print(restaurant + " " + str(self.restaurants[restaurant]))

class picker():
    def choose_one(restaurant_list):
        rand_val = random.random()
        total = 0
        for k, v in restaurant_list.items():
            total += v
            if rand_val <= total:
                return k
        assert False, 'unreachable'




if __name__ == '__main__':
    Italianfoods = {"Olive Garden": .1, "Maggianos": .2, "Noodles and Company": .7}
    Pizza = {"Pizza Hut": 1, "Nicolo's": 1, "Garlic Jim's": 1, "Anthony's": 1}
    Mexicanfoods = {"3 Margaritas": 1, "Brewery Bar III": 1, "Los Dos Portillos": 1, "Casa Caliente": 1}
    Fastfoods = {"Taco Bell": 1, "Wendy's": 1, "Burger King": 1, "Chic fil'a": 1, "McDonalds": 1, "Raising Cane's": 1}
    Wings = {"Hooters": 1, "Buffalo Wild Wings": 1, "Wingstop": 1}

    Italian = Genre("Italian", Italianfoods)
    Genre("Pizza", Pizza)
    Genre("Mexican", Mexicanfoods)

    Italian.print()
    print(picker.choose_one(Italian.restaurants))
