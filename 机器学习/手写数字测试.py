import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter
import os

image_path = 'C:\\Users\\10248\\Desktop\\sbz\\'
image_list = os.listdir(image_path)
Image_path = [image_path + i for i in image_list]
def imageprepare(input_mage): #关于图片数字化，并将每个像素值限定在0~1
    im = Image.open(input_mage) #读取的图片所在路径，注意是28*28像素
    plt.imshow(im) #显示需要识别的图片
    plt.show()
    im = im.convert('L')
    tv = list(im.getdata())
    tva = [(255-x)*1.0/255.0 for x in tv]
    return tva


#定义两个placehodler
x = tf.placeholder(tf.float32,[None,784])#图片的像素是28*28=784，原来是矩阵，把每一行放到上一行的后面，变成1*784
y = tf.placeholder(tf.float32,[None, 10])#标签(10000000000=1,0100000000=2，如此类推)

#定义第一层神经元200个
weigth_L1 = tf.Variable(tf.truncated_normal([784,200],stddev=0.05))
bacies_L1 = tf.Variable(tf.zeros([1,200]))
out_put1 = tf.nn.relu(tf.matmul(x,weigth_L1)+bacies_L1)

#定义第二层神经元100个
weigth_L2 = tf.Variable(tf.truncated_normal([200,100],stddev=0.05))
bacies_L2 = tf.Variable(tf.zeros([1,100]))
out_put2 = tf.nn.relu(tf.matmul(out_put1,weigth_L2)+bacies_L2)

#定义输出层
weigth_L3 = tf.Variable(tf.truncated_normal([100,10],stddev=0.05))
bacies_L3 = tf.Variable(tf.zeros([1,10]))
predition = tf.matmul(out_put2,weigth_L3)+bacies_L3

init = tf.global_variables_initializer()

#定义交叉熵代价函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=predition))#交叉熵
#训练
learning_rate = 0.2
train = tf.train.AdadeltaOptimizer(learning_rate).minimize(loss)

#将结果存放在一个布尔类型的列表中
current_predition = tf.equal(tf.argmax(y,1),tf.argmax(predition,1))
aucc = tf.reduce_mean(tf.cast(current_predition,tf.float32))
saver = tf.train.Saver() #用于保存模型

with tf.Session() as sess:
    sess.run(init)
    saver.restore(sess, 'C:\\Users\\10248\\Desktop\\手写数字模型\\model.ckpt')#使用模型，参数和之前的代码保持一致
    re_predition = tf.argmax(predition, 1)
    for _ in Image_path:
        result = imageprepare(_)
        predint = re_predition.eval(feed_dict={x: [result]}, session=sess)
        print('识别结果:')
        print(predint[0])