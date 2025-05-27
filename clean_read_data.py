import pandas as pd

FILEPATH = r"C:/Users/phillip.korolev/Documents/pytests/blackscholes/Download Data - STOCK_US_XNAS_TSLA.csv"

df = pd.read_csv(FILEPATH)
null = df.isnull()
# check null -> None

# simple getters -> list
def get_dates(frame):
    return frame['Date'].tolist()

def get_open(frame):
    return frame['Open'].tolist()

def get_high(frame):
    return frame['High'].tolist()

def get_low(frame):
    return frame['Low'].tolist()

import matplotlib.pyplot as plt
class Data:
    def __init__(self):
        self.time = len(get_dates(df))
        self.X = range(1, self.time + 1)
        self.openl = get_open(df)[::-1]
        self.highl = get_high(df)[::-1]
        self.lowl = get_low(df)[::-1]
        self.df = df
    
    def str_convert(self, str_metric: str):
        if str_metric == "open":
            return self.openl
        elif str_metric == "high":
            return self.highl
        elif str_metric == "low":
            return self.lowl 

    def visualize(self, metrics: list[str], plotsame=True):
        '''Metrics include Open, High, Low.
        Plotsame is True to plot listed metrics on one plot.'''
        # clean 
        for m in metrics:
            m.lower().strip()

        if (plotsame):
            for m in metrics:
                metric_list = self.str_convert(m)
                print(m)
                plt.plot(self.X, metric_list, label=m)
        else:
            num_metrics = len(metrics)
            fig, axs = plt.subplots(num_metrics)
            for i in range(num_metrics):
                axs[i] = axs.plot(self.X, self.str_convert(m[i]))
            
        plt.legend()
        plt.show()
    

data = Data()
data.visualize(["open", "low", "high"])


        
        
    



