'''
Zhang Zhang
2017-03-15

Recession checker: See if there is a recession based on lagging indicators provided by 
CFNAI index of 85 indicators: https://www.chicagofed.org/~/media/publications/cfnai/cfnai-data-series-xlsx.xlsx?la=en

An 'Official' period of recession is defined by the 3 month moving average being less than 0.7. 
'''

import pandas as pd
import io
#import requests

data_url = 'https://www.chicagofed.org/~/media/publications/cfnai/cfnai-data-series-xlsx.xlsx?la=en'
output_directory = '/var/www/html/results'

def load_data(url):
	#s=requests.get(url).content
	df=pd.read_excel(url, sheetname='data')
	print(df)
	return df


def is_recession_ma3(data):
	return data <= -0.7

def check_recession_ma3():
	df = load_data(data_url)
	latest_row = df[-1:]
	latest_MA3 = latest_row.iloc[0]['CFNAI_MA3']

	result = is_recession_ma3(latest_MA3)

	result_string = ""

	try:
		if result:
			result_string = "Uh oh, the United States appears to be in a recession!"
		else:
			result_string = "Nope! We are not in a recession."

	except:
		result_string = "We don't know! Something must have gone wrong with the crystal ball."
	
	with open(output_directory + '/CFNAI_MA3.txt', 'w') as f:
		f.write(result_string)
		print("Wrote results to " + output_directory)
	
	print(result_string)
	return result

#check_recession_ma3()
