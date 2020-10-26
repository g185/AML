import numpy as np
import math



# Compute the intersection distance between histograms x and y
# Return 1 - hist_intersection, so smaller values correspond to more similar histograms
# Check that the distance range in [0,1]
  
def dist_intersect(x,y):
    
    intersection = np.minimum(x,y)
    sum_x = x.sum()
    sum_y = y.sum()
    
    dist = ((intersection.sum()/sum_x) + (intersection.sum()/sum_y)) /2
    if dist >= 0 and dist <=1:
        return (1-dist)
    else:
        raise ValueError('distance not in 0 - 1')




# Compute the L2 distance between x and y histograms
# Check that the distance range in [0,sqrt(2)]

def dist_l2(x,y):
    
    dist = np.power(x-y, 2)
    sum_dist = dist.sum()
    
    if sum_dist >= 0 and sum_dist <= np.sqrt(2):
        return sum_dist
    else:
        raise ValueError('distance not in 0 - sqrt(2)')



# Compute chi2 distance between x and y
# Check that the distance range in [0,Inf]
# Add a minimum score to each cell of the histograms (e.g. 1) to avoid division by 0

def dist_chi2(x,y):
    x = x+1
    y = y+1
    
    dist = (np.power(x-y,2)/(x+y)).sum()
    
    if dist>0:
        return dist
    else:
        raise ValueError('distance not range in [0,Inf] ')



def get_dist_by_name(x, y, dist_name):
  if dist_name == 'chi2':
    return dist_chi2(x,y)
  elif dist_name == 'intersect':
    return dist_intersect(x,y)
  elif dist_name == 'l2':
    return dist_l2(x,y)
  else:
    assert False, 'unknown distance: %s'%dist_name
  




