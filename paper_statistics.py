import os
import numpy as np
import scipy
import matplotlib.pyplot as plt
from paper_plotting import make_plot_pretty


#compute nonparametric resampling statistics
def resamplingStatistics(data,chance,nSubj,nSamples,skipfig=None):
    #resample subjects with replacement 100,000 times
    resampledSubj = np.random.randint(0,nSubj,(nSamples,nSubj)) 

    #preallocate variables
    resampledData = np.empty(nSamples)

    #recalculate mean A' given the resampled subjects
    for i in range(0,nSamples): resampledData[i] = np.mean(data[resampledSubj[i,:]])

    #calculate p value 
    p = np.sum(np.less(resampledData,chance))/float(nSamples) #count number of resample iterations below chance
    if np.equal(p,0): p = 1./float(nSamples)

    if skipfig is None:
        plt.figure(figsize=(4,3))
        ax = plt.subplot(111)
        plt.hist(resampledData,normed=0,facecolor='gray',edgecolor='gray')
        plt.axvline(np.mean(resampledData),color='b',lw=2,label='resampled mean')
        plt.axvline(np.mean(data),color='m',lw=1,label='original mean')
        plt.axvline(chance,color='c',lw=2,label='chance')
        make_plot_pretty(ax,ylrot=90,yl='Count (#)',legend='1') 
        plt.show()
    
    return resampledData, p


#test for normality & perform parametric statistics
def paramStatistics(data,chance):

    #perform the Shapiro-Wilk test for normality
    [sw_w,sw_p] = scipy.stats.shapiro(data)

    #significance threshold
    alpha = .05
    
    #compare to significance threshold
    if np.less(sw_p,.05): print "Rejects the null hypothesis that the data is normally distributed, p = %.2E" %sw_p
    else: print "Fails to reject the null hypothesis that the data is normally distributed, p = %.2f" %sw_p

    [t,p] = scipy.stats.ttest_1samp(data,chance)

    print("Parametric statistical result: T = %.1f, p = %.1E" % (t, p))