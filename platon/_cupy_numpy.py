try:
    from cupy import *
    from cupyx import scipy
except:
    print("cupy not found. Disabling GPU acceleration")
    from numpy import *
    import scipy
    import scipy.special
    
def cpu(arr):
    try:
        return arr.get()
    except:
        return arr
