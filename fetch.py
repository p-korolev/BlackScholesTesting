import math
import numpy as np
import pandas as pd
from scipy.stats import norm
from typing import Union, List

# helpers
def get_variance(dataset: Union[List, pd.Series) -> np.float64:
    length = len(dataset)
    if length<2:
        return None
    average_value = sum(dataset)/length
    s = 0
    for val in dataset:
        s += (val - average_value)**2
    variance = s/(length-1)
    return np.float64(variance)

# get standard deviation (volatility)
def get_sd(dataset: Union[List, pd.Series]) -> np.float64:
    variance = get_variance(dataset)
    return math.sqrt(variance)

# Black-Scholes model
def calculte_call_price(curr_price: Union[float, np.float64, int, np.int64], 
                        strike_price: Union[float, np.float64, int, np.int64],
                        rf_interest: Union[float, np.float64, int, np.int64],
                        variance: Union[float, np.float64, int, np.int64],
                        days_to_maturity: int) -> np.float64:
    # final formula helpers
    sdt = math.sqrt(variance)*math.sqrt(days_to_maturity)
    d1 = ((math.log(curr_price/strike_price)) + (rf_interest + (variance/2))*days_to_maturity)/sdt
    d2 = d1 - sdt
    norm_d1, norm_d2 = norm.cdf(d1), norm_d2 = norm.cdf(d2)

    # call option price
    call_price = (curr_price*norm_d1) - (strike_price*math.exp((-rf_interest)*(days_to_maturity))*norm.cdf(d2))
    return np.float64(call_price)


