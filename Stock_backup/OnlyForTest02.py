import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('oracle://gmonkey:gmonkey@127.0.0.1:1521/xe')

df = pd.DataFrame(pd.read_excel('jbm.xlsx',sheet_name='basic2017'))
df.to_sql('jdm_test', engine, if_exists='append', index=None)

