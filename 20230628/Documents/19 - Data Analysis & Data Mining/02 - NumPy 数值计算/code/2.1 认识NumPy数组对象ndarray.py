# -*- coding: utf-8 -*-

# 代码 2-1：创建数组并查看数组属性
import numpy as np #导入 NumPy 库 
# 创建一维数组 
arr1 = np.array([1, 2, 3, 4]) 
print(' 创建的数组为： ',arr1)

# 创建二维数组
arr2 = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
print('创建的数组为：\n',arr2)

# 查看数组属性
print('数组类型为：',arr2.dtype)  #查看数组类型
print('数组元素个数为：',arr2.size)  #查看数组元素个数
print('数组每个元素大小为：',arr2.itemsize)  #查看数组每个元素大小


# 代码 2-2：重新设置shape（不是转置）
arr2.shape = 4,3 
print('重新设置shape 后的arr2 为：\n',arr2)

# 代码 2-3：使用 arange 函数创建数组（初值、终值、步长，不含终值）
print('使用arange函数创建的数组为：\n',np.arange(0,1,0.1))

# 代码 2-4：使用 linspace 函数创建数组（初值、终值、元素个数，包含终值）
print('使用linspace函数创建的数组为：',np.linspace(0, 1, 12))

# 代码 2-5：使用 logspace 函数创建等比数列
print('使用logspace函数创建的数组为：\n',np.logspace(0, 2, 20))

# 代码 2-6：使用zeros函数创建数组（全部填充0）
print('使用zeros函数创建的数组为：\n',np.zeros((2,3)))

# 代码 2-7：使用eye函数创建数组（主对角线为1，其他为0，即：单位矩阵）
print('使用eye函数创建的数组为：\n',np.eye(3))

# 代码 2-8：使用diag函数创建数组（指定对角线数值的数组，除对角线外均为0）
print('使用diag函数创建的数组为：\n',np.diag([1,2,3,4]))

# 代码 2-9：使用ones函数创建数组（数组元素全为1）
print('使用ones函数的数组为：\n',np.ones((5,3)))

# 代码 2-10：数组数据类型转换
print('转换结果为：',np.float64(42))  #整型转换为浮点型
print('转换结果为：',np.int8(42.0))  #浮点型转换为整型
print('转换结果为：',np.bool(42))  #整型转换为布尔型
print('转换结果为：',np.bool(0))  #整型转换为布尔型
print('转换结果为：',np.float(True))  #布尔型转换为浮点型
print('转换结果为：',np.float(False))  #布尔型转换为浮点型


# 代码 2-11：创建数据类型
df = np.dtype([("name", np.str_, 40), ("numitems", np.int64),
    ("price",np.float64)])
print('数据类型为：',df)

# 代码 2-12：查看数据类型，可以直接查看或者使用numpy.dtype函数查看
print('数据类型为：',df["name"])
print('数据类型为：',np.dtype(df["name"]))

# 代码 2-13：自定义数组数据，可以预先指定数据类型。
# 在使用array函数创建数组时，数组的数据类型默认是浮点型。(西红柿、卷心菜）
itemz = np.array([("tomatoes", 42, 4.14),("cabbages", 13, 1.72)],
    dtype=df)
print('自定义数据为：',itemz)

# 代码 2-14：无约束条件下生成随机数
print('生成的随机数组为：\n',np.random.random(100))

# 代码 2-15：生成服从均匀分布的随机数
print('生成的随机数组为：\n',np.random.rand(10,5))

# 代码 2-16：生成服从正态分布的随机数
print('生成的随机数组为：\n',np.random.randn(10,5))

# 代码 2-17：生成给定上下范围的随机数，如创建一个最小值不低于 2、最大值不高于 10 的 2 行 5 列数组
print('生成的随机数组为：\n',np.random.randint(2,10,size = [2,5]))

# 代码 2-18：一维数组的索引
arr = np.arange(10)
print('索引结果为：',arr[5])  #用整数作为下标可以获取数组中的某个元素
#用范围作为下标获取数组的一个切片，包括arr[3]不包括arr[5]
print('索引结果为：',arr[3:5])
print('索引结果为：',arr[:5])  #省略开始下标，表示从arr[0]开始
#下标可以使用负数，-1表示从数组后往前数的第一个元素
print('索引结果为：',arr[-1])

arr[2:4] = 100,101
print('索引结果为：',arr)  #下标还可以用来修改元素的值
#范围中的第三个参数表示步长，2表示隔一个元素取一个元素
print('索引结果为：',arr[1:-1:2])
print('索引结果为：',arr[5:1:-2])  #步长为负数时，开始下标必须大于结束下标

# 代码 2-19：多维数组的索引
arr = np.array([[1, 2, 3, 4, 5],[4, 5, 6, 7, 8], [7, 8, 9, 10, 11]])
print('创建的二维数组为：',arr)
print('索引结果为：',arr[0,3:5])  #索引第0行中第3和第4列的元素
#索引第2和第3行中第3列、第4列和第5列的元素
print('索引结果为：\n',arr[1:,2:])
print('索引结果为：',arr[:,2])  #索引第2列的元素

# 代码 2-20：多维数组的索引（使用整数和布尔值索引访问数据）
#从两个序列的对应位置取出两个整数组成下标：arr[0,1], arr[1,2], arr[2,3]
print('索引结果为：',arr[[(0,1,2),(1,2,3)]])
print('索引结果为：',arr[1:,(0,2,3)])  #索引第2、3行中第0、2、3列的元素

mask = np.array([1,0,1],dtype = np.bool)
#mask是一个布尔数组，它索引第1、3行中第2列的元素
print('索引结果为：',arr[mask,2])


# 代码 2-21：改变数组形状
arr = np.arange(12)  #创建一维数组
print('创建的一维数组为：',arr)
print('新的一维数组为：',arr.reshape(3,4))  #设置数组的形状
print('数组维度为：',arr.reshape(3,4).ndim)  #查看数组维度

# 代码 2-22：使用ravel函数展平数组
arr = np.arange(12).reshape(3,4)
print('创建的二维数组为：\n',arr)
print('数组展平后为：',arr.ravel())

# 代码 2-23：使用flatten函数展平数组
print('数组展平为：',arr.flatten())  #横向展平
print('数组展平为：',arr.flatten('F'))  #纵向展平

# 代码 2-24-0：组合数据的基于的数组
arr1 = np.arange(12).reshape(3,4)
print('创建的数组1为：',arr1)
arr2 = arr1*3
print('创建的数组2为：',arr2)

# 代码 2-24：使用hstack函数实现数组横向组合
print('横向组合为：\n',np.hstack((arr1,arr2)))  #hstack函数横向组合

# 代码 2-25：使用concatenate函数实现数组横向组合
print('纵向组合为：\n',np.vstack((arr1,arr2)))  #vstack函数纵向组合

# 代码 2-26：使用vstack函数实现数组纵向组合
print('横向组合为：\n',np.concatenate((arr1,arr2),axis = 1))  #concatenate函数横向组合
print('纵向组合为：\n',np.concatenate((arr1,arr2),axis = 0))  #concatenate函数纵向组合

# 代码 2-27：使用hsplit函数实现数组横向分割
arr = np.arange(16).reshape(4,4)
print('创建的二维数组为：\n',arr)
print('横向分割为：\n',np.hsplit(arr, 2))  #hsplit函数横向分割

# 代码 2-28：使用vsplit函数实现数组纵向分割
print('纵向分割为：\n',np.vsplit(arr, 2))  #vsplit函数纵向分割

# 代码 2-29：使用split函数实现数组横向&纵向分割
print('横向分割为：\n',np.split(arr, 2, axis=1))  #split函数横向分割
print('纵向分割为：\n',np.split(arr, 2, axis=0))  #split函数纵向分割
