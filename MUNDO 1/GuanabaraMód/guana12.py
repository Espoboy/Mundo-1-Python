# Ex 24 Ler um nome de uma cidade e dizer se começa com Santo

c = input('Diga o nome de uma cidade: ')
cid = c.strip()
# Transformo tudo em maiúsculo para não falhar na verificação
print(cid[:5].upper() == 'SANTO') 