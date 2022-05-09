# Projeto implementação de um DFA
# ------------------------------
# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3
# ------------------------------
# Felippe Onishi Yaegashi
# RA: 20.00255-6
# ------------------------------
# states = estados
# initial_state = estado inicial
# sigma = entradas
# delta = funcionamento do automato
# final_states = estados finais
# (estado,entrada): proximo estado

import sys
import string

def simular_dfa(dfa, entrada):
    estado = dfa['initial_state']
    aceitar = False
    s = list(entrada)
    while len(s) > 0:
        c = s.pop(0)
        if c not in (dfa['sigma']):
            print('O simbolo ', c , ' nao pertence ao alfabeto do automato!')
            s.insert(0, c)
            break
        if (estado not in dfa['states']):
            print('O estado ', estado, ' nao pertence ao conjunto de estados do automato!')
            break
        estado_anterior = estado
        estado = (dfa['delta'][(estado,c)])
        #print(estado)
        print('(', estado_anterior, ',', '\'',c,'\'', ') -> ', estado)
        if estado not in dfa['states']:
            print('Nao foi possivel realizar a transicao do estado ', estado, ' com entrada ', c)
            break
    if estado in dfa['final_states'] and len(s) == 0:
        aceitar = True
    if aceitar == True:
        print('A cadeia ', entrada, ' foi aceita pelo automato!')
    else:
        print('A cadeia ', entrada, ' foi rejeitada pelo automato!')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: dfa <nome_arquivo>")
        sys.exit()

    
    # Abrir e ler o arquivo m.dfa   
    with open(sys.argv[1]) as dfa_file:
        dfa_data = dfa_file.read()

    # Converte dados e armazenar na variavel dfa
    dfa = eval(dfa_data)
    print(dfa)
    
    while (1):
        try:
            entrada = input("Insira a cadeira que deseja testar: ")
            simular_dfa(dfa, entrada)
        except:
            try:
                entrada = EOFError
                print("\nPrograma encerrado pelo usuario")
                break
            except:
                entrada = KeyboardInterrupt
                print("\nPrograma encerrado pelo usuario")
                break
            break
    
    


