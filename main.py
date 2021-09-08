class Genre():
    def __init__(self, name: str, restaurants: {}):
        self.name = name
        self.restaurants = restaurants

    def print(self):
        print(self.name)
        print("-" * 60)
        for restaurant in self.restaurants:
            print(restaurant + " " + str(self.restaurants[restaurant]))


if __name__ == '__main__':
    Italianfoods = {"Olive Garden": 1, "Maggianos": 1, "Noodles and Company": 1}
    Pizza = {"Pizza Hut": 1, "Nicolo's": 1, "Garlic Jim's": 1, "Anthony's": 1}
    Mexicanfoods = {"3 Margaritas": 1, "Brewery Bar III": 1, "Los Dos Portillos": 1, "Casa Caliente": 1}
    Fastfoods = {"Taco Bell": 1, "Wendy's": 1, "Burger King": 1, "Chic fil'a": 1, "McDonalds": 1, "Raising Cane's": 1}
    Wings = {"Hooters": 1, "Buffalo Wild Wings": 1, "Wingstop": 1}

    Italian = Genre("Italian", Italianfoods)
    Genre("Pizza", Pizza)
    Genre("Mexican", Mexicanfoods)

    Italian.print()
