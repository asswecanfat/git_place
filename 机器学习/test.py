import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

'''#constant是常量
m1 = tf.constant([[2,2]])
m2 = tf.constant([[2],[2]])
t1 = tf.matmul(m1,m2)
print(t1)
#图要在会话中进行
sess = tf.Session()

result = sess.run(t1)
print(result)
sess.close()

with tf.Session() as sess:
    res = sess.run(t1)
    print(res)'''


'''x = tf.Variable([[2,2]])
y = tf.constant([[3,3]])

#变量需要初始化
init = tf.global_variables_initializer()#全局变量初始化

sub = tf.subtract(x,y)

ad = tf.add(x,sub)

with tf.Session() as sess:
    sess.run(init) #要run一下，初始化变量
    print(sess.run(sub),sess.run(ad))'''

'''state = tf.Variable(0, name='counter')
asw = tf.add(state, 1)
addion = tf.assign(state, asw) #在会话中赋值需要用函数assign
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(10):
        sess.run(addion)
        print(sess.run(state))'''

'''input1 = tf.constant(1.0)
input2 = tf.constant(2.0)
input3 = tf.constant(3.0)

sub = tf.add(input1,input2)

mul = tf.multiply(sub,input3)

with tf.Session() as sess:
    result = sess.run([sub,mul]) #Fetch可多个op同时运行
    print(result)'''

'''#Feed
input1 = tf.placeholder(tf.float32)#占位符
input2 = tf.placeholder(tf.float32)

mul = tf.multiply(input1,input2)

with tf.Session() as sess:
    #Feed以字典形式传入，而且是在运行时传入
    print(sess.run(mul,feed_dict={input1:[3.],input2:[5.]}))'''

'''x_data = np.random.rand(100)
y_data = 1.456*x_data + 0.339

b = tf.Variable(0.)
k = tf.Variable(0.)
y = b*x_data + k

#构造二次代价函数
loss = tf.reduce_mean(tf.square(y_data - y))
#定义梯度下降法来进行训练的优化器
optimize = tf.train.GradientDescentOptimizer(0.5)#梯度的量
#最小化代价函数
train = optimize.minimize(loss)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(601):
        sess.run(train)
        if i % 30 == 0:
            print(i,sess.run([b,k]))'''

x_data = np.linspace(-0.5,0.5,200)[:,np.newaxis]#一维数组转换成二维数组
noise = np.random.normal(0,0.02,x_data.shape)#干扰项
y_data = np.square(x_data) + noise

x = tf.placeholder(tf.float32,[None,1])
y = tf.placeholder(tf.float32,[None,1])

#构建神经网络中间层
weights_L1 = tf.Variable(tf.random_normal([1,10]))#有十个神经元，权值为1*10
biases_L1 = tf.Variable(tf.zeros([1,10]))#偏置值一般设为1*10个0
wx_plus_L1 = tf.matmul(x,weights_L1) + biases_L1
ouput_L1 = tf.nn.tanh(wx_plus_L1)#激活函数

#构建神经网络的输出层
weights_L2 = tf.Variable(tf.random_normal([10,1]))
biases_L2 = tf.Variable(tf.zeros([1,1]))
wx_plus_L2 = tf.matmul(ouput_L1,weights_L2) + biases_L2
predition = tf.nn.tanh(wx_plus_L2)#可不用激励函数

#构建loss函数
loss = tf.reduce_mean(tf.square(y-predition))
#使用梯度下降法来训练的优化器来最小化
train_step = tf.train.GradientDescentOptimizer(0.3).minimize(loss)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(2001):
        sess.run(train_step,feed_dict={x:x_data,y:y_data})

    #获得预测值
    predition_value = sess.run(wx_plus_L2,feed_dict={x:x_data})
    #画图
    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,predition_value,'r-',lw = 5)
    plt.show()


