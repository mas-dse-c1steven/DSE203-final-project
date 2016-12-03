import datalog_parser
import pymysql.cursors

class MysqlWrapper(object):
  """Datalog Client for Mysql"""
  def __init__(self, host='dse203gtd.cvnmpos6almn.us-east-1.rds.amazonaws.com',
                             user='student',
                             password='LEbKqX3q',
                             db='gtd',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor):
    super(MysqlWrapper, self).__init__()
    self.connection = pymysql.connect(host=host, user=user, password=password,db=db,charset=charset,cursorclass=cursorclass)
    self.parser = datalog_parser.DatalogParser("asf")
    
  def execute(self, dl_query):
    sql_query = self.parser.parse(dl_query)
    
    try:
        with self.connection.cursor() as cursor:
            cursor.execute(sql_query)

            for row in cursor:
                print(row) #TODO build a pandas DF 
    finally:
        connection.close()
    

  
if __name__ == '__main__':
  wrapper = MysqlWrapper("arg")
  dl_query = "Q(id) :- gtd(id)"
  wrapper.execute(dl_query)