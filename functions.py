def hello(name,age):
    year =2022-age
    return f"Hello {name} you were born in {year}"
def my_country(country="Uganda",student="Susan"):
    return f"Hello,you are from {country} {student}"
    
def greet(name):
    return f"Hello{name}"   
def greet_multiple(*names): # asterix tell interpreter that i don't know the length now iteration starts.
    for name in names:
          print(f"Hello {name}")
def adding(*numbers):
    p=0
    for number in numbers:
        p+=number
        return p
def multiply(*numbers):
    answer=1
    for number in numbers:
        answer+=number
        return answer
def greeti_multiple(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    keys = kwargs.keys()
    # values=kwargs.values()
    if "country" in keys:
        print(f"Hello,{kwargs['country']}")
    elif "age" in keys:
        year=2022-kwargs["age"]
        print(f"you were born in {year}")
    elif not kwargs:
        print(f"Hello Anonymous")    #the code  will run if it finds a true stmt and disreGARDS The rest as false.
def sum_and_greet(*args,**kwargs):
    sum=0
    for num in args:
        sum+=num
    keys=kwargs.keys()
    if "name" in keys:
        print(f"Hello,{kwargs['name']}, the answer is {sum}")# if one condition is true the rest are invalid
    elif "country" in keys:
        print(f"Hello,from {kwargs['country']} the answer is {sum}") 
    elif not kwargs:
        print("Hello anonymous")
        
        
    
    
    
      
    
  

