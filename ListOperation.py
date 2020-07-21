#coding=utf-8 Python 3.7.4
''' 
 * Description  : Python.List的增、删、改、查
 * Author       : Lichongyou
 * Date         : 2020-07-21 16:54:56
 * LastEditTime : 2020-07-21 17:11:06
 * LastEditors  : Lichongyou
''' 

#首先创建一个列表list
list=[ i for i in range(10)]
print('原始列表：',list)

#在列表尾巴增加一个元素
list.append(10)
print('增加一个元素的列表:',list)

#通过下标切片访问列表
print(list[2:5])

#删除
del list[9]
print(list)

#获取列表元素个数
print('列表元素个数：',len(list))