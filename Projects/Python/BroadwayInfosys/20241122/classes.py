import datetime

class User:
    ''' It is always a good practice to write a docstring - comments - to describe what this class is doing.'''

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    # class can also be written like this:
    # def __init__(self, n, b):
    #     self.name = n
    #     self.birthday = b


        # Extract first and last names
        name_pieces = name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        today = datetime.date(2024, 11, 23)

        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        
        dob = datetime.date(yyyy,mm,dd) #date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)
    
user = User("Arjun Bhadra Pokharel", "19890929")
print(user.first_name)
print(user.last_name)
print(user.age())
