import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from scipy import stats

'''Overarching Code to prep the data in order for analysis'''

#Read in stats file and salary file to python pandas data frames, adjust stats dataframe to include only relevants stats.
stats_file = pd.read_csv('NBA_Stats_2018-19.csv', encoding = 'latin1')
sal_file = pd.read_csv('NBA_Salaries_2018-19.csv', encoding = 'latin1')

#Compare the stats file with the salaries file and drop names that are not listed in both.
#clean_stats is the stats, which will be explanatory variables. clean_sal is salaries, which is the dependent variable.
dirty_sal_list = sal_file['Name'].to_list()
dirty_stats_list = stats_file['Name'].to_list()
clean_stats = stats_file[stats_file.Name.isin(dirty_sal_list)]
clean_sal = sal_file[sal_file.Name.isin(dirty_stats_list)]
stats_only = clean_stats[['PPG','RPG','APG','SPG']]
sal_only = clean_sal[['Salary']]
X = stats_only.values.tolist()
y = sal_only.values.tolist()
points_rebounds = clean_stats[['PPG','RPG']]
points_rebounds = points_rebounds.values.tolist()
points_rebounds_assists = clean_stats[['PPG','RPG','APG']]
points_rebounds_assists = points_rebounds_assists.values.tolist()

#Isolate each stat list in preparation for scatter plot visualization and linear regression
points_reg = []
for sublist in X:
    points_reg.append([sublist[0]])
rebounds_reg = []
for sublist in X:
    rebounds_reg.append([sublist[1]])
assists_reg = []
for sublist in X:
    assists_reg.append([sublist[2]])
steals_reg = []
for sublist in X:
    steals_reg.append([sublist[3]])

points = []
for sublist in X:
    points.append(sublist[0])
rebounds = []
for sublist in X:
    rebounds.append(sublist[1])
assists = []
for sublist in X:
    assists.append(sublist[2])
steals = []
for sublist in X:
    steals.append(sublist[3])

#credit for the logic of this loop, making a single list out of a list of lists: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
flat_list = []
for sublist in y:
    for item in sublist:
        flat_list.append(item)
#end credit

#Turn the lists of only salaries into a lists of strings with only numbers,
#so it can get converted to an int properly.
num_only = [s.replace("$", "") for s in flat_list]
num_only = [s.replace(",", "") for s in num_only]
y = [int(s.replace(" ", "")) for s in num_only]

#Turn the datasets into arrays so that I can compare stats of a player to that player's salary.
X, y, points, rebounds, assists, steals, points_rebounds, points_rebounds_assists = np.array(X), np.array(y), np.array(points), np.array(rebounds), np.array(assists), np.array(steals), np.array(points_rebounds), np.array(points_rebounds_assists)

def individual_linear_regression_visualization():
    '''This function takes no arguments, creates linear regression visualizations
    and prints the measure of goodness of fit (R value) and standard error'''

    #regression on points
    slope, intercept, r, p, std_err = stats.linregress(points, y)

    def myfunc(points):
      return slope * points + intercept

    mymodel = list(map(myfunc, points))

    plt.scatter(points, y)
    plt.plot(points, mymodel)
    plt.show()

    print("R-squared is", r, "and standard error is", std_err)

    #regression on rebounds
    slope, intercept, r, p, std_err = stats.linregress(rebounds, y)

    def myfunc(rebounds):
      return slope * rebounds + intercept

    mymodel = list(map(myfunc, rebounds))

    plt.scatter(rebounds, y)
    plt.plot(rebounds, mymodel)
    plt.show()

    print("R-squared is", r, "and standard error is", std_err)

    #regression on assists
    slope, intercept, r, p, std_err = stats.linregress(assists, y)

    def myfunc(assists):
      return slope * assists + intercept

    mymodel = list(map(myfunc, assists))

    plt.scatter(assists, y)
    plt.plot(assists, mymodel)
    plt.show()

    print("R-squared is", r, "and standard error is", std_err)

    #regression on steals
    slope, intercept, r, p, std_err = stats.linregress(steals, y)

    def myfunc(steals):
      return slope * steals + intercept

    mymodel = list(map(myfunc, steals))

    plt.scatter(steals, y)
    plt.plot(steals, mymodel)
    plt.show()

    print("R-squared is", r, "and standard error is", std_err)
    print()

def one_stat_predictions():
    '''This function trains and executes a linear regression on each stat and prints out
    the expected salary with only the identified stat.'''

    #Train and test my linear regression for each stat individually
    points_train, points_test, y_train, y_test = train_test_split(points_reg, y, test_size = 0.2, random_state=9)
    points_regression = linear_model.LinearRegression()
    points_regression.fit(points_train, y_train)
    points_prediction = points_regression.predict(points_test)
    points_rmse = (np.sqrt(mean_squared_error(y_test, points_prediction)))
    #Steph Curry Actual Salary: 38,320,489
    Steph = points_regression.predict([[27.3]])
    print("Steph Curry predicted salary given points only:", Steph)

    rebounds_train, rebounds_test, y_train, y_test = train_test_split(rebounds_reg, y, test_size = 0.2, random_state=9)
    rebounds_regression = linear_model.LinearRegression()
    rebounds_regression.fit(rebounds_train, y_train)
    rebounds_prediction = rebounds_regression.predict(rebounds_test)
    rebounds_rmse = (np.sqrt(mean_squared_error(y_test, rebounds_prediction)))
    #Steph Curry Actual Salary: 38,320,489
    Steph = rebounds_regression.predict([[5.3]])
    print("Steph Curry predicted salary given rebounds only:", Steph)

    assists_train, assists_test, y_train, y_test = train_test_split(assists_reg, y, test_size = 0.2, random_state=9)
    assists_regression = linear_model.LinearRegression()
    assists_regression.fit(assists_train, y_train)
    assists_prediction = assists_regression.predict(assists_test)
    assists_rmse = (np.sqrt(mean_squared_error(y_test, assists_prediction)))
    #Steph Curry Actual Salary: 38,320,489
    Steph = assists_regression.predict([[5.2]])
    print("Steph Curry predicted salary given assists only:", Steph)

    steals_train, steals_test, y_train, y_test = train_test_split(steals_reg, y, test_size = 0.2, random_state=9)
    steals_regression = linear_model.LinearRegression()
    steals_regression.fit(steals_train, y_train)
    steals_prediction = steals_regression.predict(steals_test)
    steals_rmse = (np.sqrt(mean_squared_error(y_test, steals_prediction)))
    #Steph Curry Actual Salary: 38,320,489
    Steph = steals_regression.predict([[1.33]])
    print("Steph Curry predicted salary given steals only:", Steph)
    print()

def best_model():
    '''This function runs a linear regression on points only, points and rebounds,
    points, rebounds and assists, and finally all four stats measure to determine
    which is closes to the correct answer'''

    points_train, points_test, y_train, y_test = train_test_split(points_reg, y, test_size = 0.2, random_state=9)
    points_regression = linear_model.LinearRegression()
    points_regression.fit(points_train, y_train)
    points_prediction = points_regression.predict(points_test)
    #Steph Curry Actual Salary: 38,320,489
    Steph = points_regression.predict([[27.3]])
    print("Steph Curry predicted salary given points only:", Steph)

    points_rebounds_train, points_rebounds_test, y_train, y_test = train_test_split(points_rebounds, y, test_size = 0.2, random_state=9)
    regr = linear_model.LinearRegression()
    regr.fit(points_rebounds_train, y_train)
    pred = regr.predict(points_rebounds_test)
    #Steph Curry Actual Salary: 38,320,489
    Steph = regr.predict([[27.3, 5.3]])
    print("Steph Curry predicted salary given points and rebounds only:", Steph)

    points_rebounds_assists_train, points_rebounds_assists_test, y_train, y_test = train_test_split(points_rebounds_assists, y, test_size = 0.2, random_state=9)
    regr = linear_model.LinearRegression()
    regr.fit(points_rebounds_assists_train, y_train)
    pred = regr.predict(points_rebounds_assists_test)
    #Steph Curry Actual Salary: 38,320,489
    Steph = regr.predict([[27.3, 5.3, 5.2]])
    print("Steph Curry predicted salary given points, rebounds, and assists only:", Steph)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=9)
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    pred = regr.predict(X_test)
    X_rmse = (np.sqrt(mean_squared_error(y_test, pred)))
    #Steph Curry Actual Salary: 38,320,489
    Steph = regr.predict([[27.3, 5.3, 5.2, 1.33]])
    print("Steph Curry predicted salary given points, rebounds, assists, and steals:", Steph)
    print("The rmse for Steph Curry's predicted salary is", X_rmse)
    print()

def salary_predictor():
    '''This function takes no arguments and prints predicted values for selected players
    and then asks for input to predict a salary based on stats'''

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=9)
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    pred = regr.predict(X_test)

    #Steph Curry Actual: 38,320,489
    Steph = regr.predict([[27.3, 5.3, 5.2, 1.33]])
    print("Steph Curry predicted salary:", Steph)
    print("Steph Curry actual salary: 38,320,489")
    print()
    #Alex Abrines Actual: 3,752,179
    Alex_Abrines = regr.predict([[5.3, 1.5, .6, .55]])
    print("Alex Abrines predicted salary:", Alex_Abrines) 
    print("Alex Abrines actual salary: 3,752,179")
    print()
    #Quincy Acy Actual: 218,879
    Quincy_Acy = regr.predict([[1.7, 2.5, .8, .1]])
    print("Quincy Acy predicted salary:", Quincy_Acy)
    print("Quincy Acy actual salary: 218,879")
    print()
    #Carmelo Anthony Actual: 2,449,062
    Carmelo_Anthony = regr.predict([[13.4, 5.4, .5, .4]])
    print("Carmelo Anthony predicted salary:", Carmelo_Anthony)
    print("Carmelo Anthony actual salary: 2,449,062")
    print()
    #Kevin Durant Actual: 30,691,458
    Kevin_Durant = regr.predict([[26, 6.4, 5.9, .76]])
    print("Kevin Durant predicted salary:", Kevin_Durant)
    print("Kevin Durant actual salary: 30,691,458")
    print()

    exit = input("Do you want to predict a player's salary? ")
    while exit != 'no':
        salary_prediction = []
        points = float(input("Enter average points per game: "))
        rebounds = float(input("Enter average rebounds per game: "))
        assists = float(input("Enter average assists per game: "))
        steals = float(input("Enter average steals per game: "))
        salary_prediction.append(points)
        salary_prediction.append(rebounds)
        salary_prediction.append(assists)
        salary_prediction.append(steals)
        salary_prediction = regr.predict([salary_prediction])
        print("Predicted salary given your inputs:", salary_prediction)
        test_set_rmse = (np.sqrt(mean_squared_error(y_test, pred)))
        print("Mean squared error:", test_set_rmse)
        exit = input("Do you want to predict another player's salary? ")

###############################################################################
###############################################################################

individual_linear_regression_visualization()
one_stat_predictions()
best_model()
salary_predictor()
