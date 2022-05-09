Sigma = ['a','b']   # conjunto de símbolos 
Q = [0,1,2,3]       # conjunto de estados
q0 = 0              # estado inicial
F = [3]             # conjunto de estados finais
# tabela (função) de transição de estados
delta = [ [1, 0], [2, 1], [3, 2], [3, 3] ]
# função que executa o autômato
def reconhecer(cadeia):
    estado = q0
    fim_cadeia = False
    i = 0   # índice do símbolo
    try:
        while not fim_cadeia:
            if i == len(cadeia):
                fim_cadeia = True
            else:
                simbolo =  cadeia[i]
                proximo_estado = \
                    delta[estado][Sigma.index(simbolo)]
                estado = proximo_estado
            i = i + 1
        if estado in F:
            print('A cadeia ', cadeia, ' foi reconhecida')
        else:
            print('A cadeia ', cadeia, ' foi rejeitada')
    except ValueError: # símbolo fora de sigma
        print('A cadeia ', cadeia, ' foi rejeitada')
    except Exception as e:
        print('Erro executando o autômato: ', e)
# testes
if __name__ == '__main__':
    reconhecer('babbbbabbaaaa') # aceita: >3 a's
    reconhecer('babbbb') # rejeita: < 3 a's
    reconhecer('baabbbba') # aceita: = 3 a's
    reconhecer('baaxbbba') # rejeita: x