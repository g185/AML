import numpy as np
import matplotlib.pyplot as plt

import histogram_module
import dist_module
import match_module



# compute and plot the recall/precision curve
#
# D - square matrix, D(i, j) = distance between model image i, and query image j
#
# note: assume that query and model images are in the same order, i.e. correct answer for i-th query image is the i-th model image

def plot_rpc(D, plot_color):
    
    recall = []
    precision = []
    num_queries = D.shape[1]
    
    num_images = D.shape[0]
    assert(num_images == num_queries), 'Distance matrix should be a square matrix'
    
    labels = np.diag([1]*num_images)
    d = D.reshape(D.size)
    l = labels.reshape(labels.size)
     
    sortidx = d.argsort()
    d = d[sortidx]
    l = l[sortidx]
    
    tp = 1
    fp = 0
    fn = 0

    tresh = np.linspace(0,1,20)
    
    for t in tresh:

        for idt in range(len(d)):
            tp += 1 if l[idt] == 1 and d[idt] < t else 0
            fp += 1 if l[idt] != 1 and d[idt] < t else 0
            fn += 1 if l[idt] == 1 and d[idt] > t else 0
            
            
        #Compute precision and recall values and append them to "recall" and "precision" vectors
        recall.append(tp/(tp+fn))
        precision.append(tp/(tp+fp))
        tp, fp, fn = 1,0,0     

    
    plt.plot([1-precision[i] for i in range(len(precision))], recall, plot_color+'-')



def compare_dist_rpc(model_images, query_images, dist_types, hist_type, num_bins, plot_colors):
    
    assert len(plot_colors) == len(dist_types), 'number of distance types should match the requested plot colors'

    for idx in range( len(dist_types) ):

        [best_match, D] = match_module.find_best_match(model_images, query_images, dist_types[idx], hist_type, num_bins)

        plot_rpc(D, plot_colors[idx])
    
    print("as")
    plt.axis([0, 1, 0, 1]);
    plt.xlabel('1 - precision');
    plt.ylabel('recall');
    
    # legend(dist_types, 'Location', 'Best')
    
    plt.legend( dist_types, loc='best')





