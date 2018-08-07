from sqlalchemy import create_engine
import cx_Oracle
engine = create_engine('oracle://lb/lb@192.168.10.03/test.sh.tz')#用sqlalchemy创建引擎
connection = cx_Oracle.Connection("lb/lb@192.168.10.03/test.sh.tz")
DBLINE='lb/lb@192.168.10.03/test.sh.tz'