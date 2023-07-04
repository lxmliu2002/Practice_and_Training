# -*- coding: utf-8 -*-

# 代码 2-39：save函数是以二进制的格式保存数据
import numpy as np  #导入NumPy库
arr = np.arange(100).reshape(10,10)  #创建一个数组
#在当前文件夹上级文件夹中创建 tmp 文件夹
np.save("../tmp/save_arr",arr)  #保存数组
print('保存的数组为：\n',arr)

# 代码 2-40：savez函数可以将多个数组保存到一个文件中
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.arange(0,1.0,0.1)
np.savez('../tmp/savez_arr',arr1,arr2)
print('保存的数组1为：\n',arr1)
print('保存的数组2为：',arr2)

# 代码 2-41：load函数是从二进制的文件中读取数据
loaded_data = np.load("../tmp/save_arr.npy")  #读取含有单个数组的文件
print('读取的数组为：\n',loaded_data)

loaded_data1 = np.load("../tmp/savez_arr.npz")  #读取含有多个数组的文件
print('读取的数组1为：\n',loaded_data1['arr_0'])
print('读取的数组2为：',loaded_data1['arr_1'])

# 代码 2-42：数组的文本文件的读写
arr = np.arange(0,12,0.5).reshape(4,-1)
print('创建的数组为：\n',arr)

#savetxt函数是将数组写到某种分隔符隔开的文本文件中
#fmt ="%d"为指定保存为整数
np.savetxt("../tmp/arr.txt", arr, fmt="%d", delimiter=",")

#loadtxt函数执行的是把文件加载到一个二维数组中
#读入的时候也需要指定逗号分隔
loaded_data = np.loadtxt("../tmp/arr.txt",delimiter=",")
print('读取的数组为：\n',loaded_data)


# 代码 2-43：genfromtxt函数面向的是结构化数组和缺失数据
loaded_data = np.genfromtxt("../tmp/arr.txt", delimiter = ",")
print('读取的数组为：\n',loaded_data)

# 代码 2-44：直接排序
np.random.seed(42)  #设置随机种子
arr = np.random.randint(1,10,size = 10)  #生成随机数
print('创建的数组为：\n',arr)

arr.sort()  #直接排序
print('排序后数组为：\n',arr)

arr = np.random.randint(1,10,size = (3,3))  #生成3行3列的随机数
print('创建的数组为：\n',arr)
#sort函数也可以指定一个axis参数，使得sort函数可以沿着指定轴对数据集进行排序
#axis=1为沿横轴排序； axis=0为沿纵轴排序。
arr.sort(axis = 1)  #沿着横轴排序
print('排序后数组为：\n',arr)

arr.sort(axis = 0)  #沿着纵轴排序
print('排序后数组为：\n',arr)

# 代码 2-45：间接排序-argsort
#argsort函数返回值为重新排序值的下标。 
arr = np.array([2,3,6,8,0,7])
print('创建的数组为：',arr)
print('排序后数组为：',arr.argsort())  #返回值为重新排序值的下标


# 代码 2-46：间接排序-lexsort
#lexsort函数返回值是按照最后一个传入数据排序的
a = np.array([3,2,6,4,5])
b = np.array([50,30,40,20,10])
c = np.array([400,300,600,100,200])
d = np.lexsort((a,b,c))  #lexsort函数只接受一个参数，即（a,b,c）
#多个键值排序是按照最后一个传入数据计算的
print('排序后数组为：',list(zip(a[d],b[d],c[d])))


# 代码 2-47：去重
#通过unique函数可以找出数组中的唯一值并返回已排序的结果
names = np.array(['小明', '小黄', '小花', '小明', '小花', '小兰', '小白'])
print('创建的数组为：',names)

print('去重后的数组为：',np.unique(names))

#跟np.unique等价的Python代码实现过程
print('去重后的数组为：',sorted(set(names)))

ints = np.array([1,2,3,4,4,5,6,6,7,8,8,9,10])  #创建数值型数据
print('创建的数组为：',ints)
print('去重后的数组为：',np.unique(ints))

# 代码 2-48：重复
#tile函数主要有两个参数，参数“A”指定重复的数组，参数“reps”指定重复的次数。
arr = np.arange(5)
print('创建的数组为：',arr)
print('重复后数组为：',np.tile(arr,3))  #对数组进行重复

# 代码 2-49：重复
'''
repeat函数主要有三个参数，
参数“a”是需要重复的数组元素，
参数“repeats”是重复次数，
参数“axis”指定沿着哪个轴进行重复，
axis = 0表示按行进行元素重复；axis = 1表示按列进行元素重复。
'''
np.random.seed(42)  #设置随机种子
arr = np.random.randint(0,10,size = (3,3))
print('创建的数组为：\n',arr)
print('重复后数组为：\n',arr.repeat(2, axis = 0))  #按行进行元素重复
print('重复后数组为：\n',arr.repeat(2, axis = 1))  #按列进行元素重复

# 代码 2-50：常用的统计函数
arr = np.arange(20).reshape(4,5)
print('创建的数组为：\n',arr)
print('数组的和为：',np.sum(arr))  #计算数组的和
print('数组横轴的和为：',arr.sum(axis = 0))  #沿着横轴计算求和
print('数组纵轴的和为：',arr.sum(axis = 1))  #沿着纵轴计算求和
print('数组的均值为：',np.mean(arr))  #计算数组均值
print('数组横轴的均值为：',arr.mean(axis = 0))  #沿着横轴计算数组均值
print('数组纵轴的均值为：',arr.mean(axis = 1))  #沿着纵轴计算数组均值
print('数组的标准差为：',np.std(arr))  #计算数组标准差
print('数组的方差为：',np.var(arr))  #计算数组方差
print('数组的最小值为：',np.min(arr))  #计算数组最小值
print('数组的最大值为：',np.max(arr))  #计算数组最大值
print('数组的最小元素为：',np.argmin(arr))  #返回数组最小元素的索引
print('数组的最大元素为：',np.argmax(arr))  #返回数组最大元素的索引

arr = np.arange(2,10)
print('创建的数组为：',arr)
print('数组元素的累计和为：',np.cumsum(arr))  #计算所有元素的累计和
print('数组元素的累计积为：',np.cumprod(arr))  #计算所有元素的累计积


'''
任务实现：
读取iris数据集中的花萼长度数据（已保存为csv格式），
对其进行排序、去重，并求出和、累积和、均值、标准差、方差、最小值、最大值。
'''
# 代码 2-51：iris数据集统计任务实现
iris_sepal_length = np.loadtxt("../data/iris_sepal_length.csv", 
    delimiter=",")  #读取文件
print('花萼长度表为：\n',iris_sepal_length)

iris_sepal_length.sort()  #对数据进行排序
print('排序后的花萼长度表为：\n',iris_sepal_length)

#去除重复值
print('去重后的花萼长度表为：\n',np.unique(iris_sepal_length))

print('花萼长度表的总和为：\n',np.sum(iris_sepal_length))  #计算数组总和

#计算所有元素的累计和
print('花萼长度表的累计和为：\n',np.cumsum(iris_sepal_length))

print('花萼长度表的均值为：\n',np.mean(iris_sepal_length))  #计算数组均值

#计算数组标准差
print('花萼长度表的标准差为：\n',np.std(iris_sepal_length))

print('花萼长度表的方差为：\n',np.var(iris_sepal_length))  #计算数组方差
print('花萼长度表的最小值为：\n',np.min(iris_sepal_length))  #计算最小值
print('花萼长度表的最大值为：\n',np.max(iris_sepal_length))  #计算最大值
