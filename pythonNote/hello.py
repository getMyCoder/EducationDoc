# strs='hello %s ,I have $%d' % ('zhangsan',10000)
# print(strs)
# strrs='hello {0},you have {1:0.2f}'.format('xiaohong',2.222)
# print(strrs)
# arrs=['zhangsan','lisi','wangwu','www','hao']
# print(arrs)
# print(len(arrs))
# arrs.append('大佬')
# print(arrs)
# arrs.insert(1,'taiji')
# print(arrs)
# arrs.pop()
# print(arrs)
# arrs[0]='zs'
# print(arrs)
# ---------------------------------------------------------
# age=15
# if age<10:
#     print('儿童')
# elif age<18:
#     print('未成年')
# else:
#     print('成年')
# -------------------------------------------------------
# str=input('num:')
# str=int(str)
# if str>100:
#     print('大于100')
# else:
#     print('小于100')
# -------------------------------------------------------
# height=1.75
# weight=80.5
# if weight/(height*height)<18.5:
#     print('过轻')
# elif height/(weight*weight)<25:
#     print('正常')
# elif height/(weight*weight)<28:
#     print('过重')
# elif height/(weight*weight)<32:
#     print('肥胖')
# else:
#     print('严重肥胖')
# -------------------------------------------------------
# y=0
# for x in range(10):
#     y=y+x
# print(y)
# -------------------------------------------------------
# x=10
# n=0
# sum=0
# while n<x:
#     sum=sum+n
#     n=n+1
#     if n>5:
#         continue
#     if n>8:
#         break
# print(sum)
# -------------------------------------------------------
# x=10
# n=0
# while n<x:
#     n = n + 1
#     if n==5:
#         continue
#     if n>8:
#         break
#     print(n)
# -------------------------------------------------------
# setdict={'zhangsan':100,'lisi':99,'wangwu':50,'liuliu':60}
# setdict['zhangsan']=90
# print(setdict['zhangsan'])
# print('www' in setdict)
# print(setdict.get('www',-1))
# setdict.pop('zhangsan')
# print(setdict)
# -------------------------------------------------------
# name=set([5,6,7,8,2,2,3,6,5])
# print(name)
# name.add(50)
# print(name)
# name.remove(1)
# print(name)
# -------------------------------------------------------
# age=[5,6,8,9,1,2,1,3,8,4,6,11]
# age.sort()
# print(age)
# name='hello world'
# name.replace('l','L')
# print(name.replace('l','L'))
# -------------------------------------------------------
# maxval=max(1,2,3,699)
# print(maxval)
# print(int('126'))
# print(float('22.36'))
# print(str(123))
# print(hex(1))
# -------------------------------------------------------
# from function import setNum
# print(setNum(11,22))
# def nos():
#     pass
# print(isinstance(10,int))
# print(isinstance('11',int))
# import math
# def setSql(a, b, c):
#     val1 = math.sqrt((b / (2 * a)) ** 2 - c / a) - b / (2 * a)
#     val2 = -math.sqrt((b / (2 * a)) ** 2 - c / a) - b / (2 * a)
#     if val1==val2:
#         return '%f' % (val1)
#     else:
#         return '%f | %f' % (val1, val2)
# print(setSql(1, 4, 4))
# -------------------------------------------------------
# def setArr(L=None):
#     if L==None:
#         L=[]
#     L.append('END')
#     return L
# print(setArr())
# print(setArr())
# print(setArr())
# print(setArr())
# print(setArr())
# -------------------------------------------------------
# def setVal(numbers):
#     sum=0
#     for x in numbers:
#         sum=sum+x*x
#     return sum
# print(setVal([1,2,3]))
# def setVal(*numbers):
#     sum=0
#     for x in numbers:
#         sum=sum+x*x
#     return sum
# print(setVal(1,2,3))
# -------------------------------------------------------
# name='zhangsan'
# print('name:',name)
# def fun(name,age,**kw):
#     print('name:',name,'age:',age,'keyword:',kw)
# fun('zhangsan',100,text='hello world',content='this is jinan')
# -------------------------------------------------------
# def fun(name,age,*,text,content):
#     print('name:',name,'age:',age,'text:',text,'content:',content)
# fun('zhangsan',22,text='hello world',content='山东济南')
# def fun(name,age,*flage,text,content):
#     print('name:',name,'age:',age,'flage:',flage,'text:',text,'content:',content)
# fun('zhangsan',22,1,5,6,text='hello world',content='山东济南')
# def fun(name,age=20,*flage,text,**kw):
#     print('name:',name)
#     print('age:',age)
#     print('flage:',flage)
#     print('text:',text)
#     print('kw',kw)
# fun('json',120,2,2,3,4,text='济南',content='山东省',main='中国')
# def setVal(*num):
#     sum=1
#     for n in num:
#         sum=sum*n
#     return sum
# print(setVal(1,2,3,4,5))

# def setFun(n,a,b,c):
#     if n==1:
#         print(a,'-->',c)
#     else:
#         setFun(n-1,a,c,b)
#         setFun(1,a,b,c)
#         setFun(n-1,b,a,c)
#
# setFun(3,'A','B','C')
# -------------------------------------------------------
# 递归
# def fun(num):
#     if num>1:
#         return num * fun(num - 1)
#     else:
#         return num
# print(fun(5))
# 尾递归
# def setFun(n):
#     return setFunction(n,1)
# def setFunction(n,sum):
#     if n==1:
#         return sum
#     return setFunction(n-1,n*sum)
# print(setFun(4))
# -------------------------------------------------------
# age=[2,3,6,98,2,6,2,6]
# for i in range(len(age)):
#     print(age[i])
# for i in age:
#     print(i)
# print(age[0:5])
# print(age[3:5])
# print(age[-2:-1])
# value=list(range(100))
# print(value[0:10:2])
# 去除字符串首尾空格
# name = ' hello world  '
# def setName(val):
#     n = 0
#     sum = ''
#     while n < len(val):
#         if val[n] != ' ':
#             sum = val[n:len(val)]
#             x = -1
#             xsum = 0
#             while x > -len(sum):
#                 if sum[x] != ' ':
#                     xsum = sum[-len(sum):x + 1]
#                     return xsum
#                 else:
#                     x = x - 1
#         else:
#             n = n + 1
# print(setName(name))
# -------------------------------------------------------
# d = {'a': 1, 'b': 2, 'c': 3}
# for k in d:
#     print(k)
# print('-------------')
# for v in d.values():
#     print(v)
# print('-------------')
# for k,v in d.items():
#     print(k,'-->',v)
# from collections.abc import Iterable
# print(isinstance('adf',Iterable))
# print(isinstance([1,2,3],Iterable))
# print(isinstance(222,Iterable))
# age=[2,3,6,5,6,5,6]
# for n in enumerate(age):
#     print(n)
# 迭代一个数组的最大值和最小值
# val = [2, 36, 92, 9, 89, 991,1]
# def getM(Array):
#     maxVal = Array[0]
#     minVal = Array[0]
#     for n in Array:
#         if maxVal < n:
#             maxVal = n
#         if minVal > n:
#             minVal = n
#     return (maxVal, minVal)
# print(getM(val))
# -------------------------------------------------------
# name=list(range(1,10))
# print(name)
# l=[]
# for n in list(range(1,11)):
#     l.append(n*n)
# print(l)
# val=[n*n for n in list(range(1,11))]
# print(val)
# val1=[x+y for x in '123' for y in 'ABC']
# print(val1)
# import os
# dir=[n for n in os.listdir()]
# print(dir)
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# value=[k+"="+v for k,v in d.items()]
# print(value)
# L = ['HelLo', 'World', 18, 'Apple', None]
# value=[v.lower() for v in L if isinstance(v,str)]
# print(value)
# -------------------------------------------------------
# L = (x * x for x in range(10))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# for n in L:
#     print(n)
# def fun(num):
#     n, a, b = 0, 0, 1
#     while n < num:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
# fun(10)
# def fun(num):
#     n, a, b = 0, 0, 1
#     while n < num:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#
# for x in fun(10):
#     print(x)
# 杨辉三角
# def fun(num):
#     n=1
#     ArrS=[1]
#     ArrE=[1]
#     while n<num+1:
#         print(ArrE)
#         for x in range(0,n):
#             if x>=1:
#                 ArrE[x]=ArrS[x]+ArrS[x-1]
#         ArrE.append(1)
#         ArrS.append(1)
#         for k,v in enumerate(ArrE):
#             ArrS[k]=v
#         n=n+1
# fun(10)
# -------------------------------------------------------
# print(abs(-10))
# def val(x):
#     return x*x
# newList=map(val,[1,2,3])
# print()
# list(newList)
from functools import reduce

# def fun(x,y):
#     return x*10+y
# print(reduce(fun,[1,2,3]))
# def fun(x,y):
#     return x*10+y
# def setfun(n):
#     arr={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return arr[n]
# print(reduce(fun,map(setfun,'146')))
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def fun(arr):
#     arrs = arr.lower()
#     return arrs
# def getfun(arr):
#     Arrs=arr.replace(arr[0],chr(ord(arr[0]) - 32),1)
#     return Arrs
# def setfun(arr):
#     ARR = list(map(fun, arr))
#     return list(map(getfun, ARR))
# Arr = ['adam', 'LISA', 'barT']
# print(setfun(Arr))
# name='abca'
# names=name.replace('a','A',1)
# print(names)
# print(name.title())
# -------------------------------------------------------
# def fun(n):
#     return n % 2 == 1
# print(list(filter(fun, [1, 2, 3, 4, 5, 6])))
# def fun(n):
#     return n and n.strip()
# print(list(filter(fun, ['a', ' c', 'b', None, ''])))
# a=lambda x:x+1
# print(a(1))
# def setA(n):
#     lambda n:n+1
# print(setA(1))
# def name():
#     n=1
#     yield n+1
#     next()
#     yield n+5
# print(next(name()))
# print(next(name()))
# print(next(name()))
# print(next(name()))
# print(next(name()))
# def fun(n):
#     return lambda x: x % n ==1
# print(list(filter(fun(2), [1, 2, 3, 4, 5, 6])))
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# it = _odd_iter()
# print(next(it))
# -------------------------------------------------------
# arr=[2,36,9,66,-9]
# print(sorted(arr,key=abs))
# arrs=['bob', 'about', 'Zoo', 'Credit']
# print(sorted(arrs,key=str.lower,reverse=True))
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0]
# def by_core(t):
#     return -t[1]
# print(sorted(L, key=by_name))
# print(sorted(L, key=by_core))
# -------------------------------------------------------
# def setSum(*arg):
#     def sum():
#         num = 0
#         for n in arg:
#             num = num + n
#         return num
#     return sum
# nn = setSum(1, 2, 3)
# print(nn())
# -----1-----
# def setVal():
#     sum=[]
#     for n in range(1,4):
#         sum.append(n*n)
#     return sum
# print(setVal())
# -----2-----
# def setVal():
#     sum=[]
#     def getV(j):
#         def GV():
#             return j*j
#         return GV
#     for n in range(1,4):
#         sum.append(getV(n))
#     return sum
# f1,f2,f3=setVal()
# print(f1())
# print(f2())
# print(f3())
# 作业 计数器
# -----------1----------
# def sum():
#     n = 0
#     def sm():
#         nonlocal n
#         n=n+1
#         return n
#     return sm
# nn = sum()
# print(nn())
# print(nn())
# print(nn())
#  -----------2----------
# def sum():
#     n = [0]
#     def sm():
#         n[0]=n[0]+1
#         return n[0]
#     return sm
# nn = sum()
# print(nn())
# print(nn())
# print(nn())
# -----------3----------
# def sum():
#     n=0
#     while True:
#         n=n+1
#         yield n
# nn = sum()
# print(next(nn))
# print(next(nn))
# print(next(nn))
# print(next(nn))
# print(next(nn))
# print(next(nn))
# -------------------------------------------------------
# arr=list(map(lambda x:x*x,[1,2,3,4,5,6]))
# print(arr)
# 作业
# L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
# print(L)
# -------------------------------------------------------
# def setA(fun):
#     print('这是原函数')
#     return fun()
# @setA
# def fun():
#     print('this is hello world')
# def Afun():
#     print('this is A')
# B=Afun
# B()
# print(B.__name__)
# print(B==Afun)
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# @log('execute')
# def now():
#     print('2015-3-25')
# now()
# now = log('execute')(now)
# print(now)
# print(now.__name__)
# print('-----------')
# import time
# begin = time.time()
# print(begin)
# print('')
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# 装饰器
# import functools,time
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         begin=time.time()
#         r=func(*args,**kw)
#         end = time.time()
#         print('this is time:',end-begin)
#         return r
#     return wrapper
# @log
# def setV():
#     print('this is setV')
# setV()
# -------------------------------------------------------
# num=int('001011100101',base=2)
# print(num)
# import functools
# fu=functools.partial(int,base=2)
# print(fu('10101101010110'))
# def setInt(val):
#     return int(val,base=2)
# print(setInt('10101010110'))
# -------------------------------------------------------
# import web.hello
# web.hello.val1('zhangsan')
# -------------------------------------------------------
# import sys
# sys.path.append('/F:/IDE/Anaconda/Scripts')
# -------------------------------------------------------
# class Student(object):
#
#     def __init__(self, name, score):
#         print(object)
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
#
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()
# -----------------------面向对象--------------------------------
# class Students(object):
#     def __init__(self, name):
#         self.name = name
#     def setStudent(self):
#         print(self.name)
# getStu = Students('helloworld')
# getStu.setStudent()
# getStu.name='zhangsan'
# print(getStu.name)
# print('-----')
# getStu.setStudent()
# ------------------------访问权限-------------------------------
# class Student(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def setmsg(self):
#         print('%s: %s' % (self.__name, self.__age))
# getS = Student('hello', '200')
# getS.setmsg()
# print(getS.__name)
# 作业
# class Student(object):
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         self.__gender=gender
#         return self.__gender
# stu=Student('hello','world')
# print(stu.get_gender())
# print(stu.set_gender('what'))
# print(stu.get_gender())
# --------------------继承和多态-----------------------------------
# class Father(object):
#     def run(self):
#         print('this is father')
# class Son(Father):
#     pass
# class Son1(Father):
#     pass
# sons = Son()
# sons.run()
# class Father(object):
#     def run(self):
#         print('this is father')
# class Son(Father):
#     def run(self):
#         print('this is son')
# sons = Son()
# # sons.run()
# def setSon(father):
#     father.run()
# setSon(Father())
# setSon(Son())
# --------------------获取对象信息-----------------------------------
# def fun():
#     pass
# print(type('asf'))
# print(type(123)==type('adf'))
# import types
# print(type(fun)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x: x)==types.LambdaType)
# print(type((x for x in range(10)))==types.GeneratorType)
# class Father(object):
#     pass
# class Son(Father):
#     pass
# father=Father()
# son=Son()
# print(isinstance(father,Father))
# print(isinstance(son,Father))
# print(isinstance(son,Son))
# name='hello world'
# print(dir(name))
# print(len(name))
# print(name.__len__())
# class SetName(object):
#     def __init__(self):
#         self.A=10
# setname=SetName()
# print(hasattr(setname,'A'))
# print(hasattr(setname,'B'))
# setattr(setname,'B',100)
# print(setname.B)
# print(hasattr(setname,'B'))
# print(getattr(setname,'B'))

# ----------------实例属性和类属性--------------------------------------
# class Student(object):
#     def __init__(self):
#         self.name='zhangsan'
# stu=Student()
# print(stu.name)
# class SetStu(object):
#     name = 'lisi'
#     def __init__(self):
#         self.name = 'zhangsan'
# ss = SetStu()
# print(ss.name)
# class Student(object):
#     count=0
#     def __init__(self,name):
#         Student.count+=1
#         self.name=name
#     def sum(self):
#         print(Student.count)
# SD=Student('zhangsan')
# SD=Student('zhangsan')
# SD=Student('zhangsan')
# SD=Student('zhangsan')
# SD=Student('zhangsan')
# SD.sum()
# -------------------------------------------------------
# class Student(object):
#     pass
# stu = Student()
# # stu.name = 'zhangsan'
# # print(stu.name)
# from types import MethodType
# def names(self, name):
#     self.name = name
# stu.sss = MethodType(names, stu)
# stu.sss(20)
# print(stu.name)
# stt=Student()
# print(stt.name)
# class Student(object):
#     pass
# def names(self, name):
#     self.name = name
# Student.names=names
# stu=Student()
# stu.names('zhangsanfeng')
# print(stu.name)
# stt=Student()
# stt.names('lisi')
# print(stt.name)
# class Student(object):
#     __slots__ = ('name','age')
# stt=Student()
# stt.name='zhangsan'
# stt.age=20
# stt.score=100
# print(stt.name)
# print(stt.age)
# print(stt.score)
# -------------------使用@property------------------------------------
# class Student(object):
#     def getS(self):
#         return self.score
#     def setS(self,val):
#         if isinstance(val,int) and (val>=0 and val<=100):
#             self.score=val
#         else:
#             print('this is error')
# stu=Student()
# stu.setS('sadf')
# print(stu.getS())
# 装饰器
# class Student(object):
#     @property
#     def setval(self):
#         return self.score
#     @setval.setter
#     def setval(self,val):
#         if isinstance(val,int) and (val>=0 and val<=100):
#             self.score=val
#         else:
#             print('this is error')
# stu=Student()
# stu.setval=20
# print(stu.setval)
# 进化
# class Student(object):
#     @property
#     def setval(self):
#         return self.score
#     @setval.setter
#     def setval(self,val):
#         if isinstance(val,int) and (val>=0 and val<=100):
#             self.score=val
#         else:
#             print('this is error')
#     @property
#     def getval(self):
#         return 2019-self.score
# stu=Student()
# stu.setval=20
# print(stu.setval)
# print(stu.getval)
# 作业
# class Screen(object):
#     @property
#     def width(self):
#         return self.wd
#     @width.setter
#     def width(self,val):
#         self.wd=val
#     @property
#     def height(self):
#         return self.hd
#     @height.setter
#     def height(self,val):
#         self.hd=val
#     @property
#     def resolution(self):
#         return self.wd*self.hd
# sc=Screen()
# sc.width=100
# sc.height=200
# print(sc.resolution)
# --------------------多继承-----------------------------------
# class A(object):
#     pass
# class Ason(A):
#     pass
# class B(object):
#     pass
# class ASson(Ason,B):
#     pass
# -----------------定制类--------------------------------------
# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
# print(Student('hello'))
# s=Student('hello')
# print(s)
# class Student(object):
#     def __init__(self):
#         self.A,self.B=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.A,self.B=self.B,self.A+self.B
#         if self.A>10:
#             raise StopIteration
#         return self.A
# print(list(Student())[5])
# for n in Student():
#     print(n)
# class Fib(object):
#     def __getitem__(self, item):
#         a,b=0,1
#         for n in range(item):
#             a,b=b,a+b
#         return a
# print(Fib()[1])
# 斐波拉契数列
# class Student(object):
#     def __getitem__(self, item):
#         if isinstance(item,int):
#             a,b=0,1
#             for n in range(item):
#                 a,b=b,a+b
#             return a
#         if isinstance(item,slice):
#             L=[]
#             a,b=0,1
#             s=item.start
#             if s is None:
#                 s=0
#             e=item.stop
#             for n in range(e):
#                 L.append(a)
#                 if n>=s:
#                     a,b=b,a+b
#             return L
# stu=Student()
# print(stu[:10])
# class Sa(object):
#     def __init__(self):
#         self.name='www'
#     def __getattr__(self, item):
#         if item=='a':
#             return 'this is error'
# s=Sa()
# print(s.aa)
# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#     def __str__(self):
#         return self._path
# ch = Chain()
# print(ch.status.user.timeline.list)
# 自测
# class SetS(object):
#     def __init__(self, name):
#         self.name = name
#     def __getattr__(self, item):
#         return SetS('%s/%s' % (self.name, item))
#     def __str__(self):
#         return self.name
# S = SetS('hello')
# print(S.age)
# print(callable(SetS))

# --------------------枚举-----------------------------------
# from enum import Enum
# moth=Enum('moth',('first','second','three'))
# print(moth.second.value)
# print(moth)
# for name,value in moth.__members__.items():
#     print(name)
# for data in moth:
#     print(data.name,'-->',data.value)
# from enum import Enum, unique
# @unique
# class Moth(Enum):
#     first = 2
#     second = 4
#     three = 50
# print(Moth.first)
# print(Moth['first'])
# print(Moth.first.value)
# print(Moth(50))
# from enum import Enum, unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')
# -------------------使用元类------------------------------------
# from world import world
# w=world()
# w.world()
# print(type(world))
# print(type(w))
# def fn(self):
#     print('hello function')
# Hello = type('Hello', (object,), dict(funName=fn))
# h = Hello()
# h.funName()
# ------------------错误调试-------------------------------------
# try:
#     r=10/1
#     print('try:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally')

# ZeroDivisionError
# ValueError TypeError
# def setA():
#     try:
#         r=10/0
#         print('try:',r)
#     except Exception as e:
#         print('except:',e)
#     else:
#         pass
#     finally:
#         print('end')
# setA()
import logging

# def A(s):
#     r = 10 / int(s)
#     print(r)
# def B(s):
#     A(s)
# def C():
#     B(0)
# def main():
#     try:
#         print(C())
#     except Exception as e:
#         # logging.exception(e)
#         print('-----s-------')
#         raise
#     else:
#         print('no error')
#     finally:
#         print('执行完毕')
# main()
# 作业
# from functools import reduce
# def str2num(s):
#     res=0
#     try:
#         res=int(s)
#     except ValueError as e:
#         res=float(s)
#     except Exception:
#         raise
#     finally:
#         return res
# def calc(exp):
#     ss = exp.split('+')
#     ns = list(map(str2num, ss))
#     return reduce(lambda acc, x: acc + x, ns)
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
# main()
# ----------------断点---------------------------------------
# def A(val):
#     assert val!=0,'this is error'
#     r = 10 / int(val)
#     return r
# print(A(0))
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
# --------------------IO编程-----------------------------------
# f=open('./static/test.txt','r')
# print(f.read())
# f.close()
# try:
#     f=open('./static/test.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# with open('./static/test.txt','r') as f:
#     # print(f.read(10))
#     # print(f.readline(2))
#     # print(f.readlines())
#     for test in f.readlines():
#         print(test.strip())
# with open('./static/img.png','rb') as f:
#     print(f.read())
# with open('./static/test.txt','a',encoding='UTF-8') as f:
#     f.write('山东省')
#     f.write('济南市')
# --------------------StringIO和BytesIO-----------------------------------
# from io import StringIO
# f=StringIO()
# f.write('hello world')
# print(f.getvalue())
# from io import BytesIO
# f=BytesIO()
# f.write('山东省'.encode('UTF-8'))
# print(f.getvalue())
# from io import BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())
# -------------------------操作文件和目录------------------------------
import os
# print(os.name)
# print(os.uname())
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))
# print(os.path.join('F:\Desktop\python','spacefile'))
# os.mkdir('./spacefile')
# os.rmdir('./spacefile')
# print(os.path.split('./static/test.txt'))
# print(os.path.splitext('./static/test.txt'))
# a=[x for x in os.listdir('.') if os.path.isdir(x)]
# print(a)
# a = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# print(a)
# 作业
# def setdir(name):
#     for x in os.listdir(name):
#         names = name + '/' + x
#         if os.path.isdir(names):
#             for y in os.listdir(names):
#                 nameas = names + '/' + y
#                 if os.path.isdir(nameas):
#                     setdir(nameas)
#                 else:
#                     if os.path.splitext(nameas)[1] == '.py':
#                         print(os.path.abspath(nameas))
#         else:
#             if os.path.splitext(names)[1] == '.py':
#                 print(os.path.abspath(names))
# setdir('.')
# print(os.path.isdir('F:\Desktop\python\static\aaa'))
# print(os.path.isdir('./static/aaa'))
# print(os.path.abspath('./static/aaa'))
# -------------------序列化------------------------------------
# import pickle
# d = dict(name='张三', age=20)
# print(pickle.dumps(d))
# f = open('./static/dump.txt', 'wb')
# pickle.dump(d, f)
# f=open('./static/dump.txt', 'rb')
# d=pickle.load(f)
# f.close()
# print(d)
# d = dict(name='张三', age=20)
# A=pickle.dumps(d)
# B=pickle.loads(A)
# print(A)
# print(B)
# import json
# d = dict(name='ko', age=20)
# A=json.dumps(d)
# print(A)
# B='{"name":"zhangsan","age":20}'
# json.loads(B)
# print(B)
# class序列化
# import json
# class Student(object):
#     def __init__(self, name, age, context):
#         self.name = name
#         self.age = age
#         self.context = context
# def changeList(self):
#     return {
#         'name': self.name,
#         'age': self.age,
#         'context': self.context
#     }
# stu = Student('zhangsan', 20, 'this is context')
# print(json.dumps(stu, default=changeList))
# import json
# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=True)
# print(s)
# -------------------------------------------------------
# from multiprocessing import Process
# import os
# def Student(name):
#     print('this is father %s : %s;this is son %s' % (name, os.getpid(),os.getppid()))
# if __name__ == '__main__':
#     pro = Process(target=Student, args=('setStudent',))
#     pro.start()
#     pro.join()
# from multiprocessing import Pool
# import time, random, os
# def A(index):
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('线程:%s;用时:%s;ID:%s' % (index, end - start, os.getpid()))
# def B():
#     print('this is B')
# if __name__ == '__main__':
#     poo = Pool(5)
#     print(poo)
#     for i in range(6):
#         poo.apply_async(A, args=(i,))
#     poo.close()
#     poo.join()
# import subprocess
# fun=subprocess.call(['nslookup','www.python.org'])
# print(fun)
# ----------------------正则---------------------------------
# import re
# name='001-001-002'
# if re.match(r'^\d{3}\-\d{3}\-\d.',name):
#     print('ok')
# else:
#     print('no')
# str='a b   ;;,;  c d'
# print(str.split(' '))
# print(re.split(r'[\s\;\,]+',str))
# nub='001-12121212'
# names=re.match(r'^(\d{3})-(\d{3,8})$',nub)
# print(names)
# print(names.group(0))
# print(names.group(1))
# print(names.group(2))
# strs=re.match(r'^(\d+?)(0*)$','123123000').groups()
# print(strs)
# setR=re.compile('^(\d{3})(\d{3,8})$')
# print(setR.match('123456').groups())
# 作业邮箱验证
import re

# 一
# def is_valid_email(addr):
#     if re.match(r'^([0-9a-zA-Z\_\.]+)(\@)([a-z]+)(.com)$', addr):
#         print('OK')
#         return True
#     else:
#         print('Error')
#         return False
# is_valid_email('mr-bob@example.com')
# <Tom Paris> tom@voyager.org
# str=re.match(r'^(\<)([0-9a-zA-Z\_\.\s]+)(\>)([0-9a-zA-Z\_\.\s]+)(\@)([a-z]+)(.)(org|com)$', '<Tom Paris> tom@voyager.com').groups()
# print(str)
# def is_valid_email(addr):
#     if re.match(r'^(\<)([\w\.\s]+)(\>)([\w\.\s]+)(\@)([a-z]+)(.)(org|com)$', addr):
#         print(re.match(r'^(\<)([\w\.\s]+)(\>)([\w\.\s]+)(\@)([a-z]+)(.)(org|com)$', addr).group(2))
#         return True
#     elif re.match(r'^([\w\.\s]+)(\@)([a-z]+)(.)(org|com)$', addr):
#         print(re.match(r'^([\w\.\s]+)(\@)([a-z]+)(.)(org|com)$', addr).group(1))
#         return False
# is_valid_email('<Tom Paris> tom@voyager.com')
# -----------------------常用内建模块--------------------------------
from datetime import datetime, timedelta, timezone

now = datetime.now()
# print(now)
# date=datetime(2016,10,10,13,20,15)
# print(date)
# print(date.timestamp())
# tims=date.timestamp()
# print(datetime.fromtimestamp(tims))
# times=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
# print(times)
# times=now.strftime('%Y-%m-%d %H:%M:%S')
# print(times)
# print(datetime(2015, 5, 18, 16, 57, 3, 540997))
# print(now + timedelta(hours=10))
# print(datetime(2015, 5, 19, 2, 57, 3, 540997))
# print(now - timedelta(days=1))
# print(datetime(2015, 5, 17, 16, 57, 3, 540997))
# print(now + timedelta(days=2, hours=12))
# print(datetime(2015, 5, 21, 4, 57, 3, 540997))
# timezone(timedelta(hours=8))
# -----------------------collections--------------------------------
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
# Point=namedtuple('Point',['x','y'])
# p=Point(22,10)
# print(p.x)
# print(p.y)
# name=deque(['a','b','c'])
# print(name)
# name.append('x')
# name.appendleft('x')
# print(name)
# name.pop()
# name.popleft()
# print(name)
# data=defaultdict(lambda:'this is None')
# data['name']='张三'
# print(data['name'])
# print(data['age'])
# d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(d['a'])
# data=Counter()
# for i in 'evermationse':
#     data[i]=data[i]+1
#     print(data[i],'--',i)
# print(data)
# --------------------------itertool-----------------------------
# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# ns =itertools.takewhile(lambda x:x<10 ,natuals)
# print(list(ns ))
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)
# list=[]
# for i in itertools.chain('hello','world'):
#     list.append(i)
# print(list)
# for key,group in itertools.groupby('AAABBBCCCABC'):
#     print(key,'--',list(group))
# --------------------------urllib-----------------------------
# import urllib.request
# with urllib.request.urlopen('https://www.baidu.com') as f:
#     data = f.read()
#     # print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
# ----------------------pillow---------------------------------
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random


# img=Image.open('./static/img.jpg')
# w, h = img.size
# img.thumbnail((w/2, h/2))
# img.save('./static/thumbnai2.jpg', 'jpeg')
# img=Image.open('./static/img.jpg')
# imgF=img.filter(ImageFilter.BLUR)
# imgF.save('./static/ImageFilter.jpg', 'jpeg')
# 验证码
# def getStr():
#     return chr(random.randint(65, 90))
# def getColor1():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# def getColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# width = 240
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# fontS = ImageFont.truetype('./static/arial.ttf', 36)
# draw = ImageDraw.Draw(image)
# for i in range(width):
#     for j in range(height):
#         draw.point((i, j), fill=getColor1())
# for a in range(4):
#     draw.text((60 * a + 10, 10), getStr(), font=fontS, fill=getColor2())
# images = image.filter(ImageFilter.BLUR)
# images.save('./static/font.jpg', 'jpeg')
# -------------------------requests------------------------------
# import requests
#
# data = requests.get(
#     'https://www.baidu.com',
#     params={'name': 'json', 'age': 20},
#     # headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
# )
#
# data.encoding='utf-8'
# print(data.text)
# strhtml=data.content
# htmls=str(strhtml,'utf-8')
# print(htmls)
# print(data.url)
# print(data.encoding)
# print(data.text)
# print(data.content)
# print(data.json())
# import requests
# data = requests.post(
#     'https://www.baidu.com',
#     # json={'name': 'json', 'age': 20},
#     files={'file':open('abc.txt','rb')}
# )
# data.encoding='utf-8'
# print(data.text)
# data=requests.get('https://www.baidu.com')
# data.encoding='utf-8'
# print(data.text)
# ---------------------chardet----------------------------------
# import chardet
# str=chardet.detect(b'hello world')
# print(str)
# name='山东省济南市'.encode('gbk')
# str1=chardet.detect(name)
# print(str1)
# ----------------------psutil---------------------------------
# import psutil
# cpu=psutil.cpu_count()
# cpu1=psutil.cpu_count(logical=False)
# print(cpu1)
# cpuTime=psutil.cpu_times()
# print(cpuTime)
# for i in range(10):
#     cpuF=psutil.cpu_percent(interval=1,percpu=True)
#     print(cpuF)
# print(psutil.virtual_memory())
# print(psutil.swap_memory())
# print(psutil.disk_partitions())
# print(psutil.disk_usage('/'))
# print(psutil.disk_io_counters())
# print(psutil.net_io_counters())
# print(psutil.net_if_addrs())
# print(psutil.net_if_stats())
# print(psutil.net_connections())
# print(psutil.pids())
# pro=psutil.Process(3372)
# print(pro.name())
# print(pro.exe())
# print(pro.cwd())
# print(pro.cmdline())
# print(pro.ppid())
# print(pro.parent())
# print(pro.status())
# print(pro.username())
# print(pro.create_time())
# print(pro.terminal())
# print(pro.cpu_times())
# print(pro.memory_info())
# print(pro.open_files())
# print(pro.connections())
# print(pro.num_threads())
# print(pro.threads())
# print(pro.environ())
# print(pro.terminate())
# --------------------图形-----------------------------------
# from tkinter import *
# import tkinter.messagebox as messagebox
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()
# ---------------------海龟绘图----------------------------------
# import turtle
# turtle.width(10)
#
# turtle.pencolor('red')
# turtle.forward(200)
# turtle.right(90)
#
# turtle.pencolor('red')
# turtle.forward(200)
# turtle.right(90)
#
# turtle.pencolor('red')
# turtle.forward(200)
# turtle.right(90)
#
# turtle.pencolor('red')
# turtle.forward(200)
# turtle.right(90)
#
# turtle.done()
# import turtle
#
# def drawStar(x, y):
#     turtle.pu()
#     turtle.goto(x, y)
#     turtle.pd()
#     # set heading: 0
#     turtle.seth(0)
#     for i in range(5):
#         turtle.fd(40)
#         turtle.rt(144)
#
# for x in range(0, 250, 50):
#     drawStar(x, 0)
#
# turtle.done()
# import turtle
#
# # 设置色彩模式是RGB:
# turtle.colormode(255)
#
# turtle.lt(90)
#
# lv = 14
# l = 120
# s = 45
#
# turtle.width(lv)
#
# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# turtle.pencolor(r, g, b)
#
# turtle.penup()
# turtle.bk(l)
# turtle.pendown()
# turtle.fd(l)
#
# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = turtle.width()
#
#     # narrow the pen width
#     turtle.width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     turtle.pencolor(r % 200, g % 200, b % 200)
#
#     l = 3.0 / 4.0 * l
#
#     turtle.lt(s)
#     turtle.fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     turtle.bk(l)
#     turtle.rt(2 * s)
#     turtle.fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     turtle.bk(l)
#     turtle.lt(s)
#
#     # restore the previous pen width
#     turtle.width(w)
#
# turtle.speed("fastest")
#
# draw_tree(l, 4)
#
# turtle.done()
# -----------------------web--------------------------------
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


from wsgiref.simple_server import make_server

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
