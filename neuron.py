from core.value import Value
from core.graph import draw_dot

# input of x1,x2
x1 = Value(2.00,label='x1')
x2 = Value(0.0,label='x2')

#weight w1,w2
w1 = Value(-3.0,label='w1')
w2 = Value(1.0,label='w2')

#bais of neuron
b = Value(8,label='b')

x1w1= x1*w1; x1w1.label='x1w1'
x2w2= x2*w2; x2w2.label='x2w2'
x1w1x2w2= x1w1 + x2w2; x1w1x2w2.label='x1*w1 + x2*w2'
n = x1w1x2w2 + b; n.label = 'n'

o = n.tanh()
draw_dot(o)
print(o)