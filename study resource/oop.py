#!/usr/bin/python
# -*- coding: UTF-8 -*-
# class Employee:
#     empCount = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount+=1
#     def displayCount(self):
#         print ("Totla employee %d" %Employee.empCount) 
#     def displayEmployee(self):
#         print ("Name :", self.name, ", Salary: ", self.salary)


# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Manni", 5000)
# # emp1.displayEmployee()
# # emp2.displayEmployee()
# # emp1.age = 8
# # print(emp1.age)
# # del emp1.age
# # hasattr(emp1, "age")
# # print(getattr(emp1, "age"))
# # setattr(emp1, "age", 9)
# # print(getattr(emp1, "age"))
# # delattr(emp1,"age")
# # print ("Total Employee %d" %Employee.empCount)


# print "Employee.__doc__:", Employee.__doc__
# print "Employee.__name__:", Employee.__name__
# print "Employee.__module__:", Employee.__module__
# print "Employee.__bases__:", Employee.__bases__
# print "Employee.__dict__:", Employee.__dict__

##########################################################################################################
# 类的继承
# 面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。

# 通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。

# 继承语法

# class 派生类名(基类名)
#     ...
# 在python中继承中的一些特点：

# 1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看：python 子类继承父类构造函数说明。
# 2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
# 3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
# 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。

# 语法：

# 派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：

##########################################################################################################

# class SubClassName (ParentClass1[, ParentClass2, ...]):

# class Parent:       
#     parentAttr = 100
#     def __init__(self):
#         print "father"
#     def parentMethod(self):
#         print ("use father function")
#     def setAttr(self, attr):
#         Parent.parentAttr = attr
#     def getAttr(self):
#         print "father attribute:", Parent.parentAttr

# class Child(Parent):
#     def __init__(self):
#         print ("son!!!")
#     def childMethod(self):
#         print ("use son function!")
    
# c = Child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(200)
# c.getAttr()
##########################################################################################################
# 基础重载方法
# 下表列出了一些通用的功能，你可以在自己的类重写：

# 序号	方法, 描述 & 简单的调用
# 1	__init__ ( self [,args...] )
# 构造函数
# 简单的调用方法: obj = className(args)
# 2	__del__( self )
# 析构方法, 删除一个对象
# 简单的调用方法 : del obj
# 3	__repr__( self )
# 转化为供解释器读取的形式
# 简单的调用方法 : repr(obj)
# 4	__str__( self )
# 用于将值转化为适于人阅读的形式
# 简单的调用方法 : str(obj)
# 5	__cmp__ ( self, x )
# 对象比较
# 简单的调用方法 : cmp(obj, x)
#########################################################################################################
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

# 类的方法
# 在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数

# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods

# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
 
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
   
#     def __add__(self,other):
#         return Vector(self.a + other.a, self.b + other.b)
 
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print v1 + v2


###########################################################################################
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
 
counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
# print counter.__secretCount  会报错 不允许实例化的类访问私有数据
print counter._JustCounter__secretCount 
# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性，
class Runoob:
    __site = "www.runoob.com"

runoob = Runoob()
print runoob._Runoob__site


# 单下划线、双下划线、头尾双下划线说明：
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。