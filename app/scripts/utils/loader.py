from .sqlengine import SQLEngine

class Loader():
    def __init__(self, ctx, sqlengine):
        self.dir_saida = ctx.dir_saida
        self.sqlengine = sqlengine

    def execute(self, identity):
        try:
            self.sqlengine.cursor.execute('TRUNCATE TABLE {}.tbl_{}_stg;'.format(self.sqlengine.dbname, identity))

            sql = "COPY {}.tbl_{}_stg FROM STDIN DELIMITER ';' CSV HEADER".format(self.sqlengine.dbname, identity)
            with open('{}/{}.csv'.format(self.dir_saida, identity), 'r') as f:
                self.sqlengine.cursor.copy_expert(sql,f)

            self.sqlengine.con.commit()  

            return True

        except Exception as e:
            print(e) 
            return False
