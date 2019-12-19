import MySQLdb
import io

class SQLEngine():
    def __init__(self, ctx):
        self.user = ctx.user_sql
        self.password = ctx.password_sql
        self.database = ctx.database_sql
        self.host = ctx.host_sql
        self.port = ctx.port_sql

        self.con, self.cursor = self._conect()
    
    def _conect(self):
        con = MySQLdb.connect(user = self.user,
                              password = self.password,
                              host = self.host,
                              port = self.port,
                              database = self.database)

        cursor = con.cursor()

        return con, cursor

    def execute(self, entity):
        return True
