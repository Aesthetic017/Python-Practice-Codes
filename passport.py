# Ashutosh Anil Deshpande Student ID 201758974
import datetime 
import json

class Passport:
    """
    A class to represent a passport.

    passport_id : 
        Class variable to track passport numbers.

   
    """
    passport_id = 0

    def __init__(self, first_name, last_name, dob, country, exp_date):
        """
        Initializes a new Passport.
    
        first name of the passport holder.
  
        last name of the passport holder. 
    
        date of birth of the passport holder in 'YYYY-MM-DD' format.
     
        country of the passport holder.
    
        expiration date of the passport in 'YYYY-MM-DD' format.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.date.fromisoformat(dob)
        self.country = country
        self.exp_date = datetime.date.fromisoformat(exp_date)

        # Instance variable to store stamped countries
        self.visited_countries = []

        # Assign passport number and increment the id
        self._passport_id = Passport.passport_id
        Passport.passport_id += 1

    def summary(self):
        """
        Returns a summary of the passport details.

        """
        checkValidity = "valid" if self.is_valid() else "invalid"
        return (f"This passport belongs to {self.first_name} {self.last_name}, "
                f"born on {self.dob} in {self.country}. It is {checkValidity}.")


    def is_valid(self):
        """
        Checks if the passport is still valid.
        Returns: True if the passport is valid, False otherwise.
        """
        today = datetime.date.today()
        return today < self.exp_date

    def check_data(self, first_name, last_name, dob, country):
        """
        Verifies the passport details.

            The first name , last name , date of birth and country to check.

        True if the details are matched and the passport is valid, otherwise False.
        """
        return (
            first_name == self.first_name
            and last_name == self.last_name
            and dob == str(self.dob)
            and country == self.country
            and self.is_valid()
        )

    def stamp(self, country):
        """
        Stamps the passport with a visited country.
            The country to stamp.
        """
        if country!= self.country:
            self.visited_countries.append(country)

    def countries_visited(self):
        """
        Returns a list of visited countries.

        """
        return list(set(self.visited_countries))

    def times_visited(self, country):
        """
        Returns the number of times a country has been visited.

        """
        return self.visited_countries.count(country)

    def sum_square_visits(self):
        """
        Returns the sum of squares of visits to all countries.

        """
        return sum([count**2 for count
                    in [self.times_visited(country)
                        for country in set(self.visited_countries)]])

    def passport_number(self):
        """
        Returns the passport number.

        """
        return self._passport_id

   
    
    def export(self, file_name):
        
        """ export data """
    
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "dob": self.dob.fromisoformat(),
            "country": self.country,
            "exp_date": self.exp_date.fromisoformat(),
            "countries_visited": self._countries_visited,
            "passport_number": self.passport_number()
        }
        with open(file_name, 'w') as file:   # reference : week 11 lecture Programming Fundamental 
            json.dump(data, file, indent=4) 
        """
         JSON data
        """    

   
    @classmethod
    def load(cls, file_name):
        """
        Load a BritishPassport instance from a JSON file.
        The name of the file to load the passport data from.
        Returns: A BritishPassport instance populated with data from the file.
        References: This method uses techniques demonstrated in week 11 lecture Programming Fundamentals.

        """
        with open(file_name, 'r') as file:
            data = json.load(file)
            passport = cls(
                first_name=data["first_name"],
                last_name=data["last_name"],
                dob=data["dob"],
                exp_date=data["exp_date"]
            )
            passport._countries_visited = data["countries_visited"]
            Passport._passport_id = max(Passport._passport_id, data["passport_number"] + 1)
            return passport
 
# inheritance method
class BritishPassport(Passport):
    """
    A class to represent a British passport, inheriting from the Passport class.
        First name , Last Name , DOB and Expiry Date of the passport holder.

    """
    def __init__(self, first_name, last_name, dob, exp_date):
        """ 
        Initialize a new BritishPassport instance.

        """
        super().__init__(first_name, last_name, dob, "The United Kingdom of Great Britain and Northern Ireland", exp_date)
        

# passport1 = Passport("Ashutosh", "Deshpande", "1990-01-01", "INDIA", "2030-12-31")
# print(passport1.summary())
# print(passport1.is_valid())
# print(passport1.check_data("Ashutosh", "Deshpande", "1990-01-01", "INDIA"))
# passport1.stamp("Canada")
# passport1.stamp("Mexico")
# passport1.stamp("Canada")  # Duplicate stamp to test unique countries list
# print(passport1.countries_visited())
# print(passport1.times_visited("Canada"))
# print(passport1.times_visited("Mexico"))
# print(passport1.passport_number())
