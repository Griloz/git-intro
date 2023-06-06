
# we create the class/template
class Human:

    # class attributes
    legs = 2
    hands = 2
    head = 1
    ears = 2

    # create a constructor method
    def __init__(self, first_name, last_name, nationality, language, country) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.language = language
        self.country = country

    # create an obj method
    def bio(self):
        print(f'Hi, my name is {self.first_name} and i from {self.country}')


# create obj (initialize the instances) from the class
Jane = Human('Jane', 'Robertson', 'American', 'English', 'USA')
Anna = Human('Anna', 'Ivanova', 'Mongolian', 'Rssian', 'Russia')

# print(f'{Jane.first_name} is from {Jane.country} and speaks {Jane.language}')
# print(f'{Anna.first_name} is from {Anna.country} and speaks {Anna.language}')
# print(f'{Anna.first_name} has 2 {Anna.hands} hands')

# call obj methods
Jane.bio()
Anna.bio()
