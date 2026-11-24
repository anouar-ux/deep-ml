import numpy as np

def disorder(apples: list) -> float:
    """
    Compute the disorder in a basket of apples.
    """
    if len(apples)==0:
        return None

    D={}

    for k in apples:
        if k in D:
            D[k]+=1
        else:
            D[k]=1
    S=0
    for k in D.values():
        S+=k
    
    p=np.array([k/S for k in D.values()])

    return 1-np.sum(p**2)