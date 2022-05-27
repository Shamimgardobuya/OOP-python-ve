from paramiko import Agent


class Student:
    # name="Effence"
    # age=20
    
    # country="Kenya"
    #Create function with self as parameters
    #Calculate year of birth by subtracting year from age
    #print statemnt
    #End function by creating your object student
    
    #Create a function for initials and pass in self as parameters to access the special attributes
    #find index of first character in firstname and first character in second,seperate with dot
    #End function.
    school="AkiraChix"      #class attribute 
    def __init__(self,full_name,first_name,second_name,age,country,year):
        self.full_name=full_name
        self.first_name=first_name
        self.second_name=second_name
        self.age=age
        self.country=country 
        self.year=year
    def greeting(self):
        return f"Hello{self.name} from {self.country},welcome to {self.school}"
    def date_of_birth(self):
        birthing=self.year-self.age 
        return f"Hello {self.full_name} from  {self.country} ,you were born in {birthing}"
    #create three files fruit.py car.py,Account.py
    def initial(self):
        return f"Hello {self.full_name},your initials are {self.first_name[0]}.{self.second_name[0]}"
        
    
        