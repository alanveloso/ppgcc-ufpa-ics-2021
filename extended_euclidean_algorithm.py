'''
Extended Euclidean Algorithm
----------------------------

This algorithm determined the greatest common divisor (GCD) of two integers 
(​numbers). Also, It returns two integers such that GCD(a, b) = xa + by.


@author: @alanveloso
'''

def gcd(a, b):
    ''' Run extended euclidean algorithm.
    Parameters
    ----------
    a : int
    b : int
    
    Returns
    -------
    int
        the greatest common divisor
    int
        x in GCD(a, b) = xa + by
    int
        y in GCD(a, b) = xa + by
    '''
    if (b <= 0) or (a <=0):
        raise ValueError("Expected values greater than zero!")
    if (a < b):
        raise ValueError("The second value must be greater or equal than the first!")

    x = 1 
    y = 0 
    g = a
    r = 0
    s = 1
    t = b
    while (t > 0):
        q = g//t
        u =  x - q*r
        v = y - q*s
        w = g - q*t
        x, y, g = r, s, t
        r, s, t = u, v, w
    return  g, x, y