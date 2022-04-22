# ''' sorted()'''
# a=[1,6,3,8,2]
# a.sort()
# print(a)
# print(sorted([12,3,120,9]))   #[3, 9, 12, 120]
# print(sorted([12,3,4,56]))    #[3, 4, 12, 56]
# '''all'''
# print(all([True,1,2]))         #True
# print(all([True,'',1,2]))      #False
# print(all([True,' ',1,2]))     #True
# print(all([True,False,1,2]))   #False
# print(all([True,True,1,2,0]))  #False
# print(all(([True,True,1,2,None])))  #False
# '''any'''
# print(any([True,False,False,22]))     #True
# print(any([False,False,0]))           #False
# print(any([True,True,None,0]))       #True
# ''' bool'''
# print(bool(False))     #False
# print(bool(1))         #True
# print(bool(0))         #False
# print(bool(None))      #False
# print(bool('bool'))    #True
# '''eval()'''
# print('eval=', eval('3+2.5-1'))   #4.5
# a=eval('4+8-7')
# b=eval('6+3.9-4')
# c=eval('3+2.5-1')
# print(a,type(a))     #5 int
# print(b,type(b))     #5.9 Float
# print(c,type(c),)    #4.5Float
# '''sum()'''
# print('sum=',sum([1,2,3,4,5]))     #15
# print('sum=',sum((10.5,20,30)))    #60.5
# '''reversed()-list'''
# for i in reversed([1,2,3,4]):
#     print(i)       
# '''reversed()-tuple  '''
# for i in reversed ((10,20,30,40)):
#     print(i)   
# '''enumerate()'''
# a=['water', 'milk','glass']
# b=enumerate(a) 
# print(type(b)) #class 
# print(dict(b))  ##{0: 'water', 1: 'milk', 2: 'glass'}
# print(list(b))  #[]
# print(tuple(b))#()
# a=['water','milk','glass']
# c=enumerate(a,6)
# print(list(c))#[(6, 'water'), (7, 'milk'), (8, 'glass')]