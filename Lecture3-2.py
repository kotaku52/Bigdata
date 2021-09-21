#导入相应的包
import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

#加载数据
fashion_mnist = keras.datasets.fashion_mnist

#训练集和测试集的划分
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

#使图像显示中文
plt.rcParams["font.sans-serif"]=["FangSong"]

#加载数据
fashion_mist = keras.datasets.fashion_mnist
(train_images, train_lables), (test_images, test_lables) = fashion_mist.load_data()

# 构建标签列表
class_names = ['T恤/上衣', '裤子', '套衫', '连衣裙', '外套','凉鞋', '衬衫', '运动鞋', '手提包', '踝靴']


#数据预处理,将每个像素点压缩在0和1之间（节省运算量）
train_images = train_images/255.0
test_images = test_images/255.0

new_model = keras.models.load_model("mymodel.h5")

test_loss , test_acc = new_model.evaluate(test_images,test_lables,verbose = 2)
print("\nTest accuracy:{:5.2f}%".format(100 * test_acc))
probability_model = tf.keras.Sequential([new_model,tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)
print(predictions[0])



# 答应所有的预测结果
plt.figure()
plt.subplot(1,2,1)
plt.xticks([])
plt.yticks([])
plt.imshow(test_images[1],cmap=plt.cm.binary)
plt.xlabel("{} 预测正确率：{:2.0f}%".format(class_names[np.argmax(predictions[1])],
                               100*np.max(predictions[0])),fontsize=20,color="blue")
plt.subplot(1,2,2)
plt.xticks(range(10),class_names)
plt.yticks([])
thisplot = plt.bar(range(10), predictions[1], color="#777777")
plt.ylim([0, 1])
predicted_label = np.argmax(predictions[1])

thisplot[predicted_label].set_color('blue')
# thisplot[true_label].set_color('blue')
plt.show()
print("模型预测的结果为：{}".format(class_names[np.argmax(predictions[1])]))



#打印图像
# plt.figure()
# plt.xticks()
# plt.yticks()
# plt.imshow(train_images[0])
# plt.show()