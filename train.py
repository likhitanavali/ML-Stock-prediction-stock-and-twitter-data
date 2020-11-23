import sys
import parse
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def modif(company):
	df = pd.read_csv(company)
	dateStr = df['Date'].values
	D = np.zeros(dateStr.shape)
	#Convert all date strings to a numeric value
	for i, j in enumerate(dateStr):
		#Date strings are of the form year-month-day
		D[i] = datetime.strptime(j, '%Y-%m-%d').timestamp()
	#Add the newly parsed column to the dataframe
	df['Timestamp'] = D
	#Remove any unused columns (axis = 1 specifies fields are columns)
	#print(df)
	return df.drop('Date', axis = 1)

def PredictStock(company,percent):
	path='/home/harshita/ML/datasets/'
	filename_suffix='csv'
	company = os.path.join(path, company + "." + filename_suffix)
	D = modif(company)
	print(D)
	
def main(argv):
	one = parse.main(argv[1])
	two = parse.main(argv[2])
	three = parse.main('silicon laboratories')
	print(one)
	
	res1 = PredictStock( argv[1] , one)
	res2 = PredictStock( argv[2] , two)
	res3 = PredictStock( argv[3], three)
	if(res1 > res2 and res1>res3):
		print("Invest in NRCIB")
	elif(res2 > res1 and res2 > res3):
		print("Invest in NVCN")
	else:	
		print("Invest in Silicon Labratories")
	
if __name__ == "__main__":
    # calling main function
    main(sys.argv)
    
