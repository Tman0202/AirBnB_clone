# a={1:'tom', 2:'man'}
# b={4:'jone'}
# a.update(b)
# print(a)

 
# class C:

#     # def __init__(self,a,b,c):
#     #     self.a=a
#     #     self.b=b
#     #     self.c=c
#     def set_salery(self, value):
#         self.salery = value
# e = C()     
# e.set_salery(200)  
# print(e.salery) 

# tom1=C('tman','tman1','tman2')
# print(tom1.__dict__)
# di= tom1.__dict__.copy()
# print(di)
# di['a']='maniga'
# print(di)
# dic = self.__dict__.copy()
# print(dic)





# #Creating dictionaries
# dict1 = {'color': 'blue', 'shape': 'square', 'volume':40}
# dict2 = {'color': 'red', 'edges': 4, 'perimeter':15}

# #Creating new pairs and updating old ones
# dict1['area'] = 25 #{'color': 'blue', 'shape': 'square', 'volume': 40, 'area': 25}
# dict2['perimeter'] = 20 #{'color': 'red', 'edges': 4, 'perimeter': 20}

# #Accessing values through keys
# print(dict1['shape'])

# #You can also use get, which doesn't cause an exception when the key is not found
# dict1.get('false_key') #returns None
# dict1.get('false_key', "key not found") #returns the custom message that you wrote 

# #Deleting pairs
# dict1.pop('volume')

# #Merging two dictionaries
# dict1.update(dict2) #if a key exists in both, it takes the value of the second dict
# dict1 #{'color': 'red', 'shape': 'square', 'area': 25, 'edges': 4, 'perimeter': 20}

# #Getting only the values, keys or both (can be used in loops)
# dict1.values() #dict_values(['red', 'square', 25, 4, 20])
# dict1.keys() #dict_keys(['color', 'shape', 'area', 'edges', 'perimeter'])
# dict1.items() 
# #dict_items([('color', 'red'), ('shape', 'square'), ('area', 25), ('edges', 4), ('perimeter', 20)])


# import json
# from dataclasses import dataclass

# @dataclass

# class Person:
#     name: str
#     age: int

# p=Person(name='jone', age=40)


# def encoder(Person):
#     # if isinstance(Person, Person):
#         return {'name':Person.name,'age': Person.age}
#     # raise TypeError(f'object{Person} is not type person')    

# encoded = json.dumps(p,default=encoder)
# print(encoded)




# import cmd

# class Hello(cmd.Cmd):
#     """ simple example"""
#     def do_greet(self,line):
#         """great the line gigaa"""
#         if line:
#             print('hi ',line)
#         else:
#             print("hi ")    

#     def do_EOF(self,line):
#         return True  
#     def post(self):
#         print    
# if __name__ == "__main__":
#     Hello().cmdloop()          

# import pprint

# a={"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}}
# for key, value in a.items():
#     new_obj = a[key]["id"]
#     # self.new(new_obj)
#     print(new_obj)
#     l= a[key]
#     print(l)


print(eval('BaseModel'))

    # Basemodel(**BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2)