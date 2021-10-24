# yf_dynamictable
Project to create dynamic tables of stocks attributes using pandas and yfinance

first you are going to need to install the necessary libraries.
write on your terminal:
pip install yfinance
pip install pandas
pip install openpyxl xlsxwriter xlrd

Then, all you have to use to create dynamic table and compare stocks attributes is to edit the three first variables,
ticker_list, to add all to stock tickers you want to analyse
Attributes, to add all the stock attributes you want to compare
And the sort factor that will be aplied to the first attribute that you wrote in the Attributes list
And finally a excel sheet will be saved in the same folder or the previous one as your code.
