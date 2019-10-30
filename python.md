## 语法基础 ##
#### 变量 ####
- 变量不用定义，直接声明使用  
	name='hello'
- 可以连续赋值   
	name=name1='hello'   
- 赋值方式2  
	a,b,c='山东省','济南市','历下区'  
- 作用域
	- 由范围限制
	- 分为两类
		- 全局(global)：在函数外部定义
		- 局部(local)：在函数内部定义
	- 变量的作用范围
	- 在函数外边定义的变量在函数内部可以访问，但是在函数内部调用之后又定义声明了一下全局变量，这里就会报错，问题是变量提升
	<pre>
	a=100
	def fun():
	    print(a)
	    a=200
	    print(a)
	fun()
	</pre>
	- 提升局部变量为全局变量
		- 用global,这里注意在函数外边调用函数内部的全局变量的时候，需要先执行函数，才能调到函数内部的全局变量
			<pre>
			def fun():
			    global a
			    a=10
			    print(a)
			fun()
			print(a)
			</pre>
	- globals,locals函数
		- 可以用globals和locals显示出全局变量和局部变量,用法如下  
		<pre>
		def fun():
		    global a
		    a=10
		    print(a)
		    print(globals())
		    print(locals())
		fun()
		print(a)
		</pre>
	- eval()函数
		- 把一个字符串当做一个表达式来执行
		<pre>
		a=10
		b=10
		c=eval('a+b')
		print(c)
		</pre>
	- exec和上边的eval功能相似，但是没有返回结果exec内部放置的是函数体
		<pre>
		a=10
		b=10
		d=exec('print(a+b)')
		</pre>
#
#####  变量类型  #####
- 数字Number  
	- 数字没有大小限制
	- 正数，负数，0
	- 二进制  
		- 0b开头 例如0b0010
	- 八进制  
		-0o 开头
	- 十六进制  
		- 0x开头
	- 浮点数  
		- 小数 0.5,0.45
		- 科学计数法 5e-10 print(250) print(2.5e2)
		- 复数 a+bi
	- 布尔值
		- 表示真假
		- True/False
		- 当数字使用 True=1 False=0 print(100+True)值为101
		- 除了0以外的都是True
	- 类型转换
		- int(text)把字符串转为Number类型
- 字符串类型str
	- 用单双引号
	- 三引号 保持字符串的格式 可以换行
	- 转义字符、格式化
		- 转义字符  \ 转义字符不同系统有不同的表示方法
		- 格式化  
			- 传统格式化（不提倡使用）（显示小数点后几位用 %.2f为显示小数点后两位）  
			**print('number:%d,age:%d,name:%s'%(10,20,'张三丰'))**
			- format 用函数形式格式化  
			**print('number:{0},age:{1},name:{2}'.format(10,20,'张三丰'))<br>
			print('number:{},age:{},name:{}'.format(10,20,'张三丰'))**
				- 如果没有不写下标，format中的数据的个数要和字符串中的要传入的参数对应起来
				- 使用命名参数  
			**print('number:{num},age:{age},name:{name}'.format(num=15,age=20,name='张三'))**
				- 有浮点小数的写法  {:.2f}
			**print('number:{:.2f},age:{:.2f},name:{}'.format(5.265,20.336,'张三丰'))**
			- 解包操作  \*\*b  
			**a='number:{num},age:{age},name:{name}'<br>
			b={"num":15,"age":20,"name":'张三'}<br>
			print(a.format(\*\*b))**  
			这里是把b对象{}转为()，在b对象的前边用两个星号**
	- 空字符串为False，非空的字符串为True
	- 内置函数  
		- find()如果不存在返回一个-1
		- index()如果不存在返回一个错误
		- s.find(s,25)为在25的位置开始查找  
	**print('hello world'.find('world'))<br>
	print('hello world'.index('world'))**
		- 判断类函数
			- 一般用is开头
			- isalpha判断是会否是字母，如果没有返回False
			- 数字建议用正则表达式
			- islower判断是都是大小写
			- 内容判断类
				- startswith/endswith判断是否已xxx开头或是以xxx结尾
				- suffix被检查的字符串，必须有
				- start开始
				- end 结束  
				**print('hello world'.startswith('hello'))<br>
				print('hello world'.endswith('hello'))**
		- 操作类
			- format格式化使用
			- strip用于删除开头和结尾的空格  
				- strip('A') 清楚字符串中的开头的A和结尾的A
				- lstrip 只操作左边
				- rstrip 只操作右边
			**print(name.strip())**
			- join 拼接字符串  
			**name1='hello'<br>
			name2='$'<br>
			print(name2.join(name1))**
		- type用于查看变量的类型  
		**type(name)**    
	- 字符串补充
		- 格式化
		<pre>
		name='hello {} world {}'
		name1='hello {1} world {0}'
		name2='hello {user} world {age}'
		print(name.format('张三',40))
		print(name1.format('张三',40))
		print(name2.format(user='张三',age=40))
		</pre>
- None类型
	- 用来占位置
	- 返回表示一个空
- 列表list
	- 一种数据类型，就是数组
	- 可以不是一类数据类型
	- 创建list
		- L=[2,3,6]
		- L=list()
		- 查看类型用type(L)
	- 列表的常见操作
		- 访问 
			- 使用下标  
			- 访问的下标超标 返回indexError  
			**L=[2,3,6,2,6,66,66,55]<br>
			print(L[0])**
		- 切片操作
			- 队列表中的某一段进行截取
			- 左包括右不包括
			- L[a:b]从a截取到b，返回一个新的数组  
			**L=[2,3,6,2,6,66,66,55]<br>
			print(L[1:3])**
			- 切片控制的长度（就是跨越几个）
				- print(L[::1])跨越1个
				- print(L[::2]])跨越2个
				- ......
		- id用于判断两个数组是否是同一个数组，这个id是内存中开辟空间的id  
		**L=[2,3,6,2,6,66,66,55]<br>
		print(id(L))**
		- 下标为负数
			- 下标为负数是从最后一个开始往前数
			- 切片的步长为负数是从最后一个往前走
		- 切片和步长和下标为负数的整体使用
			- print（L[-5:-2:1]）从-5位置开始到-2位置，步长为1
			- print(L[-2,-5:-1])从-2位置开始到-5位置，步长为-1，就是到这读取获取数据
		- 获取数组的长度
			- `__len__()`
				<pre>list.__len__()</pre>
			- len()
				<pre>len(list)</pre>
		- 数组循环补充
			- 颗粒循环
			<pre>
			l=[['hello','a',1],['world','b',2]]
			for v,k,s in l:
			    print(v,k,s)
			</pre>
		- 增加元素
			- append()在结尾增加元素 L.append('hello')
			- insert()在自定义的位置中插入L.insert(3,'hello')
			- extend()把一个元素列表插入到另外的一个元素列表中 A.extend(B),把B插入到A元素的中(A元素的尾部)
			- 使用+号使两个数组连接起来
				<pre>
				a=[1,2,3]
				b=[4,5,6]
				c=a+b
				print(c)
				</pre>
		- 删除元素
			- pop()删除指定下标的元素 L.pop(num) num为下标 
			- remove()删除指定元素的 L.remove(num) num为元素
			- del删除指定元素或是指定片段的中元素
				- del L[num]num为下标
				- del L[a:b]a到b指定片段
			- clear清空，清空后的id在内存中是不变的
				- list.clear()
		- 数组翻转
			- list.reverse()
		- count查找list中的某个元素的个数
			- list.count(10)
		- copy拷贝，浅拷贝
			- list中的list的在内存中的地址是一样的
		<pre>
		l=[2,3,6,4,566,2]
		a=l.copy()
		print(id(a))
		print(id(l))
		</pre>
		<pre>
		l=[1,2,3,[5,6,7]]
		a=l.copy()
		print(id(l))
		print(id(a))
		print(id(l[3]))
		print(id(a[3]))
		</pre>
	- 列表内涵 list content
		- 通过简单的方法创建列表
		- 可以进行简单的循环筛选
		<pre>
		l=[2,4,6,7,8]
		a=[i for i in l]
		print(a)
		</pre>
		<pre>
		l=[i for i in range(0,15) if i%2==0]
		print(l)
		</pre>
- 元素tuple
	- 可以理解成是一个不更改的列表
	- 元素可以是任何类型
	- 元素可以相加  
	- tuple的创建
		- T=() 直接用（）
		- T=(100,) 括号中有一个值的时候，需要加上一个逗号，用于区分类型，是一个特例，两个元素以上的就不许要
		- T=100, 直接用逗号
	- list转为tuple  
		**L=[26,3,63,6,'hello']<br>
		T=tuple(L)<br>
		print(T)**
	- 有序
		- T[0]取值和list是一样的
		- 切片和list是一样的
		- 可以访问不可以修改
	**A=(100,22,0,11,1)<br>
	B=('hello','world')<br>
	C=A+B<br>
	print(C)**
	- 元素相乘（就是把元素复制）  
	**t=(1,3,6)<br>
	tt=t\*2<br>
	print(tt)**
	- 成员检测  
		if a in b:
	- 元祖遍历  
		for i in T:
	- 元祖嵌套  
		T=(1,(2,3))  
		嵌套的元祖循环  
		for i,j,k in T:  
		这里的i,j,k对应的是元祖中的第一个第二个第三个
	- 常用元祖函数
		- len 长度 print(len(t))
		- max求最大值 print(max(t))
		- min最小值、
		- count对元素计数 count(1)有几个1
		- index某一个元素所在的位置 T.index(1)1所在的位置
		- 特殊用法 a,b=b,a把a和b的值互换		
- 字典dict
	- 字典是一种组合数据，没有顺序的组合数据，数据以键值对的形式出现
	- 字典的声明方式(就是对象)
		<pre>
		a={'name':"张三",'age':20}
		b=dict({'name':"张三",'age':20})
		c=dict(name="张三",age=20)
		d=dict([('name','张三'),('age',20)])
		print(a)
		print(b)
		print(c)
		print(d)
		</pre>
	- 字典是序列类型，但是是无序的，没有分片和索引
	- 内容是以键值对的方式存在
	- 字典的常用操作
		- 访问数据
		<pre>
		d={'name':1,'age':2}
		print(d['name'])
		</pre>
		- 赋值操作
		<pre>
		d={'name':1,'age':2}
		d['name']='张三'
		print(d)
		</pre>
		- 删除某个元素del
		<pre>
		d={'name':1,'age':2}
		del d['age']
		print(d)
		</pre>
		- 检查成员（检测的是键值）
			- in，for in
			<pre>
			d={'name':1,'age':2}
			if 'name' in d:
			    print(d['name'])
			if 'www' not in d:
			    print('no')
			</pre>
		- 遍历的循环在2和3中的代码是不通用的
			- for a in d
			- for a in d.keys() 键名循环
			- for a in d.values()键值循环
			- for a,b in d.items()键值对循环，特殊使用
			<pre>
			d={'name':1,'age':2}
			for a in d:
			    print(a,d[a])
			for a in d.keys():
			    print(a)
			for a in d.values():
			    print(a)
			for a,b in d.items():
			    print(a,b)
			</pre>
	- 字典生成式
		<pre>
		d={'name':1,'age':2}
		dd={k for k in d.items()}
		print(dd)
		ddd={k for k in d}
		print(ddd)
		</pre>
	- 字典的相关函数
		- 通用函数len,max,min,dict
		- str:返回字典的字符串格式
		- clear：清空字典
		- items：返回字典的键值对组成的元素格式
		- keys()键名
		- values()键值
		- get:通过键名获取键值
		- formkeys:根据键名生成键值
		<pre>
		print(str(d))
		print(type(d.items()))
		print(d.keys())
		print(d.values())
		print(d.get('name'))
		#fromkeys的用法
		l=['hello','world','shandong ']
		dd=dict.fromkeys(l,'济南')
		print(dd)
		</pre>
- 集合set
	- 和数学的集合一样
	- 内容无序+内容不重复（默认去掉重复的）
	- 创建set()
		- s=set(list)创建的对象中的内容只能有一个变量，这里不能往里边添加内容
		- 使用大括号 s={1,2,3,6,1,6}
	- 集合的操作
		- in操作 if num in s:
		- for循环 for i in s:
		- 集合的另外一种遍历方法 for i,j,k in s:  {(1,2,3),(),()},对应的tuple中的第一个，第二个，第三个
	- 集合的生成式  
		s={i for i in sa}  
		s={i for i in sa if i%2==0}
		a={i*2 for i in s}
		a={n*m for n in s for m in s}
	- 集合的内置函数
		- len长度
		- max/min
		- add往集合中添加内容
		- clear清空
		- remove/discard删除  
			- set.remove(num)num是值,删除的值如果有不存在会报错
			- discard用法同上，删除的值如果不存在是不报错的
		- pop删除的内容是随机的
	- 集合的数学操作
		- intersection 求交集  
		**a={1,2,3,4,5,6}<br>
		b={7,8,9,4,5,6}<br>
		print(a.intersection(b))**
		- 求差集 difference  
		**a={1,2,3,4,5,6}<br>
		b={7,8,9,4,5,6}<br>
		print(a.difference(b))**
		 注意：a交b的差集(a-b)和b交a的差集(b-a)不一样
		- 并集 union  
		**a={1,2,3,4,5,6}<br>
		b={7,8,9,4,5,6}<br>
		print(a.union(b))**
		- issubset检查一个集合是否是另一个子集
		- issuperset检查一个集合是否是另一个集合的超级
	- frozenset冰冻集合
		- 集合不能进行任何操作
- map
### 表达式 ###
		a=1+2
### 运算符 ###
		加、减、乘、除、赋值、位运算  
### 算数运算符   ###
- 用来进行算数运算的符号
-  表示加减乘除
-  没有自增自减
-  /为除法 //为除法取整数 print(9/2) print(9//2)
	- 正数除以负数求余：证书除以负数后得到的负小数取消数整数，然后用除数减去取得的值乘以被除数后的值为余数  
	  `例如 9%-4 为9//-4等于-3，然后9-((-3)*(-4))=-3 所以9%-4的余数为-3`
-  比较运算符
	- 大于、大于等于、小于、小于等于
	- 结果是一个布尔值
	- a的4次幂的写法为a**4
-  赋值运算符
	- 就是等号
-  逻辑运算符
	- 对布尔值进行运算的符号
	- and逻辑与
	- or逻辑或
	- not逻辑非，就是取反
	- 没有亦或
	- 短路问题，知道结果后不再往下运行，直接把结果返回出来
	- 字符串乘以数字是吧字符串重复多少遍的意思
-  成员运算符
	- 用来检测一个值或是变量是否在某个集合里边
	- in 成员运算符
	- not in 不在里边的意思  
	**a=10
	c=[2,3,61,10]<br>
	b=a in c<br>
	print(b)**
-  身份运算符
	- 用来确定两个变量是否是同一个变量
	- is 变量运算符
	- is not 不是  
	- 这里的是地址中的内存用同一个为True,[-5,256]中的相同的数字用同一个内存
	**a=10<br>
	b=20<br>
	print(a is b)**
-  运算符的优先级问题
	-位运算 >> << 右移 左移
### 程序结构 ###
- 三种结构
	- 顺序
	- 循环
	- 分支
### 分支结构 ###
- 分支结构基本语法
	- if语句
	- while语句
	- input的作用
		- 在屏幕上输出括号你内的字符串
		- 接受用户输入的内容并返回带程序
		- input返回的内容一定是字符串类型
		**a=input()<br>
		if a=='man':<br>
		print('男生')<br>
		else:<br>
		print('女生')**  
		*--------------------------------------*  
		**text=input('成绩输入')<br>
		if int(text) > 90:<br>
		    print('成绩优秀')<br>
		else:<br>
		    print('成绩较差')**
### 多路分支 ###
- if 条件:	elif 条件:  else:
- if嵌套使用
- 没有switch语句 
### 循环语句 ###
- for循环
	- for 变量 in 序列：  
	**for i in range(10):<br>
    print(i)**
	- for-else语句执行完for语句后可以执行一个else语句用于结尾  
		**for i in range(10):<br>
		    print(i)<br>
		else:<br>
		    print('is none')**
- while循环
	- 条件成立执行循环
	- 另外一种表达式 while 条件:    else:
	**a=0<br>
	while a<6:<br>
	    print(a)<br>
	    a+=1<br>
	else:<br>
	    print('over')**
- 停止循环
	- break 整个循环结束
	- continue	跳出当前循环，执行后边的循环
	- pass 不做任何操作，当做占位符使用(if条件中必须要有语句，可以用pass作为占位符)
- 生成序列range
	- range(10)生成一个0到10的数字
	- range(1,10)生成一个1到10的数字
	- 左包括右不包括
	- randint是个特例
### 函数 ###
- 自定义函数
- 形参 没有值，用于占位
- 实参 调用的时候实际输入的值
- print("{0} asdf".format(val))
- 函数执行完默认会返回一个return None
- help获取函数的文档，help(print)  
###### 例子 ######
    for i in range(1,10):
    	for j in range(1,i+1):
    		print("%d*%d=%d"%(i,j,i*j),end=" ")
   		 print()
#### 参数详解 ####
- 参数分类
	- 普通参数/位置参数  
		 **def name(a,b,c):<br>
   		 print(a,b,c)**
	- 默认参数  
		**def name(a,b,c=10):<br>
   		 print(a,b,c)**
	- 关键字参数  
		**def name(a,b,c):<br>
		print(a,b,c)<br>
		name(a=1,b=2,c=3)**
	- 收集参数
		- 把没有位置，不能和定义时的参数位置相对应的参数，放入一个特性的数据结构中
		- 语法 def fun(*args)
		- 收集参数可以和其他的类型参数共存
		- 一般在不确定参数的情况下使用收集参数
		<pre>
		def fun(*args):
		    list=args
		    for item in list:
		        print(item)
		fun('张三',40,'man')
		</pre>
		- 收集参数之关键字收集参数
			- 简言之就是对象
			- 传入的参数是不确定的
			- 传入的参数要有键名键值
			- 例子
			<pre>
			def fun(**args):
			    print(args)
			    for item in args:
			        print(item,args[item])			
			fun(name='张三',age=40,sex='man')
			</pre>
	- 各种参数整体使用
		- 传入参数的顺普通参数、收集参数、关键字参数、收集参数关键字参数
	<pre>
	def fun(name,age,*args,aaa='空',**kwargs):
	    print(name)
	    print(age)
	    print(aaa)
	    print(args)
	    print(kwargs)
	fun('张三',40,'小红','小刚','小李',aaa='内容',user='adf',sex='man')
	</pre>
#### 递归函数####
- 函数调用自身
- 递归函数有一个深度，这个深度跟电脑的自身配置有关系
#### 函数文档 ####
- 函数的文档的作用是对当前函数提供使用相关的参考信息
	- 函数文档一般用于help进行查看
	- 使用stu。__doc__
	- 函数的文档定义 一般用''' 内容 '''
	<pre>
	def stu(name,age):
    '''
    参数定义
    :param name:姓名 
    :param age: 年龄
    :return: 
    '''
    return 1
	</pre>
#### 面向对象 OOP####
- 常用名词
	- OO：面向对象
	- OOA：分析
	- OOD：设计
	- OOP：编程
	- OOI：实现
	- OOA->OOD->OOI
- 类和对象
	- 类描述的是集合（如：学生）
		- 动作，函数
		- 属性，变量
	- 对象描述的是个体 （如：张三，有各种属性）
	- 类是描述集合，对象是集合中的个体，属性是描述个体的特征，方法是描述个体的动作或是事件
	- is-a
	- 定义类：class  
	<pre>
	class Student():
		pass
	</pre>
	- 类的介绍
		- 类就是对象
		- 用点调用方法或是属性
		- 检查类的所有成员
			- class_name.\_\_dict\_\_
			<pre>
			class Student():
			    name=None
			    age=18
			    def fun(self):
			        print('hello world')
			        return None
			student=Student()
			print(Student.\_\_dict\_\_)
			</pre>
		- 检查所有成员要用\_\_class_name\_\_,不能是实例化后的对象
		- 实例化后的对象，只是访问的时候，在内存中的地址和没有实例化之前的地址是一样的
		- 实例化后重新对类的成员进行重新赋值，这个值会保存到实例化的对象中，并不会改变类中的属性的值
		- 类多次实例化，是把每个实例化的对象创建一个新的对象，每个实例化的对象相互不影响
		- 类中的self和JavaScript中的this是一样的，表示对象本身
		- 类中嵌套字典的使用
		<pre>
		class Student():
		    infor={
		        'user':'',
		        'age':10
		    }
		    def fun(self):
		        self.infor['user']='adsfasdf'
		        print(self.infor['user'])
		stu=Student()
		stu.fun()
		</pre>
		<pre>
		class Student():
		    name=''
		    def __init__(self,user):
		        self.name = user
		        print('*****',id(user))
		    def fun(self):
		        print(self.name)
		        return None
		a=Student('张三')
		b=Student('李四')
		a.fun()
		b.fun()
		print(id(a.name))
		print(id(b.name))
		</pre>
	- 例子  
	    <pre>
		class Setname():
		    name='张三'
		    age='40'
		    def fun(self):
		        print(self.name)
		        return None
		getName=Setname()</pre>
	- 类的属性
	- 方法中的self
		- 指代本身
		- 不是关键字
		- 调用该方法的时候不需要传
	- 类的变量的作用域的问题  
		- 实例属性如果不存在则访问类的属性
	- 访问类的属性
		- 类里边如果强制访问类的属性，要用\_\_class__
		- 类方法，里边没有self
		- 不定义self无法访问类的属性
			- 想要访问类的属性，使用类名，间接指代
			<pre>
			class SetAge():
			    name='李四'
			    age=20
			    def fun():
			        print(SetAge.name)
			        return None
			setage=SetAge()
			SetAge.fun()
			</pre>
			- 用\_\_class__访问,间接指代  
			<pre>
			class SetAge():
			    name='李四'
			    age=20
			    def fun01():
			        print(__class__.name)
			        return None
			setage=SetAge()
			SetAge.fun01()
			</pre>
		- 调用类的属性和方发
			- 实例化后再调用类的属性和方发
			- 直接调用类的属性Student.fun()
				- 如果这个方法中没有参数(self)，或是没有用到参数，可以直接调用，不会把报错
				- self和\_\_class__，self指向的是当前类的属性，class指向类中初始值的属性的值
				- 如果这个方法中有参数(self),在调用的时候也可以直接调用，但是要传入参数(self),但是这里如果传入随意的参数会报错，可以传入stu=Student()实例化后的stu，也可以传入一个新的类，但是类中的属性或是方法在这个新的类中都要有。这种类型称为鸭子模型
				<pre>
				class Student():
				    name='张三'
				    def fun(self):
				        self.name='hello'
				        print(self.name)
				    def aa(self):
				        print(__class__.name)
				    def ab():
				        print('this is no value')
				    def ac(self):
				        print(self.name)
				stu=Student()
				stu.fun()
				Student.fun(stu)
				Student.ab()
				class A():
				    name='山东省济南市'
				Student.ac(A)
				</pre>
				- 类中的方法有属性的值的设置的时候，在方法执行完成后，整个类中的属性值也会发生变化
				<pre>
				class Student():
				    name='张三'
				    def fun(self):
				        self.name='hello world'
				        print(self.name)
				    def aa(self):
				        print(self.name)
				st=Student()
				st.aa()
				st.fun()
				</pre>
- 构造函数
	- 类的实例化的时候执行初始化的工作
	- 使用特殊的名称和写法  
		<pre>
		def __init(self)__:
			pass
		</pre>
	- 构造函数是在实例化的时候自动执行的
	- 构造函数内部不能直接访问类内部构造函数外部的变量，但是可以方位类的外部的变量
- 继承
	- 继承
		- 子类可以使用父类的内容和行为
		- 继承的实现
			- 父类，基类，超类：被继承的类，Base Class，Super Class
			- 子类：有继承行为的类
		- 所有的类都必须有父类
			- 如果没有，默认给一个object的子类
			- print(issubclass(Parse,object))object是最外成的父类
		- 如果继承的子类中的变量和父类中的变量存在冲突的时候优先使用子类的变量
		- 子类如果想扩充父类的方法，可以在定义的新方法中调用父类的方法进行重用，也可以用super().父类成员
			<pre>
			class Parse():
			    name = '李四'
			    def setName(self):
			        print('this is parse fun')
			class Son(Parse):
			    name='www.baidu.com'
			    age='20'
			    def setNames(self):
			        self.setName()
			        print('this is son fun')
			son=Son()
			son.setNames(),
			</pre>
			- 第二种写法
			<pre>
			class Parse():
			    name = '李四'
			    def setName(self):
			        print('this is parse fun')
			class Son(Parse):
			    name='www.baidu.com'
			    age='20'
			    def setNames(self):
			        Parse.setName(self)
			        print('this is son fun')
			son=Son()
			son.setNames()
			</pre>
			- 用super()
			<pre>
				class Parse():
				    name = '李四'
				    def setName(self):
				        print('this is parse fun')
				class Son(Parse):
				    name='www.baidu.com'
				    age='20'
				    def setName(self):
				        super().setName()
				        print('this is son fun')
				son=Son()
				son.setName()
			</pre>
		- issubclass 验证两个类是否是父子关系
		- 子类没有构造函数会自动继承父类的构造函数
		- 多继承
			- 两个类可以让子类同时继承
			- 子类同时继承的两个类不能是父子类
			- 被继承的两个类可以是同时继承的父类的兄弟类
			- 子类可以同时继承两个父类，但是如果父类中的变量存在相同的，则取第一个
			<pre>
			class Person():
			    name='张三'
			class Student01(Person):
			    age01=10
			class Student02(Person):
			    age02=20
			class me(Student01,Student02):
			    def fun(self):
			        print(self.name)
			        print(self.age01)
			        print(self.age02)
			        return None
			m=me()
			m.fun()
			</pre>
		- 代码案例
		<pre>
       	class Person():
		    name='person'
		class Student(Person):
		    def fun(self):
		        print(self.name)
		        return None
		class Teacher(Person):
		    age=10
		    def fun(self):
		        print(self.name)
		        return None
		class Sex():
		    sex='man'
		class me(Person,Sex):
		    def fun(self):
		        print(self.name)
		        print(self.age)
		        return None
		teacher=Teacher()
		teacher.fun()
		print(issubclass(Student,Person))
        </pre>
		- 构造函数的继承
			- 构造函数默认是自动继承的
			- 如果构造函数中有需要传递参数的，在继承的子类需要把参数传递进去
			- 构造函数的默认参数self必须要有
			- 代码案例
			<pre>
			class Person():
			    def __init__(self,name,age):
			        print(name,age)
			class Student(Person):
			    pass
			student=Student('张三',20)
			</pre>
		- 继承变量函数的查找顺序问题
			- 优先查找自己的变量
			- 没有则查找父类
			- 本类中如果没有构造函数，则自动查找父类的构造函数
		- 构造函数
			- \_\_init__(self)
			- 构造函数的写法是固定的
			- 实例化的时候自动执行，无需调用
			<pre>
			class Dog():
			    def __init__(self):
			        print('this is dog')
			        return None
			dog=Dog()
			</pre>
			- 如果本类中没有构造函数则向上查找
			<pre>
			class Animal():
			    def __init__(self):
			        print('this is animal')
			class Dog(Animal):
			    def __init__(self):
			        print('this is dog')
			        return None
			class Cat(Animal):
			    pass
			dog=Dog()
			cat=Cat()
			</pre>
			- 构造函数中如果有参数，则需要在实例化的时候传递
			<pre>
			class Animal():
			    def __init__(self):
			        print('this is animal')
			class Dog(Animal):
			    def __init__(self,name):
			        print('this is dog',name)
			dog=Dog(20)
			</pre>
			- 父类的所有成员
				- A.\_\_mor__
	- 单继承多继承
		- 单继承
			- 只能有一个父类
			- 使用较多
			- 但是功能不能无限扩展
		- 多继承
			- 可以继承多个父类
			- 不太建议使用
			- 类的功能扩展方便
			- 继承关系混乱
		- 继承表
			- MRO是继承的父子多层的关系
			- python采用c3算法
		- 继承的构造函数，需要注意的是如果父类的构造函数需要传参数，如果不传参会报错
		- 使用super调用父类中的构造函数
		- 构造函数继承(就是有一部分功能在父类的构造函数中已经实现了，现在只需要继承过来)
			- 直接继承
			<pre>
			class A():
			    def __init__(self):
			        print('this is A')
			class B(A):
			    def __init__(self,name):
			        print('this is B',name)
			class C(B):
			    def __init__(self,name):
			        B.__init__(self,name) #用B.__init__()
			        print('this is C')
			c=C('CCCC')
			</pre>
			- 拓展父类的构造函数，使用super继承
			<pre>
			class A():
			    def __init__(self):
			        print('this is A')
			class B(A):
			    def __init__(self,name):
			        print('this is B',name)
			class C(B):
			    def __init__(self,name):
			        super(C,self).__init__(name)
			        print('this is C')
			#在调用的时候传参
			c=C('张三')
			</pre>
			<pre>
			class A():
			    def __init__(self):
			        print('this is A')
			class B(A):
			    def __init__(self,name):
			        print('this is B',name)
			class C(B):
			    def __init__(self):
			        # 在继承构造函数的时候继承
			        super().__init__('李四')
			        print('this is C')
			c=C()
			</pre>
			上边两种方法区别是怎么传参的问题
		- 构造函数中一般是用于初始化的作用
	- 封装
		- 对对象的成员进行访问限制
		- 三个级别
			- 公开 public
			- 受保护的 protected
			- 私有的private
			- public、protected、private不是关键字
		- 访问限制在python中更像是一种思想
		- 私有
			- 在当前的类中或是对象中访问
			- 私有变量的定义 __name,在属性前边加上两个下划线
			<pre>
			class Student():
			    name = 'hello world'
			    __age=20
			    def fun(self):
			        print(self.name,self.__age) #只有在类的内部才能使用
			st=Student()
			st.fun()
			print(st.name)
			print(st.__age) #访问不到
			</pre>
			- 私有不是真正的私有，如果要访问私有属性的方法
				- 检查类成员
				- 调用
				<pre>
				class Student():
				    name = 'hello world'
				    __age=20
				    def fun(self):
				        print(self.name,self.__age)
				st=Student()
				print(Student.__dict__) #检查成员
				print(st._Student__age)	#访问私有属性__age			
				</pre>
			- 在成员内部可以访问，在外部不行
	- 多态
		- 多态就是在同一个对象中不同的情况表现出的不同的状态
		- 不是语法，是一种设计思想
		- Mixin设计模式
			- 主要采用多继承对功能的扩展
			- 必须表示某一个单一的功能，
			- 简单来讲就是方法父子类中的方法是一样的，表示单一功能（就是多继承）
	- 类的相关函数
		- issubclass，用于判断类的父子关系
		<pre>
		class Fash(Person):
		    def run(self):
		        print('鱼在游.....')
		class FashA(Fash):
		    print('this is fasha')
		print(issubclass(FashA,Fash))
		</pre>
		- isinstance()，用于判断一个对象是否是一个类的实例
		<pre>
		class Fash(Person):
		    def run(self):
		        print('鱼在游.....')
		class FashA(Fash):
		    print('this is fasha')
		fly = Fly()
		fash = Fash()
		print(issubclass(FashA,Fash))
		print(isinstance(fashA,Fash))
		</pre>
		- hasattr，检测一个对象时候有某个成员,检测的成员要用引号
		<pre>
		class Fash(Person):
		    def run(self):
		        print('鱼在游.....')
		class FashA(Fash):
		    print('this is fasha')
		fly = Fly()
		fash = Fash()
		print(hasattr(fash,"run"))
		</pre>
		- setattr设置成员对象
		- getattr获取成员对象
		- delattr删除成员对象
		- dir获取对象的成员列表
	- 类的成员检测符
		- 类的成员属性就是对类的某些属性进行一定的操作
			<pre>
			class Student():
			    name='张三'
			    def __init__(self):
			        self.setName()
			    def setName(self):
			        print(self.name)
			s=Student()
			</pre>
			- 简单讲就是在构造函数中执行对某些属性操作的方法
			- get获取属性的操作
			- set修改或是添加属性的操作
			- delete删除属性操作
		- 使用类的成员描述符
			- 使用类实行
			- 类的属性
			- 使用property函数
				- property(fget,fset,fdel,doc)
				- 使用方法
				<pre>
				class Person():
				    def fget(self):
				        print('this is fget',self._name)
				        return self._name
				    def fset(self,name):
				        self._name=name
				        print('this is fset',name)
				    def fdel(self):
				        self._name='NoneName'
				        print('this is fdel')
				    name=property(fget,fset,fdel,'this is doc')
				p=Person()
				p.name='张三'
				print(p.name)
				</pre>
				参数解析：对于传入的参数只能透过fset进行设置，获取的fget是不能传入参数的，只能获取数据和返回，fdel是执行的对参数或是变量的结尾操作
		- 类的内置属性
			- \_\_dict__ 以字典的方式显示类的成员组成
			- \_\_doc__获取类的文档信息
			- \_\_name__获取类的名称，如果在模块中使用获取的是模块的名称
			- \_\_bases__获取某个类的所有父类，以元祖的形式显示
			<pre>
			class Student():
			    '''
			    说明文档
			    '''
			    name='张安',
			    def setName(self):
			        print('this is setName')
			print(Student.__dict__)
			print(Student.__doc__)
			print(Student.__name__)
			print(Student.__bases__)
			</pre>
- 下划线
	- '_A'一个下划线表示只有类和子类能够使用 无法通过important引用
	- '__A'两个下划线表示只能当前的类的对象的本身使用
	- '__A__'表示系统函数
- 魔法函数
	- 魔法函数概述
		- 不要认为的调用，在特殊的时刻自动执行
		- 特征，方法名被前后两个下划线包裹
		- 需要学习的时候在什么时候调用什么魔法函数
	- 操作类
		- \_\_init__:类中自动初始化的函数
		- \_\_new__:对象实例化方法，类中首先被调用方法，一般不使用
		- \_\_call__:对象当做函数使用的时候触发
			- 实例化类后直接把实例化的类当做方法执行
			<pre>
			class A():
			    def __init__(self):
			        print('this is __init')
			a=A()
			a()
			</pre>
			这里a是一个类的实例化对象，但是不是方法，如果要调用，这里默认的是调用一个\_\_call__的方法
			<pre>
			class A():
			    def __init__(self):
			        print('this is __init')
			    def __call__(self, *args, **kwargs):
			        print('这是一个__call__函数')
			a=A()
			a()
			</pre>
			使用方法如上
		- \_\_str__:当把对象当做字符串使用的时候引发的函数
			<pre>
			class A():
			    def __init__(self):
			        print('this is __init')
			    def __str__(self):
			        return 'this is __str__'
			a=A()
			print(a)
			</pre>
			把实例化的a对象直接使用的时候自动执行\_\_str__方法，返回的值就是a对象的
		- \_\_repr__返回字符串，和上边的str方法一样，也有区别
	- 描述服相关
		- \_\_get__
		- \_\_set__
		- \_\_delet__
	- 属性操作相关
		- \_\_getattr__访问一个不存在的属性的时候触发
			<pre>
			class A():
			    def __getattr__(self, item):
			        print('__getattr__')
			a=A()
			print(a.setName)
			</pre>
			该方法会把要调用的方法当做参数传递进\_\_getattr\_\_方法中，如果传递进去的方法存在则执行，如果不存在则会执行\_\_getattr\_\_内部的方法
		- \_\_setattr__对成员属性进行设置的时候触发
			- 存在三个参数，(self,key,val)
			- self当前对象
			- key设置属性名称
			- value设置属性或是名称的值
			- 不能对属性进行直接赋值操作
			<pre>
			class A():
			    def __init__(self):
			        print('this is init')
			    def __setattr__(self, key, value):
			        print("执行到此处了")
			        super().__setattr__(key,value)
			a=A()			
			a.setName=100			
			print(a.setName)
			</pre>
			此处需要调用父类的setattr方法，如果直接使用该类中的setattr会出现死循环，在使用的时候赋值就可以进行正常赋值
	- 运算分类相关魔术方法
		- \_\_gt__进行大于运算的时候触发
			- 参数self，本省
			- 第二个对象
				- 返回任意值，推荐boole
			<pre>
			class A():
			    def __init__(self,name):
			        self.name=name
			    def __gt__(self, other):
			        return self.name>other.name
			a1=A(10)
			a2=A(1000)
			print(a1>a2)
			</pre>
			使用方法如上，需要比较的是两个实例化传入的参数，
			用于比较的两个参数会默认\_\_init\_\_为第一个参数，\_\_gt\_\_的参数为第二个参数进行比较
	- 类和对象的三种方法
		- 实例方法
			- 需要实例化对象才能使用的方法，使用的时候需要截止对象的的其他对象的方法完成
		- 静态方法
			- 不需要实例化，通过类直接访问(也可以通过实例化后的对象进行调用)；参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
		- 类方法
			- 不需要实例化(也可以通过实例化后的对象进行调用)；该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
		<pre>
		class A():
		    def setName(self):  #实例化方法
		        print('this is 实例化方法')
		    @classmethod；    #类方法
		    def name(cls):
		        print('this is 类方法')
		    @staticmethod   #静态方法
		    def staticName():
		        print('this is 静态方法')
		a=A()
		#实例化
		a.setName()
		#类方法
		a.name()
		A.name()
		#静态方法
		a.staticName()
		A.staticName()
		</pre>
		- 区别
	- 成员描述符
		- 变量的三种用法
			- 查询（调用）
			- 修改（修改变量）
			- 删（删除变量）
			<pre>
			class A():
			    def __init__(self):
			        self.name='www'
			a=A()
			print(a.name) #查询
			a.name='http' #修改
			print(a.name)
			del a.name  #删除
			print(a.name)
			</pre> 
		- 属性property
			<pre>
			class A():
			    def __init__(self):
			        self.name='张三'
			    def fget(self):
			        print('我被执行了')
			        return self.name
			    def fset(self,name):
			        self.name='百度:'+name
			    def fdel(self):
			        print('删除成功')
			    user=property(fget,fset,fdel,'this is property')
			a=A()
			print(a.name)
			a.user='AAA'
			print(a.user)
			</pre>
			property方法是默认是调用fget方法，当给user设置值的时候才会调用fset方法，如果直接调用a.user是只调用fget而不调用fset
		- 抽象类
			- 抽象方法的定义：没有具体实现内容的方法成为抽象方法
			- 抽象方法不是在父类中定义具体的方法，需要在继承的子类中实现具体的方法
			<pre>
			class A():
			    def say(self):
			        pass
			class B(A):
			    def say(self):
			        print('this is person')
			class C(A):
			    def say(self):
			        print('this is animal')
			a=A()
			a.say()
			b=B()
			b.say()
			c=C()
			c.say()
			</pre>
			- 抽象的类需要借助abc模块，import abc
			- 声明抽象类的方法
				- class Human(metaclass=abc.ABCMeta) 这种写法是死的，只能这么写
				- 抽象方法的定义
					@abc.abstractmethod
					<pre>
					import abc
					class Human(metaclass=abc.ABCMeta):
					    # 定义一个抽象的方法
					    @abc.abstractmethod
					    def person(self):
					        pass
					        # print('this is person')
					    # 定义类抽象方法
					    @abc.abstractclassmethod
					    def animal(cls):
					        pass
					        # print('this is animal')
					    # 定义静态抽象方法
					    @abc.abstractstaticmethod
					    def god():
					        pass
					</pre>
			- 抽象类的使用(抽象方法使用较少)
				- 抽象类可以包含抽象方法，也可以是具体的方法
				- 抽象类中可以有方法可以有属性
				- 抽象类不能直接实例化
				- 必须继承才可以使用，且继承的子类必须实现所有继承类的抽象方法
				- 假定子类没有实现继承的所有的抽象方法，子类也是不能实例化的
				- 抽象类的主要作用是设定类型的标准，以便于开发的时候具有统一的规范
				<pre>
				import abc
				class Human(metaclass=abc.ABCMeta):
				    # 定义一个抽象的方法
				    @abc.abstractmethod
				    def person(self):
				        pass
				    # 定义类抽象方法
				    @abc.abstractclassmethod
				    def animal(cls):
				        pass
				    # 定义静态抽象方法
				    @abc.abstractstaticmethod
				    def god():
				        pass
				class Other(Human):
				    def person(self):
				        print('我继承了父类person')
				    def animal(cls):
				        print('我继承了父类animal')
				    def god():
				        print('我继承了父类god')
				other=Other()
				other.person()
				other.animal()
				Other.god()
				</pre>
			- 自定义类
				- 函数名称可以当做变量使用
				- 外面定义的类要用参数
				<pre>
				class A():
				    pass
				def setName(self):
				    print('this is fun')
				A.setName=setName
				a=A()
				a.setName()
				</pre>
				同
				<pre>
				class A():
				    def setName(self):
				        print('this is fun')
				a=A()
				a.setName()
				</pre>
				- 类就是一堆属性和一堆方法的集合，可以自定义的组装
				- 组装的类需要在实例化之前赋值完成，也就是说往类上绑定方法(带参数)，而不是往实例化上绑定方法
					- 对于往实例化上绑定方法需要借助于第三发木块 from types impor MethodType
					<pre>
					from types import MethodType
					class A():
					    pass
					def B(self):
					    print('this is B')
					a=A()
					a.B=MethodType(B,A)
					a.B()
					</pre>
				- 把单独的类和单独的方法组装起来
				- 借助于type实现
				- type参数(类的名、继承的父类、类中的方法)
				<pre>
				def name(self):
				    print('this is name')
				def age(self):
				    print('this is age')
				A=type('Aname',(object,),{'class_Name':name,'class_Age':age})
				a=A()
				a.class_Name()
				a.class_Age()
				</pre>
				- 利用元类实现，Metaclass,
				- 元类的写法是固定的，必须继承type
					- class A(type)
					<pre>
					class person(type):
					    def __new__(cls, name,bases,attrs):
					         attrs['id']='001'
					         return type.__new__(cls,  name,bases,attrs)					
					class getPerson(object,metaclass=person):
					    pass
					get=getPerson()					
					print(get.id)
					</pre>
					metaclass为动态创建类的写法，创建类的内容为person继承的type的类，需要注意创建的person的类中的__new__的参数
#### Python包 ####
- 模块
	- 一个模块就是一个包含python代码的片段，文件后缀为.py，模块就是python文件
	- 模块的有点
		- 程序拆分，方便维护
		- 重复使用
		- 当做命名空间使用
	- 定义
		- 就是普通文件
		- 为了规范，最好在模块中书写
			- 函数（最好功能单一）
			- 类（相似功能的组合）
			- 测试代码
	- 如何使用
		- 模块直接导入
		- 语法
			<pre>
			import module
			module.className
			module.function()
			A=module.AB()
			A.function()
			</pre>
		- 案例
			- 包文件
			<pre>
			class Student():
			    def __init__(self,name,age):
			        self.name=name
			        self.age=age
			    def setName(self):
			        print('this is student:{0},age:{1}'.format(self.name,self.age))
			def say():
			    print('hello world')
			</pre>
			- 引用包文件
			<pre>
			import p01
			A=p01.Student('张三',33)
			A.setName()
			p01.say()			
			</pre>
		- 包名为数字的不能直接导入
			- 借助importLib
		- import 模块 as 别名
			<pre>
			import p01 as AA
			A=AA.Student('张三',33)
			A.setName()
			AA.say()
			</pre>
		- from module import func\_name,class\_name
			<pre>
			from p01 import Student,say
			A=Student('张三',33)
			A.setName()
			say()
			</pre>
		- from module\_name import *把模块中的所有的都导入,好处是不用再用模块引包了
			<pre>
			from p01 import *
			A=Student('张三',33)
			A.setName()
			say()
			</pre>
		- 对于导入的文件会自动执行函数和类外边的程序
			- 加判断 if  \_\_name\_\_=='\_\_main\_\_'
				- 这里的\_\_name\_\_是当前文件的名，'\_\_main\_\_'是当前文件当做主线程执行的时候(非引入)的文件名称或是包的名称
			- 程序的入口就是被当做主线程巡行的名称(所有的主线程文件的名称都是\_\_main\_\_)
	- 模块的路径
		- 引用包
			<pre>
			import sys			
			sys.path #显示路径
			</pre>
			搜索路径后，把包放在搜到的路径中，如果不想放在搜索到的文件路径中,往sys.path中添加路径  
			sys.path.append(dir)dir为设置的路径
		- 路径的查找顺序
			- 先在内存中查找
			- 搜索python内置模块
			- 搜索sys.path中的路径
		- 包是大于模块，包中是放置模块的文件夹
			- 包大于模块
			- 模块是文件
			- 包是文件夹
		- 项目文件夹的文件
			- 包的结构
				- 每一个包中包含一个\_\_init\_\_.py文件(有且只有一个)
				- 模块文件.py
				- 可以包中嵌套包
		- 包的导入操作
			- import package\_name
				- 直接导入的包可以使用\_\_init\_\_.py中的内容
				- 使用方式
					- package\_name.fun()
					- package\_name.class\_name.fun()
			
			



























<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<hr/>
# 课时39 1:21:30#
<hr/>
