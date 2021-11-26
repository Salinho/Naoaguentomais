from Model.DAO.VeiculoDAO import VeiculoDAO
from Model.DTO.VeiculoDTO import VeiculoDTO


class VeiculoCTR:
    def CadastrarVeiculo(modelo, marca, anoModelo, placa, alugado, kmAtual, valorDiaria, tipoVeiculo):
        veiculoDTO = VeiculoDTO
        veiculoDTO.Modelo = modelo
        veiculoDTO.Marca = marca
        veiculoDTO.AnoModelo = anoModelo
        veiculoDTO.Placa = placa
        veiculoDTO.Alugado = alugado
        veiculoDTO.KmAtual = kmAtual
        veiculoDTO.ValorDiaria = valorDiaria
        veiculoDTO.TipoVeiculo = tipoVeiculo

        veiculoDAO = VeiculoDAO
        veiculoDAO.CadastrarVeiculo(veiculoDTO)

    def AtualizarVeiculo(codigoVeic, modelo, marca, anoModelo, placa, alugado, kmAtual, valorDiaria, tipoVeiculo):
        veiculoDTO = VeiculoDTO
        veiculoDTO.Modelo = modelo
        veiculoDTO.Marca = marca
        veiculoDTO.AnoModelo = anoModelo
        veiculoDTO.Placa = placa
        veiculoDTO.Alugado = alugado
        veiculoDTO.KmAtual = kmAtual
        veiculoDTO.ValorDiaria = valorDiaria
        veiculoDTO.TipoVeiculo = tipoVeiculo

        veiculoDAO = VeiculoDAO
        veiculoDAO.AtualizarVeiculo(codigoVeic, veiculoDTO)

    def PesquisarVeiculosDisponiveis():
        veiculoDAO = VeiculoDAO
        query = veiculoDAO.PesquisarVeiculosDisponiveis()

        return query

    def PesquisarTodosVeiculos():
        veiculoDAO = VeiculoDAO
        query = veiculoDAO.PesquisarTodosVeiculos()

        return query

    def PesquisarVeiculo(valor, tipo):
        veiculoDAO = VeiculoDAO
        query = veiculoDAO.PesquisarVeiculo(valor, tipo)

        return query

    def ExcluirVeiculo(codigoVeic):
        veiculoDAO = VeiculoDAO
        veiculoDAO.ExcluirVeiculo(codigoVeic)

