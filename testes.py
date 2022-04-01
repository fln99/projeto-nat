'''
Protótipo: Máquina de Refrigerante

Componentes do grupo:
- Olivia
- Guilherme
- Felipe
'''

while True:
    garrafas_refri = int(input("Quantidade de garrafas de refrigerante: "))

    if garrafas_refri > 10:
        print("Limite máximo permitido de 10 litros!")
        continue
    break

capacidade_garrafas = float(input("Capacidade das garrafas (litros): "))
capacidade_copos = float(input("Capacidade dos copos (mililitros): "))

while True:
    total_pessoas = int(input("Quantidade de pessoas no evento: "))

    if total_pessoas > 200:
        print("Limite máximo de 200 pessoas!")
        continue
    break


total_litros_refri = garrafas_refri * capacidade_garrafas
quantidade_copos = (total_litros_refri * 1000) / capacidade_copos
copos_faltantes = total_pessoas - quantidade_copos

print('-' * 20)

print(f"{round(quantidade_copos,2)} copos de {capacidade_copos} ml")

palavra_chave = ''

if copos_faltantes < 0:
    palavra_chave = 'a mais'
    
else:
    palavra_chave = 'faltantes'

print(f"""{abs(round(copos_faltantes, 2))} copos {palavra_chave}.\n{abs(round((copos_faltantes * capacidade_copos) / 1000))} litros {palavra_chave}.""")

