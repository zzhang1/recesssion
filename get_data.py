import pandas as pd
import io
import numpy as np
import os.path
from os import path
import time
import pandas_datareader.data as web
import datetime
#import requests

data_output_directory = '/tmp'

def get_combined_cfnai_recession_df_old():
    CFNAI_data_url = 'https://www.chicagofed.org/~/media/publications/cfnai/cfnai-data-series-xlsx.xlsx?la=en'
    NBER_data_url = 'https://www.nber.org/cycles/bcdc1.xlsx'

    'If the data is recently cached, then just return the file'
    if path.exists(data_output_directory + '/data.xlsx'):
        ten_hours = 60*60*10
        if path.getmtime(data_output_directory + '/data.xlsx') + ten_hours > time.time():
            return pd.read_excel(data_output_directory + '/data.xlsx')


    df=pd.read_excel(CFNAI_data_url, sheet_name='data')
    df['Date'] = pd.to_datetime(df['Date'])

    recession_df = pd.read_excel(NBER_data_url, sheet_name='NBER Chronology', header=2)
    recession_df = recession_df.iloc[:-7,2:]
    recession_df['recession_start'] = pd.to_datetime(recession_df['Peak month'], format='%B %Y')
    recession_df['recession_end'] = pd.to_datetime(recession_df['Trough month'], format='%B %Y') + pd.tseries.offsets.MonthEnd(1)

    # https://stackoverflow.com/questions/41020978/pandas-select-df-rows-based-on-another-df
    # Perform the searchsorted and get the corresponding df2 values for both endpoints of df1.
    s1 = recession_df.reindex(np.searchsorted(recession_df['recession_start'], df['Date'], side='right')-1)
    s2 = recession_df.reindex(np.searchsorted(recession_df['recession_end'], df['Date'], side='right')-1)

    # Build the conditions that indicate an overlap (any True condition indicates an overlap).
    cond = [
        df['Date'].values <= s1['recession_end'].values,
        df['Date'].values <= s2['recession_end'].values,
        s1.index.values != s2.index.values
        ]

    # Filter df1 to only the overlapping intervals, and set those to 1 to indicate recession
    df['USREC'] = 0
    df.loc[np.any(cond, axis=0), 'USREC'] = 1

    # Cache data so subsequent calls in a short time window don't re-fetch the data
    df.to_excel(data_output_directory + '/data.xlsx')

    return df


def get_combined_cfnai_recession_df():
    'If the data is recently cached, then just return the file'
    if path.exists(data_output_directory + '/data.xlsx'):
        ten_hours = 60*60*10
        if path.getmtime(data_output_directory + '/data.xlsx') + ten_hours > time.time():
            return pd.read_excel(data_output_directory + '/data.xlsx').set_index('DATE').ffill().dropna()

    start_dt = datetime.datetime(1967, 1, 1)
    end_dt = datetime.date.today()
    df = web.DataReader(['USREC','CFNAI','CFNAIMA3','CFNAIDIFF','CANDH','EUANDH','PANDI','SOANDI'], 'fred', start_dt)
    df = df.reset_index()
    df['DATE'] = df['DATE'] + pd.tseries.offsets.MonthEnd(1)
    df.set_index('DATE')

    df.to_excel(data_output_directory + '/data.xlsx')
    return df.ffill().dropna()


def get_monthly_fred_data(id_list):
    'If the data is recently cached, then just return the file'
    if path.exists(output_directory + '/data2.xlsx'):
        ten_hours = 60*60*10
        if path.getmtime(data_output_directory + '/data2.xlsx') + ten_hours > time.time():
            return pd.read_excel(data_output_directory + '/data2.xlsx').set_index('DATE').drop('Unnamed: 0',axis=1).ffill().dropna()

    start_dt = datetime.datetime(1967, 1, 1)
    end_dt = datetime.date.today()
    df = web.DataReader(id_list, 'fred', start_dt)
    df = df.reset_index()
    df['DATE'] = df['DATE'] + pd.tseries.offsets.MonthEnd(1)
    df.set_index('DATE')

    df.to_excel(data_output_directory + '/data2.xlsx')
    return df.ffill().dropna()
