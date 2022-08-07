NBA Project analyzing points, rebounds, assists, and steals per game and
relating them to salary by use of linear regressions.

You need both of the following CSVs downloaded to run the program properly:
  NBA_Stats_2018-19.csv
  NBA_Salaries_2018-19.csv

Run the program in a terminal:
  python3 NBA_Project.py

Use the "X" at the top right corner of the generated graph to move to the next graph

If you want to predict a salary with your input, type a number for each stat
(the program accepts floats)

When you are done predicting salaries, reply "no" to exit the program.

The R-squared value shows what percent of the variance in salary is predicted
by the variance in points, rebounds, assists, and steals respectively.
RMSE measures how good the model predicts salary.

The program is not very accurate. This is largely due to the dataset: I only
used one year, a specific sample, and only four stats. The output would become
more accurate if I used panel data as opposed to cross sectional, if I used more
players in the sample, and if I utilized more relevant stats in the analysis.
Due to the nature of the project (Programming focused, not econometrics focused)
I felt it was appropriate to only use the limited sample I had.

The program does not stop the salary predictor function from outputting a negative
number. If your input for steals is too high relative to your other inputs,
you could get a negative number as an output. This is a quirk of the linear 
regression and results from statistical errors (like omitted variable bias,
heteroskedasticity, etc) that are beyond the scope of the programming project.
