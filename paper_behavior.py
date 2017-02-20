import numpy as np
import scipy

#determine the frequent category 
#note: which category was frequent vs. infrequent category was counterbalanced across subjects

def find_freq_categ(categs):
    modeCategs = scipy.stats.mode(categs,axis=None)
    freqCateg = modeCategs[0]
    infreqCateg = freqCateg % 2 + 1
    return freqCateg, infreqCateg


#convert keycode response to memory confidence scale
def convertKey2Resp(key):
    if (key==30) or (key==49): return 1
    if (key==31) or (key==50): return 2
    if (key==32) or (key==51): return 3
    if (key==33) or (key==52): return 4
    else: return 0

#calculate sensitivity via aprime formula
@np.vectorize
def aprime(h,fa):
    if np.greater_equal(h,fa): a = .5 + (((h-fa) * (1+h-fa)) / (4 * h * (1-fa)))
    else: a = .5 - (((fa-h) * (1+fa-h)) / (4 * fa * (1-h)))
    return a
