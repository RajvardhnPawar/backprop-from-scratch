class Value:
    def __init__(self,data,_children=(),_op='',label=''):
        self.data = data
        self._prev = set(_children)
        self.grad = 0.0
        self._op = _op
        self.label = label
    
    def __repr__(self):
        return f"Value(data={self.data})"
    
    def __add__(self,other):
        out = Value(self.data + other.data,(self,other),'+')
        return out

    def __mul__(self,other):
        out = Value(self.data * other.data,(self,other),'*')
        return out

def lol():
    h = 0.001 

    m = Value(2.00,label='M')
    x = Value(5.00,label='X')
    c = Value(10.00,label='C')
    a = m * x; a.label='A'
    b = a + c; b.label='B'
    y1 = b.data
    y2 = b.data + h 

    #dy/dy = 1 ( grad of y)
    print(f"grad of y: {(y2-y1)/h}")

    #dy/db = 1 ( grad of b)
    print(f"grad of b: {((b.data + h)-b.data)/h}")

    #dy/da = dy/db * db/da
    dy_db = ((b.data + h) - (b.data))/h  #1
    db_da = ((a.data + h + c.data) - (a.data + c.data)) / h 
    dy_da = dy_db * db_da
    print(f"grad of a: {dy_da}")

    #dy/dm = dy/db * db/da * da/dm
    da_dm = (((m.data + h)* x.data) - (m.data*x.data))/h
    dy_dm = dy_db * db_da * da_dm
    print(f"grad of m: {dy_dm}")

    #dy/dx = dy/db * db/da * da/dx
    da_dx = ((m.data* (x.data +h)) - (m.data*x.data))/h
    dy_dx = dy_db * db_da * da_dx
    print(f"grad of x: {dy_dx}")

    print(f"grad of c: {1.000:.4f}")

lol()