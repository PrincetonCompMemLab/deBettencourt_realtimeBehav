import sys
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np


#default plotting function

def make_plot_pretty(ax,xt=None,xtl=None,xl=None,ylim=None,yt=None,yl=None,ytl=None,xlim=None,ylrot=None,t=None,legend=None):
    
    if sys.platform == 'darwin'
        if os.path.isfile("/Library/Fonts/HelveticaNeue.ttf"): 
            prop = fm.FontProperties(fname="/Library/Fonts/HelveticaNeue.ttf")
        else:
            prop = fm.FontProperties(fname="/Library/Fonts/Arial.ttf") 
    else:
        prop = fm.FontProperties()  
        
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['bottom'].set_color("gray")
    ax.spines['left'].set_linewidth(1)
    ax.spines['left'].set_color("gray")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.yaxis.set_ticks_position("left")   
    ax.tick_params(axis='y',direction='out',length=5,width=1,color='gray')
    ax.xaxis.set_ticks_position("bottom") 
    ax.tick_params(axis='x',direction='out',length=5,width=1,color='gray')
    
    if yt is not None: ax.set_yticks(yt)
    if ytl is not None: ax.set_yticklabels((ytl),fontsize=12,fontproperties=prop)    
    if yl is not None: h = ax.set_ylabel(yl,fontsize=14,fontproperties=prop,labelpad=5)
    if ylim is not None: ax.set_ylim(ylim) 
        
    if xt is not None: ax.set_xticks(xt)
    if xtl is not None: ax.set_xticklabels((xtl),fontsize=12,fontproperties=prop)
    if xl is not None: ax.set_xlabel(xl,fontsize=14,fontproperties=prop)
    if xlim is not None: ax.set_xlim(xlim)
    
    if t is not None: ax.set_title(t,y=1.08)
    if legend is not None: ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),prop=prop)

    ax.tick_params(axis='both',pad=5)
    plt.locator_params(nbins=5)
    plt.tight_layout()

def savefig(fig,name):
    fig.savefig("figures/{}.pdf".format(name))

def plotSpread(x,y):
    xtol=.03
    ytol=.03
    sp = .031#must be greater than xtol or ytol
    x_swarm=np.zeros(np.size(x))
    b = np.arange(0,np.size(x))
    for a in range(0,np.size(x)):
        c=np.setdiff1d(b,a)
        if any(np.sqrt((y[a]-y[c])**2)<ytol):
            inds=np.where(np.sqrt((y[a]-y[c])**2)<ytol)
            inds = np.append(c[inds[0]],a)
            indsmat=np.tile(x_swarm[inds],(np.size(inds),1))          
            indsmatt=np.transpose(indsmat)
            indsmatdist=np.sqrt((indsmat-indsmatt)**2)
            indsmatdist[np.triu_indices(np.size(inds))]=1
            i,j =np.where((indsmatdist<=xtol)==True)
            k = np.union1d(i,j)
            x_swarm[inds[k]]=x_swarm[inds[k]]+(np.arange(0,np.size(k))+.5-float(np.size(k))/2)*sp

    return x_swarm,a,b
