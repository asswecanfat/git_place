import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#导入数据集
minist = input_data.read_data_sets('C:\\Users\\10248\\Desktop\\minist_data', one_hot=True)
#one_hot就是数组中只含有一个1，其他都是0
#每个批次大小
batch_size = 200
#分多少批次输入
n_batch = minist.train.num_examples // batch_size

#定义两个placehodler
x = tf.placeholder(tf.float32,[None,784])#图片的像素是28*28=784，原来是矩阵，把每一行放到上一行的后面，变成1*784
y = tf.placeholder(tf.float32,[None, 10])#标签(10000000000=1,0100000000=2，如此类推)
keep_prob = tf.placeholder(tf.float32)#drop层使用，决定多少比例的神经元工作

'''#定义无隐藏层的神经网络
weigth_L = tf.Variable(tf.zeros([784,10]))
bacies_L = tf.Variable(tf.zeros([10]))
predition = tf.nn.softmax(tf.matmul(x,weigth_L)+bacies_L)'''

#定义第一层神经元200个
weigth_L1 = tf.Variable(tf.truncated_normal([784,200],stddev=0.1))
bacies_L1 = tf.Variable(tf.zeros([1,200])+0.1)
out_put1 = tf.nn.relu(tf.matmul(x,weigth_L1)+bacies_L1)
out_put1 = tf.nn.dropout(out_put1,keep_prob=keep_prob)

#定义第二层神经元100个
weigth_L2 = tf.Variable(tf.truncated_normal([200,100],stddev=0.1))
bacies_L2 = tf.Variable(tf.zeros([1,100])+0.1)
out_put2 = tf.nn.relu(tf.matmul(out_put1,weigth_L2)+bacies_L2)
out_put2 = tf.nn.dropout(out_put2,keep_prob=keep_prob)

#定义输出层
weigth_L3 = tf.Variable(tf.truncated_normal([100,10],stddev=0.1))
bacies_L3 = tf.Variable(tf.zeros([1,10]))
predition = tf.matmul(out_put2,weigth_L3)+bacies_L3

#定义二次代价函数
#loss = tf.reduce_mean(tf.square(y-predition))
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=predition))#交叉熵
#训练
learning_rate = 0.2
train = tf.train.AdadeltaOptimizer(learning_rate).minimize(loss)

init = tf.global_variables_initializer()

#将结果存放在一个布尔类型的列表中
current_predition = tf.equal(tf.argmax(y,1),tf.argmax(predition,1))

#求准确率
aucc = tf.reduce_mean(tf.cast(current_predition,tf.float32))

saver = tf.train.Saver() #用于保存模型

with tf.Session() as sess:
    sess.run(init)
    for i in range(201):
        for a in range(n_batch):
            batch_xs,batch_ys = minist.train.next_batch(batch_size)
            sess.run(train,feed_dict={x:batch_xs,y:batch_ys,keep_prob:0.8})#,

        acc = sess.run(aucc,feed_dict={x:minist.test.images,y:minist.test.labels,keep_prob:1})#,
        print('第%d次训练，识别准确率为：%f' % (i+1,acc))
    saver.save(sess ,'C:\\Users\\10248\\Desktop\\手写数字模型\\model.ckpt')

