# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 13:57:32 2016

@author: four
"""
import pandas as pd


# 获取地址数据
def get_adress_data(adress=0):
    data = pd.read_csv(adress, parse_dates=False, header=None,names=['dateL', 'openL', 'highL', 'lowL', 'closeL', 'volL'])
    data.drop(0, axis=0, inplace=True)
    data['dateL'] = pd.to_datetime(data.dateL)
    return data


# 获取macd
def get_macd_data(data, short=0, long1=0, mid=0):
    if short == 0:
        short = 12
    if long1 == 0:
        long1 = 26
    if mid == 0:
        mid = 9
    data['sema'] = pd.ewma(data['closeL'], span=short)
    data['lema'] = pd.ewma(data['closeL'], span=long1)
    data.fillna(0, inplace=True)
    data['data_dif'] = data['sema'] - data['lema']
    data['data_dea'] = pd.ewma(data['data_dif'], span=mid)
    data['data_macd'] = 2 * (data['data_dif'] - data['data_dea'])
    data.fillna(0, inplace=True)
    return data[['data_dif', 'data_dea', 'data_macd']]


def get_kdj_data(data, N=0, M=0):
    if N == 0:
        N = 9
    if M == 0:
        M = 2
    low_list = pd.rolling_min(data['lowL'], N)
    low_list.fillna(value=pd.expanding_min(data['lowL']), inplace=True)
    high_list = pd.rolling_max(data['highL'], N)
    high_list.fillna(value=pd.expanding_max(data['highL']), inplace=True)
    rsv = (data['closeL'] - low_list) / (high_list - low_list) * 100
    data['KDJ_K'] = pd.ewma(rsv, com=M)
    data['KDJ_D'] = pd.ewma(data['KDJ_K'], com=M)
    data['KDJ_J'] = 3 * data['KDJ_K'] - 2 * data['KDJ_D']
    data.fillna(0, inplace=True)
    return data[['KDJ_K', 'KDJ_D', 'KDJ_J']]


def get_ma_data(data, N=0):
    if N == 0:
        N = 5
    data['ma'] = pd.rolling_mean(data['closeL'], N)
    data.fillna(0, inplace=True)
    return data[['ma']]


def get_cci_data(data, N=0):
    if N == 0:
        N = 14
    data['tp'] = (data['highL'] + data['lowL'] + data['closeL']) / 3
    data['mac'] = pd.rolling_mean(data['tp'], N)
    data['md'] = 0
    for i in range(len(data) - 14):
        data['md'][i + 13] = data['closeL'][i:i + 13].mad()
    cci = (data['tp'] - data['mac']) / (data['md'] * 0.015)
    cci = pd.DataFrame(cci, columns=['cci'])
    return cci

def get_rsi_data(data, N=0):
    if N == 0:
        N = 24
    data['value'] = data['closeL'] - data['closeL'].shift(1)
    data.fillna(0, inplace=True)
    data['value1'] = data['value']
    data['value1'][data['value1'] < 0] = 0
    data['value2'] = data['value']
    data['value2'][data['value2'] > 0] = 0
    data['plus'] = pd.rolling_sum(data['value1'], N)
    data['minus'] = pd.rolling_sum(data['value2'], N)
    data.fillna(0, inplace=True)
    rsi = data['plus'] / (data['plus'] - data['minus']) * 100
    data.fillna(0, inplace=True)
    rsi = pd.DataFrame(rsi, columns=['rsi'])
    return rsi

# 读取数据
data = get_adress_data(adress='D:/Data/600021.csv')
# a = get_macd_data(data)
# b = get_kdj_data(data)
# c = get_ma_data(data)
d = get_rsi_data(data)
# e = get_cci_data(data)





