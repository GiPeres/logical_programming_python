cpf_usuario = '74682489070'

noveDigitos = cpf_usuario[:9]
contador_regressivo = 10

resultado = 0
for digito in noveDigitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

digito = (resultado * 10) % 11
digito = digito if digito <= 9 else 0

dezDigitos = noveDigitos + str(digito)
contador_regressivo_2 = 11

resultado_digito2 = 0
for digito in dezDigitos:
    resultado_digito2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculo = f'{noveDigitos}{digito}{digito_2}'

if cpf_usuario == cpf_calculo:
    print(f'{cpf_usuario} é valido')
else:
    print('cpf inválido!')


   

