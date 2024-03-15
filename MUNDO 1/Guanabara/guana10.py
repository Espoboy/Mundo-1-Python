#Ex 8 Conversor de medidas, transformar metros em km, hc, dca, dc, cm e mm

med = float(input('Quantos metros: '))
dec = med * 10
cent = dec * 10
mili = cent * 10
deca = med / 10
hec = deca / 10
km = hec / 10


print(med, 'é equivalente a {:.1f} quilômetros, {:.1f} hectômetros,'.format(km, hec))
print('{:.1f} decâmetros, {:.1f} decímetros, {:.1f} centímetros e {:.1f} milímetros.'.format(deca, dec, cent, mili))