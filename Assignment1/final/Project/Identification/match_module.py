import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import histogram_module
import dist_module

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray



# model_images - list of file names of model images
# query_images - list of file names of query images
#
# dist_type - string which specifies distance type:  'chi2', 'l2', 'intersect'
# hist_type - string which specifies histogram type:  'grayvalue', 'dxdy', 'rgb', 'rg'
#
# note: use functions 'get_dist_by_name', 'get_hist_by_name' and 'is_grayvalue_hist' to obtain 
#       handles to distance and histogram functions, and to find out whether histogram function 
#       expects grayvalue or color image

def find_best_match(model_images, query_images, dist_type, hist_type, num_bins):

    hist_isgray = histogram_module.is_grayvalue_hist(hist_type)
    
    model_hists = compute_histograms(model_images, hist_type, hist_isgray, num_bins)
    query_hists = compute_histograms(query_images, hist_type, hist_isgray, num_bins)


    D = np.zeros((len(query_images), len(model_images)))
        
    for i in range(len(query_images)):
        for j in range(len(model_images)):
            D[i][j] = dist_module.get_dist_by_name( model_hists[j], query_hists[i], dist_type)
            
    best_match = np.argmin(D, axis=0)
    return best_match, D



def compute_histograms(image_list, hist_type, hist_isgray, num_bins):
    
    image_hist = []

    # Compute histogram for each image and add it at the bottom of image_hist

    for i in image_list:
        if hist_isgray == True:
            img = rgb2gray(np.array(Image.open(i)).astype('double'))
        else:
            img = np.array(Image.open(i)).astype('double')
            
        hist = histogram_module.get_hist_by_name(img, num_bins, hist_type)
        image_hist.append(hist)
            

    return image_hist



# For each image file from 'query_images' find and visualize the 5 nearest images from 'model_image'.
#
# Note: use the previously implemented function 'find_best_match'
# Note: use subplot command to show all the images in the same Python figure, one row per query image

def show_neighbors(model_images, query_images, dist_type, hist_type, num_bins):
    
    _, D = find_best_match(model_images,query_images, dist_type, hist_type, num_bins)

    num_nearest = 5  # show the top-5 neighbors
    
    top_k = np.zeros((len(query_images), 5), dtype = int)

    for i in range(len(query_images)):
        
        top_k[i] = np.argsort(D[i])[:5]
        
        plt.figure()
        plt.subplot(1,6,1); plt.imshow(np.array(Image.open(query_images[i])), vmin=0, vmax=255); plt.title(query_images[i])
        plt.subplot(1,6,2); plt.imshow(np.array(Image.open(model_images[top_k[i][0]]))); plt.title(model_images[top_k[i][0]])
        plt.subplot(1,6,3); plt.imshow(np.array(Image.open(model_images[top_k[i][1]]))); plt.title(model_images[top_k[i][1]])
        plt.subplot(1,6,4); plt.imshow(np.array(Image.open(model_images[top_k[i][2]]))); plt.title(model_images[top_k[i][2]])
        plt.subplot(1,6,5); plt.imshow(np.array(Image.open(model_images[top_k[i][3]]))); plt.title(model_images[top_k[i][3]])
        plt.subplot(1,6,6); plt.imshow(np.array(Image.open(model_images[top_k[i][4]]))); plt.title(model_images[top_k[i][4]])
        plt.show()

