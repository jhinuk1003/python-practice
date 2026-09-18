person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')   
print(person)      # Removes the firstname item
person.popitem() 
print(person)
del person['is_married'] 
print(person)              # Removes the address item
      # Removes the is_married item