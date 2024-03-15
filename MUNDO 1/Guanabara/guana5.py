# Praticando formatações do .format

nome = input('Qual seu nome?')
# :20 significa que vão ser adicionado 20 caracteres
print('Prazer em te conhecer {:20}!'.format(nome))
#* '>' alinhamento pra direita, '<' alinhamento esquerda, '^' central
print('Prazer em te conhecer {:^20}!'.format(nome))
# o '=' pode ser qualquer símbolo, será colocado nos caracteres
print('Prazer em te conhecer {:=^20}!'.format(nome))
