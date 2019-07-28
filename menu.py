#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Biblioteca padrão
from os import system
from time import sleep

def start_menu():
    try:
        system('cls')
        print('Menu [versão 1.0]' + '\n' +
            '(c) 2019 Pedro Lucas. Todos os direitos reservados.\n')
        opcao = 0
        print('*' * 30)
        lista = ['MENU PRINCIPAL', 'Opção 1', 'Opção 2', 'Limpar tela', 'Sair']
        for index, item in enumerate(lista):
            if index == 0:
                print(f'{item}')
            else:
                print(f'[ {index} ]' + f' {item} ')

        opcao = int(input('\n>>>>> Opção: '))

        for index, item in enumerate(lista):
            if opcao == index:

                if opcao == 1:
                    opcao1()

                elif opcao == 2:
                    opcao2()

                elif opcao == 3:
                    limpar_tela()

                elif opcao == 4:
                    sair()

                else:
                    msg = 'Aviso: Opção inválida'
                    formata_str(msg)
                    sleep(3)
                    system('cls')
                    start_menu()

    except ValueError:
        msg = 'Aviso: Somente números são válidos...'
        formata_str(msg)
        sleep(3)
        system('cls')
        start_menu()
    except Exception:
        pass

def formata_str(msg):
    msg = f'>>>>> {msg}'
    tamanho_msg = len(msg)
    print('*' * tamanho_msg)
    print(msg)

def opcao1():
    opcao = 0
    print('*' * 30)
    print('Você escolheu a opção 1\n')
    print ("""[ 1 ] Opção 1 \n[ 2 ] Sair\n""")

    opcao = int(input('>>>>> Opção: '))
    if opcao == 1:
        pass

    elif opcao == 2:
        sair()

def lista_opcoes():
    lista = ['MENU PRINCIPAL', 'Opção 1', 'Opção 2', 'Limpar tela', 'Sair']

    for index, item in enumerate(lista):
        return index, item


def limpar_tela():
    msg = ('Limpando a tela, por favor, este processo leva alguns'
                        ' segundos...')
    formata_str(msg)
    sleep(5)
    system('cls')
    start_menu()

def sair():
    msg = 'Finalizando... Volte sempre!'
    formata_str(msg)
    sleep(3)
    system('cls')
    exit

def opcao2():
    pass

start_menu()
