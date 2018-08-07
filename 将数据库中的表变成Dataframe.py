from sqlalchemy import  create_engine
import  pandas as pd

engine = create_engine('oracle://gmonkey:gmonkey@127.0.0.1:1521/xe')
def getData(tablename):
    res = pd.read_sql(tablename, engine)
    return res

if __name__ == '__main__':
    df = getData('st_jrj_zh')
    for i in range(len(df)):
        print(df.iat[i,5],df.iat[i,6],df.iat[i,7])
