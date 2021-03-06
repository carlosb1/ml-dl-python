def weight_variable(shape):
    initial = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.truncated_normal(0,1,shape=shape)
    return tf.Variable(initial)


def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max.pool(x,ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

 W_conv1 = weight_variable([5,5,1,32])
 b_conv1 = bias_variable([32])

 x_image = tf.reshape(x,[-1,28,28,1])


