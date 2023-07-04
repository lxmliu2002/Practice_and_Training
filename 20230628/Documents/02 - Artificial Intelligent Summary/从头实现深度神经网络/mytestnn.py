#numpy是数学工具包
#后边要用到numpy中的数组类型、矩阵运算等
import numpy as np

# 前向传播函数
# - x：包含输入数据的numpy数组，形状为（N，d_1，...，d_k）
# - w：形状为（D，M）的一系列权重
# - b：偏置，形状为（M，）
def affine_forward(x, w, b) :
    out = None                       # 初始化返回值为None
    N = x.shape[0]                   # 重置输入参数X的形状
    x_row = x.reshape(N, -1)         # (N,D)
    out = np.dot(x_row, w) + b       # (N,M)
    cache = (x, w, b)                # 缓存值，反向传播时使用
    return out, cache

# 反向传播函数
# - x：包含输入数据的numpy数组，形状为（N，d_1，...，d_k）
# - w：形状（D，M）的一系列权重
# - b：偏置，形状为（M，）
def affine_backward(dout, cache):
    x, w, b = cache                              # 读取缓存
    dx, dw, db = None, None, None                # 返回值初始化
    dx = np.dot(dout, w.T)                       # (N,D)
    dx = np.reshape(dx, x.shape)                 # (N,d1,...,d_k)
    x_row = x.reshape(x.shape[0], -1)            # (N,D)
    dw = np.dot(x_row.T, dout)                   # (D,M)
    db = np.sum(dout, axis=0, keepdims=True)     # (1,M)
    return dx, dw, db

X = np.array([[2,1],
            [-1,1],
            [-1,-1],
            [1,-1]])      # 用于训练的坐标，对应的是I、II、III、IV象限
t = np.array([0,1,2,3])   # 标签，对应的是I、II、III、IV象限
np.random.seed(1)         # 有这行语句，你们生成的随机数就和我一样了

# 一些初始化参数
input_dim = X.shape[1]     # 输入参数的维度，此处为2，即每个坐标用两个数表示
num_classes = t.shape[0]   # 输出参数的维度，此处为4，即最终分为四个象限
hidden_dim = 50            # 隐藏层维度，为可调参数
reg = 0.001                # 正则化强度，为可调参数
epsilon = 0.001            # 梯度下降的学习率，为可调参数
# 初始化W1，W2，b1，b2
W1 = np.random.randn(input_dim, hidden_dim)     # (2,50)
W2 = np.random.randn(hidden_dim, num_classes)   # (50,4)
b1 = np.zeros((1, hidden_dim))                  # (1,50)
b2 = np.zeros((1, num_classes))                 # (1,4)

for j in range(10000):   #这里设置了训练的循环次数为10000
 # ①前向传播
    H,fc_cache = affine_forward(X,W1,b1)                 # 第一层前向传播
    H = np.maximum(0, H)                                 # 激活
    relu_cache = H                                       # 缓存第一层激活后的结果
    Y,cachey = affine_forward(H,W2,b2)                   # 第二层前向传播
 # ②Softmax层计算
    probs = np.exp(Y - np.max(Y, axis=1, keepdims=True))
    probs /= np.sum(probs, axis=1, keepdims=True)        # Softmax算法实现
 # ③计算loss值
    N = Y.shape[0]                                       # 值为4
    print(probs[np.arange(N), t])                        # 打印各个数据的正确解标签对应的神经网络的输出
    loss = -np.sum(np.log(probs[np.arange(N), t])) / N   # 计算loss
    print(loss)                                          # 打印loss
 # ④反向传播
    dx = probs.copy()                                    # 以Softmax输出结果作为反向输出的起点
    dx[np.arange(N), t] -= 1                             #
    dx /= N                                              # 到这里是反向传播到softmax前
    dh1, dW2, db2 = affine_backward(dx, cachey)          # 反向传播至第二层前
    dh1[relu_cache <= 0] = 0                             # 反向传播至激活层前
    dX, dW1, db1 = affine_backward(dh1, fc_cache)        # 反向传播至第一层前
 # ⑤参数更新
    dW2 += reg * W2
    dW1 += reg * W1
    W2 += -epsilon * dW2
    b2 += -epsilon * db2
    W1 += -epsilon * dW1
    b1 += -epsilon * db1

test = np.array([[2,2],[-2,2],[-2,-2],[2,-2]])
H,fc_cache = affine_forward(test,W1,b1)               #仿射
H = np.maximum(0, H)                                  #激活
relu_cache = H
Y,cachey = affine_forward(H,W2,b2)  #仿射
 # Softmax
probs = np.exp(Y - np.max(Y, axis=1, keepdims=True))
probs /= np.sum(probs, axis=1, keepdims=True)  # Softmax
print(probs)
for k in range(4):
    print(test[k,:],"所在的象限为",np.argmax(probs[k,:])+1)