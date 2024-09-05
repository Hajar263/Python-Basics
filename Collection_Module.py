# 1_OrderedDict
import collections
d1=collections.OrderedDict()
d1['A']=10
d1['C']=12
d1['B']=11
d1['D']=13
d1['C']=20
print(d1['C'])
print(d1.keys())
print(d1.values())
for k,v in d1.items():
    print (k,v)

# 2_defaultdict
from collections import defaultdict
number = defaultdict(int)   #int
number['one'] = 1
number['two'] = 2
print(number['three'])
print(type(number))


# 3_counter
from collections import Counter
print(Counter(['B','B','A','B','C','A','B','B','A','C','C','C','C']))
print(Counter({'A':3, 'B':5, 'C':7, 'A':4}))
print(Counter(A=3, B=5, C=2))

# 4_ChainMap
from collections import ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
c = ChainMap(d1, d2, d3)
print(c)
a=[7,4,6,7]
n=[9,3,0,3,7]
print(ChainMap(a,n))


# 5_namedtuple
from collections import namedtuple
Student = namedtuple('Student',['name','age','DOB'])
S = Student('Nandini','19','2541997')
li = ['Manjeet', '19', '411997' ]
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }
print ("The namedtuple instance using iterable is : ")
print (Student._make(li))
print ("The OrderedDict instance using namedtuple is : ")
print (S._asdict())




