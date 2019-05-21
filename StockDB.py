import twstock
import time
import os
import json

###################################################################
## Class StockDB:
## Function: GetOneStock => Use to Gen Stock/ETF list file
##      Input:  NA  
##      Output: Default is StockCode.txt
#####################
## Class Key Variables:
## Ex: AllStockData['2330']['price']
##     AllStockData['2330']['high']
## 
###################################################################

class StockDB():
    def Reset(self):
        self.AllStockData = {}
        
    def __init__(self):
        self.Reset()

    def SetCodeLst(self,CodeLstFile):
        self.CodeLstFile = CodeLstFile

    def GetAllStockCode(self,outfile='StockCode.txt'):
        f = open(outfile,'w')
        for aCode in twstock.codes.keys():
            if twstock.codes[aCode].type == '股票' or twstock.codes[aCode].type == 'ETF':
                f.write('%s\n' % aCode)
        f.close()    

    def GetOneStock(self,StockCode):
        stock    = twstock.Stock(StockCode)
        high     = stock.high
        low      = stock.low
        price    = stock.price
        capacity = stock.capacity
        avg5_Price= stock.moving_average(stock.price,5)
        avg10_Price= stock.moving_average(stock.price,10)
        avg5_Cap= stock.moving_average(stock.capacity,5)
        avg10_Cap= stock.moving_average(stock.capacity,10)

        self.AllStockData[StockCode] = {
            'high' : high,
            'low'  : low,
            'price':price,
            'capacity': capacity,
            'avg5_Price' :  avg5_Price,
            'avg10_Price':  avg10_Price,
            'avg5_Cap' :    avg5_Cap, 
            'avg10_Cap' :   avg10_Cap
        }
        time.sleep(5)
   
    def GetAllStockFromWeb(self):
        with open(self.CodeLstFile) as Code_f:
            CodesLst = Code_f.read().strip().split()
        Cnt = 0
        for aCode in CodesLst:
            try:
                aStDB.GetOneStock(aCode)
            except:
                print('%s is Error' % aCode)
            Cnt = Cnt + 1
            print('%s: %s ... Processing ...' % (Cnt,aCode) )
            if Cnt % 50 == 0 : aStDB.SaveDB()

        aStDB.SaveDB()
     

    def SaveDB(self,jsonfile='StockData.json'):
        with open(jsonfile,'w') as outf:
            json.dump(self.AllStockData,outf)

    def GetAllStockFromFile(self,jsonfile='StockData.json'):
        with open(jsonfile,'r') as inf:
            self.AllStockData = json.load(inf)


def main():
    print('This is StockDB class, no test-function now')

if __name__ == '__main__':main()
