from Model.DTO.AluguelDTO import AluguelDTO
from Model.DAO.AluguelDAO import AluguelDAO

class AluguelCTR:
    def CadastrarAluguel(DataAluguel, DataPrazo, DataDevolucao, ValorAluguel, ValorMulta, KmEntrada, KmSaida, CodigoCli, CodigoVeic):
        aluguelDTO = AluguelDTO
        aluguelDTO.DataAluguel = DataAluguel
        aluguelDTO.DataPrazo = DataPrazo
        aluguelDTO.DataDevolucao = DataDevolucao
        aluguelDTO.ValorAluguel = ValorAluguel
        aluguelDTO.ValorMulta = ValorMulta
        aluguelDTO.KmEntrada = KmEntrada
        aluguelDTO.KmSaida = KmSaida
        aluguelDTO.CodigoCli = CodigoCli
        aluguelDTO.CodigoVeic = CodigoVeic

        aluguelDAO = AluguelDAO
        aluguelDAO.CadastrarAluguel(aluguelDTO)
    
    def PesquisarTodosAluguel():
        aluguelDAO = AluguelDAO
        query = aluguelDAO.PesquisarTodosAluguel()

        return query

    def PesquisarAluguel(valor, tipo):
        aluguelDAO = AluguelDAO
        query = aluguelDAO.PesquisarAluguel(valor, tipo)

        return query

    def DevolverVeiculo(codigoAlug, dataDevol, valorMulta, kmSaida):
        aluguelDTO = AluguelDTO

        aluguelDTO.DataDevolucao = dataDevol
        aluguelDTO.ValorMulta = valorMulta
        aluguelDTO.KmSaida = kmSaida

        aluguelDAO = AluguelDAO
        aluguelDAO.DevolverVeiculo(codigoAlug, aluguelDTO)    