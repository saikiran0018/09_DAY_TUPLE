a=1,2
print(a,type(a))                               # (1,2) class 'tuple'

a=(1,)
print(a,type(a))                               # tuple  

a=('nokia','apple','samsung','lenova')
a[1]='motorolla'                               # typeerror: 'tuple' object does not support item assignment
 
n=("hello","world","ashish")
print(n,type(n))                                  # tuple
print(n[3])                                       # Index error:tuple index out of range

v=(1,4.2,'hello',[2,3],('h','d'))
print(v,type(v))                                         # tuple

print (dir(tuple))

v=(1,4.2,'hello',[1,2],('h','d','hello','hello'))
print(v.count(4.32))                                 # 0
print(v.index([1,2]))                                 # 3
print(v.index(42.3))                               # value error: tuple . index(x): x not in tuple
print(v.count('hello'))                                   # 1