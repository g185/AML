import numpy as np
import math



# Compute the intersection distance between histograms x and y
# Return 1 - hist_intersection, so smaller values correspond to more similar histograms
# Check that the distance range in [0,1]

def dist_intersect(x,y):
  
  if len(x) == len(y):
        
      intersection = np.zeros(len(x))
      for i in range(len(x)):
          if x[i] <= y[i]:
              intersection[i] = x[i]
          elif x[i] >= y[i]:
              intersection[i] = y[i]
  else:
      print("Error! Histograms with different shapes")
        
  dist = ((intersection.sum()/x.sum()) + (intersection.sum()/y.sum())) /2
  if dist >= 0 and dist <=1:
      return (1-dist)
  else:
      raise ValueError('distance not in in 0-1')




# Compute the L2 distance between x and y histograms
# Check that the distance range in [0,sqrt(2)]

def dist_l2(x,y):
    
    #... (your code here)



# Compute chi2 distance between x and y
# Check that the distance range in [0,Inf]
# Add a minimum score to each cell of the histograms (e.g. 1) to avoid division by 0

def dist_chi2(x,y):
    
    #... (your code here)



def get_dist_by_name(x, y, dist_name):
  if dist_name == 'chi2':
    return dist_chi2(x,y)
  elif dist_name == 'intersect':
    return dist_intersect(x,y)
  elif dist_name == 'l2':
    return dist_l2(x,y)
  else:
    assert False, 'unknown distance: %s'%dist_name
  




