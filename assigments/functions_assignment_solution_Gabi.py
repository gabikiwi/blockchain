# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
def function():
    return ('This is the output of the funtion()')
def normal_function(func):
    return func()

print(normal_function(function))
# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.

print(normal_function(lambda: 1+1))


# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed. 
# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.

def normal_function_modf (*args):
    list_args = list(args) 
    results = list(map(lambda x: x*2, list_args))

    for iterator in results:
        print('{:^20}'.format(iterator))

    return results


print(normal_function_modf(1,2,3))


