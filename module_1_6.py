my_dict = {'yan':2003, 'egor':1911,'roma':2010}
print(my_dict)
print(my_dict['yan'])
my_dict.update({"anton": 2020,"gena": 1993})
del my_dict['egor']
print(my_dict.get ('egor'))
print(my_dict)

my_set = {1,2,1,3,3,1.12,'home'}
print(my_set)
my_set.update([5],[(1,2,3)])
my_set.remove(1)
print(my_set)