from PyQt5.QtSql import QSqlQuery
from DataBase.ConexaoSQL import ConexaoSQL

class AluguelDAO:
    def CadastrarAluguel(aluguel):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()


        query.prepare("UPDATE Veiculo SET Alugado = 'Sim' WHERE CodigoVeic = "+aluguel.CodigoVeic)
        query.exec_()
        db.commit()

        query.prepare("INSERT INTO Aluguel(DataAluguel, DataPrazo, DataDevolucao, ValorAluguel, "
                      "ValorMulta, KmEntrada, KmSaida, CodigoCli, CodigoVeic) "
                      "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(aluguel.DataAluguel)
        query.addBindValue(aluguel.DataPrazo)
        query.addBindValue(aluguel.DataDevolucao)
        query.addBindValue(aluguel.ValorAluguel)
        query.addBindValue(aluguel.ValorMulta)
        query.addBindValue(aluguel.KmEntrada)
        query.addBindValue(aluguel.KmSaida)
        query.addBindValue(aluguel.CodigoCli)
        query.addBindValue(aluguel.CodigoVeic)
        query.exec_()
        db.commit()

    def PesquisarTodosAluguel():
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        sql = "SELECT Aluguel.*, Cliente.Nome FROM Aluguel " \
              "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli"
        query = QSqlQuery(sql)

        return query

    def PesquisarAluguel(valor, tipo):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        if tipo=='Código Aluguel':
            sql = "SELECT Aluguel.*, Cliente.Nome FROM Aluguel " \
                  "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli " \
                   "where Aluguel.CodigoAlug = " + valor
            query = QSqlQuery(sql)
        elif tipo=='Código Cliente':
            sql = "SELECT Aluguel.*, Cliente.Nome FROM Aluguel " \
                    "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli " \
                    "where Aluguel.CodigoCli = "+valor
            query = QSqlQuery(sql)
        elif tipo=='Código Veículo':
            sql = "SELECT Aluguel.*, Cliente.Nome FROM Aluguel " \
                    "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli " \
                    "where Aluguel.CodigoVeic = " + valor
            query = QSqlQuery(sql)
        elif tipo=='Nome Cliente':
            sql = "SELECT Aluguel.*, Cliente.Nome FROM Aluguel " \
                    "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli " \
                    "where Cliente.Nome = '" + valor+"'"
            query = QSqlQuery(sql)

        return query

    def DevolverVeiculo(codigoAlug, aluguel):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()



        select = "SELECT Veiculo.CodigoVeic FROM Aluguel"\
                      " INNER JOIN Veiculo ON Aluguel.CodigoVeic = Veiculo.CodigoVeic"\
                      " WHERE Aluguel.CodigoAlug = "+codigoAlug

        query = QSqlQuery(select)

        while query.next():
            codigoVeic = str(query.value(0))

        sql = "UPDATE Veiculo SET Alugado = 'Não' WHERE CodigoVeic = "+codigoVeic
        query.prepare(sql)
        query.exec_()
        db.commit()


        sql = "UPDATE Aluguel SET DataDevolucao = '"+aluguel.DataDevolucao+"', ValorMulta = '"+aluguel.ValorMulta\
                      +"', KmSaida = '"+aluguel.KmSaida\
                      +"' WHERE CodigoAlug = "+codigoAlug
        print(sql)
        query.prepare(sql)
        print
        query.exec_()
        db.commit()