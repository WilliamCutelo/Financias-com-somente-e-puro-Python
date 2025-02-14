from models import *
from view import *
from datetime import datetime

#para criar uma interface
class UI:
    def start(self):
        while True:
            print('''
            [1] -> Criar conta
            [2] -> Desativar conta
            [3] -> Transferir dinheiro
            [4] -> Movimentar dinheiro
            [5] -> Total contas
            [6] -> Filtrar histórico
            [7] -> Gráfico
            ''')
            #Para interagir com a interface
            try:
                choice = int(input('Escolha uma opção: '))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                continue  

            match choice:
                case 1:
                    self._criar_conta()
                case 2:
                    self._desativar_conta()
                case 3:
                    self._transferir_saldo()
                case 4:
                    self._movimentar_dinheiro()
                case 5:
                    self._total_contas()
                case 6:
                    self._filtrar_movimentacoes()
                case 7:
                    self._criar_grafico()
                case _:  #Para um numero fora da serie
                    print("Opção inválida. Por favor, escolha uma opção de 1 a 7.")
                    continue  
         
#função de criar uma conta        
    def _criar_conta(self):
        print('Digite o nome de algum dos bancos abaixo:')
        for banco in Bancos:
            print(f'---{banco.value}---')
            
        banco = input().title()
        valor = float(input('Digite o valor em sua conta:'))
        
        conta = Conta(banco=Bancos(banco), valor=valor)
        criar_conta(conta)
        
#função para chamar o desativar a conta       
    def _desativar_conta(self):
        print('Escolha a conta que deseja desativar.')    
        for i in listar_contas():
            if i.valor == 0:
                print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')
                
        id_conta = int(input())
        
        try:
            desativar_conta(id_conta)
            print('Conta desativada com sucesso.')
        except ValueError:
            print('Essa conta ainda possui saldo, faça uma transferência')

    def _transferir_saldo(self):
        print('Escolha a conta retirar o dinheiro.')
        
        for i in listar_contas():
            print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')
        conta_retirar_id = int(input())
        print('Escolha a conta para enviar dinheiro.')
        
        for i in listar_contas():
            if i.id != conta_retirar_id:
                print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')
        conta_enviar_id = int(input())
        valor = float(input('Digite o valor para transferir: '))
        transferir_saldo(conta_retirar_id, conta_enviar_id, valor)
#função para chamar o movimentar dinheiro
    def _movimentar_dinheiro(self):
        print('Escolha a conta.')
        for i in listar_contas():
            print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')
        conta_id = int(input())
        valor = float(input('Digite o valor movimentado: '))
        print('Selecione o tipo da movimentação')
        for tipo in Tipos:
          print(f'---{tipo.value}---')

        tipo = input().title()
        historico = Historico(conta_id=conta_id, tipo=Tipos(tipo), valor=valor, data=date.today())
        movimentar_dinheiro()
        
#função para chamar de ver o total de contas        
    def _total_contas(self):
        print(f'R$ {total_contas()}')
#função para chamar o movimentação de contas especificas        
    def _filtrar_movimentacoes(self):
        data_inicio = input('Digite a data de início: ')
        data_fim = input('Digite a data final: ')
        data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
        data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()
        for i in buscar_historicos_entre_datas(data_inicio, data_fim):
            print(f'{i.valor} - {i.tipo.value}')
#Para criar um grafico        
    def _criar_grafico(self):
        criar_grafico()


UI().start()
