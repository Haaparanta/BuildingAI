import math
import random
import numpy as np
import io
from io import StringIO
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # Write your recursive code here
    if len(ports) == 0:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            route.append(ports[i])
            permutations(route, ports[:i]+ports[i+1:])
            route.pop()
    
# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))