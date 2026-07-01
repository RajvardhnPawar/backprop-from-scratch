import math

class Value:
    def __init__(self,data,_children=(),_op='',label=''):
        self.data = data
        self._prev = set(_children)
        self.grad = 0.0
        self._backward = lambda: None
        self._op = _op
        self.label = label
    
    def __repr__(self):
        return f"Value(data={self.data})"
    
    def __add__(self,other):
        out = Value(self.data + other.data,(self,other),'+')
        def _backward():
            self.grad += 1 * out.grad
            other.grad += 1* out.grad 
        out._backward = _backward
        return out

    def __mul__(self,other):
        out = Value(self.data * other.data,(self,other),'*')
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad 
        out._backward = _backward
        return out

    def tanh(self):
        x = self.data
        t = (math.exp(2*x)-1) / (math.exp(2*x)+1)
        out = Value(t,(self,),'tanh')
        def _backward():
            self.grad += (1 - (t**2)) * out.grad
        out._backward = _backward
        return out
    
    def backward(self):
        #topological sort
        node_values = []
        visted  = set()
        def get_val(x):
            if x not in visted:
                visted.add(x)
                for v in x._prev:
                    get_val(v)
                node_values.append(x)
        get_val(self)

        #add gradient for each node
        self.grad = 1.00
        for n in reversed(node_values):
            n._backward()

