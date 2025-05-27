import math

# helper formulas---------------------
# get variance
def get_variance(dataset: list[float]):
    length = len(dataset)
    if length<2:
        return None
    average_value = sum(dataset)/length
    s = 0
    for val in dataset:
        s += (val - average_value)**2
    variance = s/(length-1)
    return variance

# get standard deviation (volatility)
def get_sd(dataset: list[float]):
    variance = get_variance(dataset)
    return math.sqrt(variance)

# For Black-Scholes model----------------
from scipy.stats import norm
def calculte_call_price(curr_price: float, strike_price: float,
                        rf_interest: float, days_to_maturity: int,
                        variance: float):
    # final formula helpers
    sdt = math.sqrt(variance)*math.sqrt(days_to_maturity)
    d1 = ((math.log(curr_price/strike_price)) + (rf_interest + (variance/2))*days_to_maturity)/sdt
    d2 = d1 - sdt
    norm_d1 = norm.cdf(d1)
    norm_d2 = norm.cdf(d2)

    # call option price
    call_price = (curr_price*norm_d1) - (strike_price*math.exp((-rf_interest)*(days_to_maturity))*norm.cdf(d2))
    return call_price


