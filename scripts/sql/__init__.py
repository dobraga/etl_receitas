import psycopg2
import io

class SQLEngine():
    def __init__(self, ctx):
        self.user = ctx.user_sql
        self.password = ctx.password_sql
        self.database = ctx.database_sql
        self.dbname = ctx.dbname_sql
        self.host = ctx.host_sql
        self.port = ctx.port_sql

        self.con, self.cursor = self._conect()
    
    def _conect(self):
        con = psycopg2.connect(user = self.user,
                               password = self.password,
                               host = self.host,
                               port = self.port,
                               database = self.database)

        cursor = con.cursor()

        return con, cursor

    def execute(self, entity):
        return True



# con = psycopg2.connect(user = 'python', password = 'python', host = 'localhost', port = '5432', database = 'postgres')
# cursor = conn.cursor()
# for line in io.open('E:/GoogleDrive/projects/receitas/saida/tastemade.jsonl','r',encoding='utf8'):
#     print(line)
#     cursor.execute('insert into receitas.tbl_tastemade_stg values {};'.format(line))

# cursor.execute("insert into receitas.tbl_tastemade_stg values ('{ 'customer': 'John Doe', 'items': {'product': 'Beer','qty': 6}');")

