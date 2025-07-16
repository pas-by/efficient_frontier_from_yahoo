#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name   : yfin_test001.py
#    description : 列出某股票的歷史數據。
#          begin :  2021-09-21
#  last modified :  2025-07-16

"""
安裝 Yahoo finance Python module
pip install yfinance #Yahoo Finance python API
"""

import yfinance as yf
import math
import numpy as np
import pandas as pd
import scipy.optimize as sco
#  import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


def efficientFrontier(log_returns):
    print("monthly return")
    print(log_returns)

    # annual return
    year_ret = log_returns.sum()

    # however, the example use monthly mean return
    mon_mean_ret = log_returns.mean()

    #  pd.set_option("display.max_rows", None, "display.max_columns", None)
    pd.set_option("display.max_rows", None)

    print("\nmean monthly return :")
    print(mon_mean_ret)
    max_ret = np.amax(mon_mean_ret)
    print("\nmax. = %6.4f" % (max_ret))
    min_ret = np.amin(mon_mean_ret)
    print("min. = %6.4f" % (min_ret))

    # covariance matrix
    cov_mar = log_returns.cov()

    print("\ncovariance matrix :")
    print(cov_mar.copy(deep=True).round(4))
    # print(cov_mar)

    number_of_assets = log_returns.shape[1]
    # print(number_of_assets)

    def portfolio_risk(weights):
        weights = np.array(weights)
        pvol = np.sqrt(np.dot(weights.T, np.dot(cov_mar, weights)))

        # return stand deviation
        return pvol

    def portfolio_return(weights):
        weights = np.array(weights)
        pret = np.dot(weights, mon_mean_ret)
        return pret

    bnds = tuple((0, 1) for x in range(number_of_assets))

    # target returns to be solved
    target_return = np.linspace(min_ret, max_ret, 20)

    #  target risk to be solved
    tvols = []

    # 碼農的測試碼
    # print(min_ret);
    # print(max_ret);
    # print(target_return);

    # compute & print results
    print("\nresults")
    for tret in target_return:
        cons = (
            {"type": "eq", "fun": lambda x: portfolio_return(x) - tret},
            {"type": "eq", "fun": lambda x: np.sum(x) - 1},
        )
        res = sco.minimize(
            portfolio_risk,
            number_of_assets
            * [
                1.0 / number_of_assets,
            ],
            method="SLSQP",
            bounds=bnds,
            constraints=cons,
        )
        tvols.append(res['fun'])
        print("%6.4f" % tret, end=", ")

        # print(res['x'], end=' ');
        # print(res['x'].sum());

        print("%6.4f" % res["fun"], end=", ")

        for index in range(len(res["x"])):
            if index % 5 < 1:
                # print();
                pass

            print("%6.4f" % res["x"][index], end=", ")

        print()

    tvols = np.array(tvols)

    #  max. Sharpe ratio
    #
    def statistics(weights):
        weights = np.array(weights)
        pret = np.sum(log_returns.mean() * weights)
        pvols = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov(), weights)))
        return np.array([pret, pvols, pret/pvols])

    def min_sharpe(weights):
        return -statistics(weights)[2]

    cons = ({'type': 'eq', 'fun': lambda x: np.sum(x)-1})
    bnds = tuple((0, 1) for x in range(number_of_assets))
    opts = sco.minimize(min_sharpe, number_of_assets * [1/number_of_assets], method='SLSQP', bounds=bnds, constraints=cons)
    # opts['x'].round(3)

    #  碼農的測試碼
    #  print(opts['x'].round(3))
    #  print(statistics(opts['x'].round(3)))

    #  weight in max. sharpe ratio
    print();
    print("weight values in max. sharpe ratio");
    maxSharpe = opts['x'].round(3);
    for a in range(len(maxSharpe)):
        #  print(maxSharpe[a], end=", ");
        print(a+1, "\t", end="");
        if maxSharpe[a] >= 0.001 :
            print(maxSharpe[a]);
        else :
            print("0");

    print()
    print(statistics(opts['x'].round(3)))


    plt.figure(figsize=(10, 6))
    plt.scatter(tvols, target_return, c=target_return/tvols, marker='x', s=100)
    plt.plot(statistics(opts['x'])[1], statistics(opts['x'])[0], '*', markersize=15, label='max. Sharpe ratio')
    plt.grid(True)
    plt.xlabel('risk')
    plt.ylabel('monthly return')
    #  plt.colorbar(label='Sharpe ratio')
    plt.legend()
    plt.show()


def closePriceOfLastYear(stock_code):
    a = yf.Ticker(stock_code)
    history = a.history(period="1y", interval="1mo")

    # 碼農的測試碼
    print(history)

    rows_2be_del = []

    for index in range(history.index.size):
        close_price = history.iloc[index, 3]
        if math.isnan(close_price):
            # 將股息加進下月的股價
            history.iloc[index + 1, 3] += history.iloc[index, 5]
            rows_2be_del.append(index)
        else:
            # 碼農的測試碼
            # print(close_price);
            pass

    # remove the 'dividend events'
    adjusted_prices = history.drop(history.index[rows_2be_del], axis=0)
    adjusted_prices = adjusted_prices["Close"]

    #  程罪員的測試碼
    #  print(adjusted_prices)

    return adjusted_prices;

def returnOfLastYear(stock_code):

    # assign the numpy log function to a new function called ln
    ln = np.log

    a = yf.Ticker(stock_code)
    history = a.history(period="1y", interval="1mo")

    # 碼農的測試碼
    print(history)

    rows_2be_del = [];
    totalDividends = 0.0;

    for index in range(history.index.size):
        close_price = history.iloc[index, 3]
        totalDividends += history.iloc[index, 5];

        if math.isnan(close_price):
            #  將股息加進下月的股價
            #  history.iloc[index + 1, 3] += history.iloc[index, 5]
            rows_2be_del.append(index)
        else:
            # 碼農的測試碼
            # print(close_price);
            pass

    # add the total dividend to the last month
    history.iloc[history.index.size - 1, 3] += totalDividends;

    # remove the 'dividend events'
    adjusted_prices = history.drop(history.index[rows_2be_del], axis=0)
    adjusted_prices = adjusted_prices["Close"]

    # 程罪員的測試碼
    print(adjusted_prices)

    t0 = ln(adjusted_prices)
    t1 = ln(adjusted_prices)

    # remove the 1'st row
    t1 = t1.drop(t1.index[0], axis=0)

    # remove the last row
    t0 = t0.drop(t0.index[t0.index.size - 1], axis=0)

    # to compute the 'Log Return'
    logReturn = t1.to_numpy() - t0.to_numpy()

    # convert a NumPy array to a Pandas series
    logReturn = pd.Series(logReturn)
    logReturn = logReturn.rename(stock_code)

    #  remove the last row
    #  logReturn = logReturn.drop(logReturn.index[logReturn.index.size - 1], axis=0)

    return logReturn

if __name__ == "__main__":
    #  程罪員的測試碼
    print(pd.concat([pd.DataFrame(), returnOfLastYear('AZO'), returnOfLastYear('AAPL')], axis=1));
