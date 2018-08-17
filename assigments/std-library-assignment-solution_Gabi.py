# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random as rand
import datetime as dt
print(rand.random())
print(rand.uniform(1, 10.0))

def gen_random_range():
    random1= rand.randint(1,10)
    random2= rand.randrange(0,1)
    return([random1, random2])
 
print('Generated Random Numbers are: {:5}'.format(str(gen_random_range())))

# 2) Use the datetime library together with the random number to generate a random, unique value.
x = dt.datetime.now()
print(dt.datetime.now())
print(x.strftime("%f"))



for i in range(1, 20):
    first_number = dt.datetime.now().strftime("%f")
    second_number = rand.random()
    print(str(float(first_number) * float(second_number)))