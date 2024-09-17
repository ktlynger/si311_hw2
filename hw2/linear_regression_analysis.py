import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

"""

The code below runs a linear regression using the Big Ten Softball data by team. 

"""

# SETUP - getting df and independent and dependent variables

big_ten = pd.read_csv('../SI 311/homework/hw2/big10_data.csv')
big_ten['1B'] = big_ten['H'] - (big_ten['2B'] - big_ten['3B'] - big_ten['HR'])

# dependent variable = runs scored
Y = big_ten['R']

# independent variable = 1B, 2B, 3B, HR, BB, HBP, SB
independent_variables = ['1B','2B', '3B', 'HR', 'BB', 'HBP', 'SB']
X = big_ten[independent_variables]

# running the regression
model = linear_model.LinearRegression().fit(X, Y)
coefficients = model.coef_
intercept = model.intercept_
predictions = model.predict(X)
mse = mean_squared_error(Y, predictions)
r2 = r2_score(Y, predictions)


# Model Results
# print("Coefficients:", coefficients)
# print("Intercept:", intercept)
# print(f"Mean Squared Error (MSE): {mse}")
# print(f"R² Score: {r2}")

""" 

    Creating the predicted runs scored equation from the regression results

"""

coefficients_dict = dict(zip(independent_variables, coefficients))
coefficients_dict['constant'] = intercept

def predicted_rs(data, dict):
    singles = (data['H'] - (data['2B']+ data['3B']+ data['HR']))
    rs = dict['constant'] + dict['1B']*singles + dict['2B']*data['2B'] + dict['3B']*data['3B'] + dict['HR']*data['HR'] + dict['BB']*data['BB'] + dict['HBP']*data['HBP']
    return rs


""""

    The code below predicts the runs scored for two players on the Michigan Softball Team
    using the multiple linear regression created using the Big Ten softball data.

    Note I did not use CS in my model because I didn't have that statistic.

"""

# creating the dataframe and getting all necessary coefficients
michigan_softball = pd.read_csv('../SI 311/homework/hw2/michigan_softball_2024_data.csv')
michigan_softball.set_index('Name', inplace=True)
michigan_softball['1B'] = michigan_softball['H'] - (michigan_softball['2B'] - michigan_softball['3B'] - michigan_softball['HR'])

# predicting runs scored using coefficients from linear regression for every player
michigan_softball['predicted rs'] = [predicted_rs(michigan_softball.loc[idx], coefficients_dict) for idx in michigan_softball.index]

# predicted runs scored for two players of my analysis
print(f'Maddie Erickson is predicted to score {michigan_softball.loc['Maddie Erickson']['predicted rs']} runs using the linear weights approach.')
print(f'Keke Tholl is predicted to score {michigan_softball.loc['Keke Tholl']['predicted rs']} runs using the linear weights approach.')

