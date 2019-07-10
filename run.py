# -*- coding: utf-8 -*-
print('正在加载模块...')
import tensorflow as tf
import numpy as np
import re
import os
import time
#将类别ID转换为标签
def load_index(model_dir):
  word_re=re.compile(r'.*')
  file=open(model_dir+'/traned_imagenet_synset_to_human_label_map.txt')
  index_dict=dict()
  k=0
  for line in file.readlines():
    cut_words=word_re.findall(str(line))
    for word in cut_words:
      if word!='' and word != '\n':
        index_dict[k]=word
    k+=1
  return index_dict
#读取训练好的Inception-v3模型来创建graph
def create_graph(model_dir):
  with tf.gfile.FastGFile(os.path.join(
      model_dir, 'classify_image_graph_def.pb'), 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

def main():
  #目录设置
  model_dir='/home/pi/Desktop/object_detection'
  image_path='/home/pi/Desktop'
  images=os.listdir(image_path)
  #读取标签
  index_dict=load_index(model_dir)
  #创建graph
  print('开始构建TensorFlow图...')
  create_graph(model_dir)
  sess=tf.Session()
  softmax_tensor= sess.graph.get_tensor_by_name('softmax:0')
  #开始预测
  print('需要几次检测(第一次检查需要较长时间):')
  k=int(input())
  j=0
  while(j<k):
    print('第%d次检测!'%(j+1))
    os.system("raspistill -o /home/pi/Desktop/keychain.jpg -t 1")
    result=[]
    for image in images:
      if image[-3:] in ['jpg','JPG','peg','PEG']:
        image_data = tf.gfile.FastGFile(image_path+'/'+image, 'rb').read()
        #输入图像数据，得到softmax概率值（一个shape=(1,1008)的向量）
        predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
        #(1,1008)->(1008,)
        predictions = np.squeeze(predictions)
        objects=''
        split=','
        for i in range(5):
          if i==4:
            split=' 或者 '
          objects=objects+split+index_dict[np.where(predictions==max(predictions))[0][0]]+' '
          predictions[predictions==max(predictions)]=0
        result.append(image+'中可能有 '+objects[1:-1]+'.')
    print(result)
    j+=1
    #time.sleep(0.5)
  print('退出.')
  sess.close()
  
if __name__ == '__main__':
  main()


