import pandas as pd
import matplotlib.pyplot as plt
from typing import Union, List

# for testing
FILEPATH = r"[PATH]/Download Data - STOCK_US_XNAS_TSLA.csv"
df = pd.read_csv(FILEPATH)
null = df.isnull() # check null -> None

# simple getters
def get_dates(frame: pd.DataFrame) -> List:
    return frame['Date'].tolist()

def get_open(frame: pd.DataFrame) -> List:
    return frame['Open'].tolist()

def get_high(frame: pd.DataFrame) -> List:
    return frame['High'].tolist()

def get_low(frame: pd.DataFrame) -> List:
    return frame['Low'].tolist()

# For data readability
class Data:
    def __init__(self):
        self.time = len(get_dates(df))
        self.X = range(1, self.time + 1)
        self.openl = get_open(df)[::-1]
        self.highl = get_high(df)[::-1]
        self.lowl = get_low(df)[::-1]
        self.df = df

    # helper function
    def str_convert(self, str_metric: str) -> List:
        if str_metric == "open":
            return self.openl
        elif str_metric == "high":
            return self.highl
        elif str_metric == "low":
            return self.lowl 

    # build visual
    def visualize(self, metrics: List[str], plotsame=True) -> None:
        '''Metrics include Open, High, Low.
        Plotsame is True to plot listed metrics on one plot.'''
        # clean 
        for m in metrics:
            m.lower().strip()

        # use common graph
        if (plotsame):
            for m in metrics:
                metric_list = self.str_convert(m)
                print(m)
                plt.plot(self.X, metric_list, label=m)
                
        # use subplots
        else:
            num_metrics = len(metrics)
            fig, axs = plt.subplots(num_metrics)
            for i in range(num_metrics):
                axs[i] = axs.plot(self.X, self.str_convert(m[i]))
            
        plt.legend()
        plt.show()
    



        
        
    



