# import packages: numpy, math (you might need pi for gaussian functions)
import numpy as np
import math
from math import *
import matplotlib.pyplot as plt
from scipy.signal import convolve2d as conv2
import scipy


"""
Gaussian function taking as argument the standard deviation sigma
The filter should be defined for all integer values x in the range [-3sigma,3sigma]
The function should return the Gaussian values Gx computed at the indexes x
"""
#returns gaussian vector applied on sigma
def gauss(sigma):
    r = range(-int(3*sigma), int(3*sigma))
    return [1 / (sigma * sqrt(2*pi)) * exp(-float(x)**2/(2*sigma**2)) for x in r], r

#returns gaussian kernel on sigma
def gauss_kernel(sigma):
    vector, _ = gauss(sigma)
    kernel = np.outer(vector,vector)
    return kernel

"""
Implement a 2D Gaussian filter, leveraging the previous gauss.
Implement the filter from scratch or leverage the convolve2D method (scipy.signal)
Leverage the separability of Gaussian filtering
Input: image, sigma (standard deviation)
Output: smoothed image
"""
#returns expected result 
def expected_result_GF(im2d, sigma):
    return scipy.ndimage.gaussian_filter(im2d, sigma)

#basic implementation using gaussian kernel
def gaussianfilter(im2d, sigma):
    return conv2(im2d, gauss_kernel(sigma))

#faster implementation using gaussian filter separability
def gaussianfilter_fast_impl(im2d, sigma):
    out = np.zeros(im2d.shape, dtype=im2d.dtype)
    [Gx, _] = gauss(sigma)
    for row in range(im2d.shape[0]):
            out[row,:] = np.convolve(im2d[row,:], Gx, mode='same')
    for col in range(im2d.shape[1]):
            out[:,col] = np.convolve(out[:,col], Gx, mode='same')
    return out



"""
Gaussian derivative function taking as argument the standard deviation sigma
The filter should be defined for all integer values x in the range [-3sigma,3sigma]
The function should return the Gaussian derivative values Dx computed at the indexes x
"""
def gaussdx(sigma):
    r = range(-int(3*sigma), int(3*sigma))
    return [1 / (sigma**3 * sqrt(2*pi)) * x * exp(-float(x)**2/(2*sigma**2)) for x in r], r



def gaussderiv(img, sigma):

    #...
    
    return imgDx, imgDy

