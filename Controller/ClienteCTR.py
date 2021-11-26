from Model.DTO.ClienteDTO import ClienteDTO
from Model.DAO.ClienteDAO import ClienteDAO

class ClienteCTR:
    def CadastrarCliente(nome, CPF, endereco, email, telefone):
        clienteDTO = ClienteDTO
        clienteDTO.Nome = nome
        clienteDTO.CPF = CPF
        clienteDTO.Endereco = endereco
        clienteDTO.Email = email
        clienteDTO.Telefone = telefone

        clienteDAO = ClienteDAO
        clienteDAO.CadastrarCliente(clienteDTO)

    def AtualizarCliente(codigoCli, nome, CPF, endereco, email, telefone):
        clienteDTO = ClienteDTO
        clienteDTO.Nome = nome
        clienteDTO.CPF = CPF
        clienteDTO.Endereco = endereco
        clienteDTO.Email = email
        clienteDTO.Telefone = telefone

        clienteDAO = ClienteDAO
        clienteDAO.AtualizarCliente(codigoCli, clienteDTO)

    def PesquisarTodosClientes():
        clienteDAO = ClienteDAO
        query = clienteDAO.PesquisarTodosClientes()
    
        return query
    
    def ExcluirCliente(codigoCli):
        clienteDAO = ClienteDAO
        clienteDAO.ExcluirCliente(codigoCli)