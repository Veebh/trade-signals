import talib
import pandas as pd

from utility import utility


class CDL3BLACKCROWS:
    def check(response,symbol,period):
        df = utility.getDataFrame(response["candles"])
        result = CDL3BLACKCROWS.CDL3BLACKCROWS(df)
        print(result)
    def CDL3BLACKCROWS(DataFrame):
        res = talib.CDL3BLACKCROWS(
            DataFrame.open.values, DataFrame.high.values, DataFrame.low.values, DataFrame.close.values)
        return pd.DataFrame({'CDL3BLACKCROWS': res}, index=DataFrame.index) 