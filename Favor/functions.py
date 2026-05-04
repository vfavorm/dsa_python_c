import random

def max_min(numbers):
    for num in numbers:
        if num < minimum:
            minimum=num
        print(f"Current minimum {minimum}")
        
    return minimum

def getValues():
    random_list = random.sample(range(50, 100), k=5)
    random_list = [5, 4, 3, 2, 1]
    print(random_list)
    max_min(random_list)
    
getValues()

