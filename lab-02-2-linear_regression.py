# Lab 2 Linear Regression
import tensorflow as tf
import numpy as np

x_data = np.array([1, 2, 3])
y_data = np.array([1, 2, 3])

# Try to find values for W and b to compute y_data = W * x_data + b
# We know that W should be 1 and b should be 0
# But let's use Tensorflow to figure it out
W = tf.Variable(tf.random_uniform(
    [1], minval=-1.0, maxval=1.0, dtype=tf.float32))
b = tf.Variable(tf.random_uniform(
    [1], minval=-1.0, maxval=1.0, dtype=tf.float32))

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
# Now we can use X and Y in place of x_data and y_data

# Our hypothesis
hypothesis = X * W + b

# Simplified cost function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize
a = tf.Variable(0.1)  # Learning rate, alpha
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

# Initialize all variables before we start
init = tf.global_variables_initializer()

# Lauch graph
sess = tf.Session()
sess.run(init)

# Fit the line
for step in range(2001):
    sess.run(train, feed_dict={X: x_data, Y: y_data})
    if step % 20 == 0:
        print(step, sess.run(cost, feed_dict={
              X: x_data, Y: y_data}), sess.run(W), sess.run(b))

# Learns best fit W:[ 1.],  b:[  5.90419234e-08]

print(sess.run(hypothesis, feed_dict={X: 5}))
print(sess.run(hypothesis, feed_dict={X: 2.5}))
