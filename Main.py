import os
import twstock
import StockDB, StockStrategy

def main():
    StockCodeLst = 'StockCode.txt'

    aStDB = StockDB.StockDB()
    aStDB.SetCodeLst(StockCodeLst)
    #aStDB.GetAllStockCode(StockCodeLst)   => Initial Stock Code list. Only use it when we need to update

    # Load data from Web, and save it to *.json
    aStDB.GetAllStockFromFile()
    #aStDB.GetAllStockFromWeb()

    # Load data from *.json
    #aStDB.GetAllStockFromFile()

    #########################################
    aStrategy = StockStrategy.StockStrategy()
    aStrategy.SetStockData(aStDB.AllStockData)
    aStrategy.wrk1()

if __name__ == '__main__':main()
