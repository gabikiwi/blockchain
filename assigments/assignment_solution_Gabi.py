# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
persons = [
    { "name": "Tom", "age": 41, 'hobbies':['chess', 'surfing', 'reading'] },
    { "name": "Max", "age": 29, 'hobbies': ['javascript', 'hiking', 'foreign languages']  },
    { "name": "Pam", "age": 27, 'hobbies':['piano', 'social', 'foreign languages'] },
    { "name": "Dick", "age": 17, 'hobbies': ['grils', 'beer', 'parties']}
]


# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
names = [dic['name'] for dic in persons]
print(names)

# 3) Use a list comprehension to check whether all persons are older than 20.
ages_bigger_than_20 = ([dic['age'] > 20 for dic in persons])
all_ages_bigger_than_20 = all(ages_bigger_than_20)
print(all_ages_bigger_than_20)

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# copied_persons = persons[:]

copied_persons = persons[:]
copied_persons_deep = [dic.copy() for dic in copied_persons]
copied_persons_deep[0]['name'] = "Gabriel"
print(copied_persons_deep)
print('Original person list is ',  persons)



# 5) Unpack the persons of the original list into different variables and output these variables.
unpack_persons = [dic.items() for dic in persons]
print(unpack_persons)
for person in unpack_persons:
    for (key, value) in person:
        print('variable ', key, '= ', value)




