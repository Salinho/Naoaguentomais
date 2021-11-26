from PyQt5.QtSql import QSqlDatabase

class ConexaoSQL:
    def getConexao():
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("Database/LocadoraSG.db3")

        return db