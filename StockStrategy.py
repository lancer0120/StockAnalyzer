import os

###################################################################
## Class StockStrategy:
## Function: There are different strategy, wrk1(), wrk2(), ....
##           Each wrk* should be individual
##      Input: Database from StockDB
##      Output: The stock code we find
#####################
## Class Key Variables: NA
##   
###################################################################

class StockStrategy():
    def Reset(self):
        self.AllStockData = {}
        
    def __init__(self):
        self.Reset()

    def SetStockData(self,AllStockData):
        self.AllStockData = AllStockData

    def wrk1(self):
    ## In this work, we find all stock Cap. > 10days average Cap.
        f = open('wrk1.rpt','w')
        f_err = open('err.log','w')
        for aCode in self.AllStockData.keys():
            aStockData = self.AllStockData[aCode]
            try:
                if aStockData['capacity'][-1] < 100000: continue
                for i in range(len(aStockData)-1,-1,-1):
                    if aStockData['capacity'][-1] > 3*aStockData['avg10_Cap'][-1]:
                        f.write('%s\n' % aCode)
                        break
            except:
                f_err.write('Error in Code %s' % aCode)
        f.close()
        f_err.close()

def main():
    print('This is StockStrategy class, no test-function now')

if __name__ == '__main__':main()
