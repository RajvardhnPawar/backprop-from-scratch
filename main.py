from core import Value

#y = mx + c ( my own example)
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

#andrej video example
def lol_2():
    a = Value(2.0,label='A')
    b = Value(-3.0,label='B')
    c = Value(10.0,label='C')
    e = a * b; e.label = 'E'
    d = e + c; d.label= 'D'
    f = Value(-2.0,label='F')
    l = d * f; l.label = 'L'

    # dl/dl
    print(f"dl/dl: {((l.data + h)-(l.data))/h}")

    #dl/dd
    dl_dd = (((d.data + h) * f.data) - (d.data * f.data))/h
    print(f"dl/dd: {dl_dd}")

    #dl/de
    #dl/de = dl/dd * dd/de
    dd_de = ((e.data+h +c.data) - (e.data + c.data))/h
    dl_de = dl_dd * dd_de
    print(f"dl/de: {dl_de}")

   # dL/da
    de_da = (((a.data + h) * b.data) - (a.data * b.data)) / h
    dl_da = dl_dd * dd_de * de_da
    print(f"dL/da: {dl_da}")

    #dl/db
    de_db = ((a.data * (b.data + h)) - (a.data * b.data)) / h
    dl_db = dl_dd * dd_de * de_db
    print(f"dl/db: {dl_db}")

    #dl/dc
    #dl/dc = dl/dd * dd/dc
    dd_dc = ((e.data + (c.data +h)) - (e.data + c.data))/h
    dl_dc = dl_dd * dd_dc
    print(f"dl/dc: {dl_dc}")

     #dl/dd
    dl_df = ((d.data * (f.data +h)) - (d.data * f.data))/h
    print(f"dl/df: {dl_df}")

    dl_dl= 1.000000000000334
    dl_dd= -2.000000000000668
    dl_de= -2.000000000001336
    dl_da= 6.000000000004235
    dl_db= -4.000000000002231
    dl_dc= -1.9999999999995595
    dl_df= 3.9999999999995595


    h = 0.001

    a.grad = dl_da
    b.grad = dl_db
    c.grad = dl_dc
    f.grad = dl_df


    a.data += 0.01 * a.grad
    b.data += 0.01 * b.grad
    c.data += 0.01 * c.grad
    f.data += 0.01 * f.grad

    e = a * b
    d = e + c
    l = d * f

    print(l.data)