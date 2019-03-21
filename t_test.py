import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

class t_test_demo:
    
    def __init__(self, df, alpha, top_yaxis, tail, reject):

        #define the paras
        self.df        = df
        self.alpha     = alpha
        self.top_yaxis = top_yaxis
        self.tail      = tail
        self.reject    = reject
        
    def t_pvalue_plot(self):
          
        if self.tail=='Two' :
            ## Calculate critical t-score
            tcrit = abs(st.t.ppf(self.alpha/2, self.df))
            
            plt.figure()
            xs = np.linspace(-5,5,100)
            plt.plot(xs, st.t.pdf(xs,self.df), 'b', linewidth=3)
    
            ## Plot some vertical lines representing critical t-score cutoff
            plt.axvline(x=   tcrit, color='g', linewidth=3, linestyle='--')           
            plt.axvline(x=-1*tcrit, color='g', linewidth=3, linestyle='--', label="-1 * |t-stat| and |t-stat|")
    
            section_1 = np.arange(tcrit, 5, 1/20.)
            plt.fill_between(section_1, abs(st.t.pdf(section_1, self.df)), color='lawngreen')
            section_2 = np.arange(-5, -1*tcrit, 1/20.)
            plt.fill_between(section_2, abs(st.t.pdf(np.abs(section_2), self.df)), color='lawngreen',label="two-tail p-value")
    
            plt.xlim(-5,5)
            plt.ylim(0,self.top_yaxis)
            
            plt.title("t distibution: two-tail p-value")
            plt.legend(bbox_to_anchor=(1.0,1.0))
            plt.show()
            
        if self.tail=='Left':
            ## Calculate critical t-score
            tcrit = abs(st.t.ppf(self.alpha, self.df))
            
            plt.figure()
            xs = np.linspace(-5,5,100)
            plt.plot(xs, st.t.pdf(xs,self.df), 'b', linewidth=3)
    
            ## Plot some vertical lines representing critical t-score cutoff
            plt.axvline(x=tcrit, color='g', linewidth=3, linestyle='--', label="t-stat")

            section_2 = np.arange(-5, tcrit, 1/20.)
            plt.fill_between(section_2, abs(st.t.pdf(np.abs(section_2), self.df)), color='lawngreen',label="left-tail p-value")
    
            plt.xlim(-5,5)
            plt.ylim(0,self.top_yaxis)
            
            plt.title("t distibution: left-tail p-value")
            plt.legend(bbox_to_anchor=(1.0,1.0))
            plt.show()
            
        if self.tail=='Right' :
            ## Calculate critical t-score
            tcrit = abs(st.t.ppf(self.alpha, self.df))
            
            plt.figure()
            xs = np.linspace(-5,5,100)
            plt.plot(xs, st.t.pdf(xs,self.df), 'b', linewidth=3)
    
            ## Plot some vertical lines representing critical t-score cutoff
            plt.axvline(x= -1*tcrit, color='g', linewidth=3, linestyle='--', label="t-stat")
            
            section_1 = np.arange(-1*tcrit, 5, 1/20.)
            plt.fill_between(section_1, abs(st.t.pdf(section_1, self.df)), color='lawngreen',label="right-tail p-value")
    
            plt.xlim(-5,5)
            plt.ylim(0,self.top_yaxis)
            plt.title("t distibution: right-tail p-value")
            plt.legend(bbox_to_anchor=(1.0,1.0))
            plt.show()
            
    def t_plot(self):
          
        if self.tail=='Two' :
            ## Calculate critical t-score
            tcrit = abs(st.t.ppf(self.alpha/2, self.df))
            
            plt.figure()
            xs = np.linspace(-5,5,100)
            plt.plot(xs, st.t.pdf(xs,self.df), 'b', linewidth=3)
    
            ## Plot some vertical lines representing critical t-score cutoff
            plt.axvline(x=   tcrit, color='k', linewidth=3, linestyle='--', label="right-tail cutoff point")
            plt.axvline(x=-1*tcrit, color='r', linewidth=3, linestyle='--', label="left-tail cutoff point")
    
            section_0 = np.arange(-1*tcrit, tcrit, 1/20.)
            plt.fill_between(section_0, abs(st.t.pdf(section_0, self.df)), color='skyblue',label="non-rejection region")
            section_1 = np.arange(tcrit, 5, 1/20.)
            plt.fill_between(section_1, abs(st.t.pdf(section_1, self.df)), color='orangered')
            section_2 = np.arange(-5, -1*tcrit, 1/20.)
            plt.fill_between(section_2, abs(st.t.pdf(np.abs(section_2), self.df)), color='orangered',label="rejection region")
    
            plt.xlim(-5,5)
            plt.ylim(0,self.top_yaxis)
            
            if self.reject == 'True-Right':
                plt.axvline(x= tcrit + 1, color='g', linewidth=3, linestyle='--', label="t-stat")
                plt.title("t distibution: reject H0")
            elif self.reject == 'True-Left':
                plt.axvline(x= -1*tcrit - 1, color='g', linewidth=3, linestyle='--', label="t-stat")
                plt.title("t distibution: reject H0")
            else:
                plt.axvline(x= tcrit - 1, color='g', linewidth=3, linestyle='--', label="t-stat")
                plt.title("t distibution: not to reject H0")
            plt.legend(bbox_to_anchor=(1.0,1.0))
            plt.show()
            
        if self.tail=='Left':
            ## Calculate critical t-score
            tcrit = abs(st.t.ppf(self.alpha, self.df))
            
            plt.figure()
            xs = np.linspace(-5,5,100)
            plt.plot(xs, st.t.pdf(xs,self.df), 'b', linewidth=3)
    
            ## Plot some vertical lines representing critical t-score cutoff
            plt.axvline(x=-1*tcrit, color='r', linewidth=3, linestyle='--', label="left-tail cutoff point")
    
            section_0 = np.arange(-1*tcrit, 5, 1/20.)
            plt.fill_between(section_0, abs(st.t.pdf(section_0, self.df)), color='skyblue',label="non-rejection region")
            section_2 = np.arange(-5, -1*tcrit, 1/20.)
            plt.fill_between(section_2, abs(st.t.pdf(np.abs(section_2), self.df)), color='orangered',label="rejection region")
    
            plt.xlim(-5,5)
            plt.ylim(0,self.top_yaxis)
            
            if self.reject == 'True':
                plt.axvline(x= -1*tcrit - 1, color='g', linewidth=3, linestyle='--', label="t-stat")
                plt.title("t distibution: reject H0")
            else:
                plt.axvline(x= -1*tcrit + 1, color='g', linewidth=3, linestyle='--', label="t-stat")
                plt.title("t distibution: not to reject H0")
            plt.legend(bbox_to_anchor=(1.0,1.0))
            plt.show()
            
        if self.tail=='Right' :
            ## Calculate critical t-score
            tcrit = abs(st.t.ppf(self.alpha, self.df))
            
            plt.figure()
            xs = np.linspace(-5,5,100)
            plt.plot(xs, st.t.pdf(xs,self.df), 'b', linewidth=3)
    
            ## Plot some vertical lines representing critical t-score cutoff
            plt.axvline(x=   tcrit, color='k', linewidth=3, linestyle='--', label="right-tail cutoff point")
            
            section_0 = np.arange(-5, tcrit, 1/20.)
            plt.fill_between(section_0, abs(st.t.pdf(section_0, self.df)), color='skyblue',label="non-rejection region")
            section_1 = np.arange(tcrit, 5, 1/20.)
            plt.fill_between(section_1, abs(st.t.pdf(section_1, self.df)), color='orangered',label="rejection region")
    
            plt.xlim(-5,5)
            plt.ylim(0,self.top_yaxis)
            
            if self.reject == 'True':
                plt.axvline(x= tcrit + 1, color='g', linewidth=3, linestyle='--', label="t-stat")
                plt.title("t distibution: reject H0")
            else:
                plt.axvline(x= tcrit - 1, color='g', linewidth=3, linestyle='--', label="t-stat")
                plt.title("t distibution: not to reject H0")
            
            plt.legend(bbox_to_anchor=(1.0,1.0))
            plt.show()