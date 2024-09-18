import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

"""

The code below runs a linear regression using the Big Ten Softball data by team. 

"""

# This code sets up the dataframe from the csv file I created using the scraped data

big_ten = pd.read_csv('../SI_311/homework/hw2/big10_data.csv')
big_ten['1B'] = big_ten['H'] - (big_ten['2B'] - big_ten['3B'] - big_ten['HR'])

# create dataframe where x the independent variables and y the dependent one
independent_variables = ['1B','2B', 'BB', 'SB']
x = big_ten[independent_variables]
y = big_ten['R']

x = sm.add_constant(x)
model = sm.OLS(y, x).fit()

"""

Creating the predicted runs scored equation from the regression results

"""

model_coefficients = model.params

def predicted_rs(data, coefficients):
    singles = (data['H'] - (data['2B']+ data['3B']+ data['HR']))
    rs = coefficients['const']+coefficients['1B']*singles+coefficients['2B']*data['2B']+coefficients['BB']*data['BB']+coefficients['SB']*data['SB']
    return rs

""""

The code below predicts the runs scored for two players on the Michigan Softball Team
using the multiple linear regression created using the Big Ten softball data.

Note I did not use CS in my model because I didn't have that statistic.

"""

# creating the dataframe and getting all necessary coefficients
michigan_softball = pd.read_csv('../SI_311/homework/hw2/michigan_softball_2024_data.csv')
michigan_softball.set_index('Name', inplace=True)
michigan_softball['1B'] = michigan_softball['H'] - (michigan_softball['2B'] - michigan_softball['3B'] - michigan_softball['HR'])
michigan_softball['SB'] = [int(michigan_softball.loc[idx]['SB-ATT'].split('-')[0]) for idx in michigan_softball.index]

# predicting runs scored using coefficients from linear regression for every player
michigan_softball['predicted rs'] = [predicted_rs(michigan_softball.loc[idx], model_coefficients) for idx in michigan_softball.index]
print('\n')
print(michigan_softball)

# predicted runs scored for two players of my analysis
print('\n')
print(f'Maddie Erickson is predicted to score {michigan_softball.loc['Maddie Erickson']['predicted rs']} runs using the linear weights approach.')
print(f'Keke Tholl is predicted to score {michigan_softball.loc['Keke Tholl']['predicted rs']} runs using the linear weights approach.')

