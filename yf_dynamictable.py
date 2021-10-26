import pandas as pd
from pandas.core.frame import DataFrame
import yfinance as yf

# list to select all stocks you want, beware, you have to write as the yahoo finance ticker show
tickers_list = ["BNS.TO","UPL.NS","CPFE3.SA","TOTS3.SA","GAZP.ME","WFC","PFE","7203.T","NEX.PA","2222.SR","BASFY"]
# list to select all attributes you want be in your spreadsheet, the rows will be organized by the first attribute you assign in this list
Attributes = ["trailingPE","forwardPE","shortName","fiveYearAvgDividendYield","country","industry"]
# write between the next quotations marks the way the main filter will display: "Asceding"(Crescente) or "Descending"(Decrescente)
sort_factor = "Ascending"

sort_dict = {"Descending":False, "Ascending":True} # dict to assign a parameter of .sort_values
tickers_data= {} # empty dictionary
attri_data = {} # empty dictionary

# creating empty dataframe variables dynamically 
for at in Attributes:
    attri_data[at] = pd.DataFrame()

for ticker in tickers_list:
    ticker_object = yf.Ticker(ticker)

    #convert info() output from dictionary to dataframe
    temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
    temp.reset_index(inplace=True)
    temp.columns = ["Attribute", "Recent"]
    
    # add (ticker, dataframe) to main dictionary
    tickers_data[ticker] = temp

# creating a dataframe with all the informations of every stock selected
combined_data = pd.concat(tickers_data)

# polishing the complete dataframe
combined_data = combined_data.reset_index()
del combined_data["level_1"]
combined_data.columns = ["Ticker", "Attribute", "Recent"]

for df in range(len(Attributes)):
    # selecting from the complete dataframe the attributes from attributes list and creating a mini table for each attribute
    attri_data[Attributes[df]] = combined_data[combined_data["Attribute"]=="{}".format(Attributes[df])]
    # polishing the mini dataframes
    attri_data[Attributes[df]].rename(columns={"Recent":"{}".format(Attributes[df])}, inplace=True)
    attri_data[Attributes[df]] = attri_data[Attributes[df]].set_index("Ticker")

# merging all the mini tables in one
combined_minidata = pd.concat(attri_data, axis=1)

# polishing the final dataframe
combined_minidata.columns = combined_minidata.columns.droplevel(-1)
clean_df = combined_minidata.iloc[:, 1::2]
clean_df_org = clean_df.sort_values("{}".format(Attributes[0]),ascending=sort_dict[sort_factor])

# outputs to use: excel, print and paste
clean_df_org.to_excel('./tabeladinamica.xlsx')
print(clean_df_org)
clean_df_org.to_clipboard(sep=',')