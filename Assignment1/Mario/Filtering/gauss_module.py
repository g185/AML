# import packages: numpy, math (you might need pi for gaussian functions)
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import convolve2d as conv2



"""
Gaussian function taking as argument the standard deviation sigma
The filter should be defined for all integer values x in the range [-3sigma,3sigma]
The function should return the Gaussian values Gx computed at the indexes x
"""
def gauss(sigma):
    
    r = range(-int(3*sigma),int(3*sigma)+1)
    x = []
    Gx = []
    for i in r:
        data = [1 / (sigma * sqrt(2*pi)) * exp(-float(i)**2/(2*sigma**2))]
        Gx.append(data)
        x.append(i)
        
    Gx = np.array(Gx)
    x = np.array(x)
        
    
    return Gx, x


"""
Implement a 2D Gaussian filter, leveraging the previous gauss.
Implement the filter from scratch or leverage the convolve2D method (scipy.signal)
Leverage the separability of Gaussian filtering
Input: image, sigma (standard deviation)
Output: smoothed image
"""
def gaussianfilter(img, sigma):
    
    '''
    Reimplementing GAUSS this time without returning the value of X, in the way that it will not create a shape that is
    not supported by the algorithm
    '''
                    
    r = range(-int(3*sigma),int(3*sigma)+1)

    Gx = []
    for i in r:
        data = [1 / (sigma * sqrt(2*pi)) * exp(-float(i)**2/(2*sigma**2))]
        Gx.append(data)

    Gx = np.array(Gx)

     
    smooth_img = signal.convolve2d(Gx, img, boundary='symm', mode='valid')
    return smooth_img



"""
Gaussian derivative function taking as argument the standard deviation sigma
The filter should be defined for all integer values x in the range [-3sigma,3sigma]
The function should return the Gaussian derivative values Dx computed at the indexes x
"""
def gaussdx(sigma):

    r = range(-int(3*sigma),int(3*sigma)+1)
    x = []
    Dx = []
    for i in r:
        data = (-1 / (sigma**3 * sqrt(2*pi))* i * exp(-float(i)**2/(2*sigma**2)))
        Dx.append(data)
        x.append(i)
    
    Dx = np.array(Dx)
    x = np.array(x)


    return Dx, x



def gaussderiv(im2d, sigma):
    imgDy = np.zeros(im2d.shape, dtype=im2d.dtype)
    imgDx = np.zeros(im2d.shape, dtype=im2d.dtype)
    [Gx, x] = gauss(sigma)
    [Dx, x] = gaussdx(sigma)
    
    Gx = Gx.reshape(1, Gx.size)
    Dx = Dx.reshape(1, Dx.size)
    imgDx = conv2(conv2(im2d, Gx, 'same'), Dx.T, 'same')
    imgDy = conv2(conv2(im2d, Dx, 'same'), Gx.T, 'same')

    return imgDx, imgDy

