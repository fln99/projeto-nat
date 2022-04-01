'''
Protótipo: Máquina de Refrigerante.

Componentes:
- Olivia
- Guilherme
- Felipe
'''

LIMITE_GARRAFAS = 10
LIMITE_PESSOAS = 200
LITRO_EM_ML = 1000

while True:
    garrafas_refrigerante = int(input("Quantidade de garrafas de refrigerante: "))

    if garrafas_refrigerante > LIMITE_GARRAFAS:
        print("Limite máximo permitido de 10 litros!")
        continue

    break

capacidade_das_garrafas = float(input("Capacidade das garrafas (litros): "))
capacidade_dos_copos = float(input("Capacidade dos copos (mililitros): "))

while True:
    total_de_pessoas = int(input("Quantidade de pessoas no evento: "))

    if total_de_pessoas > LIMITE_PESSOAS:
        print("Limite máximo de 200 pessoas!")
        continue

    break


total_litros_de_refrigerante = garrafas_refrigerante * capacidade_das_garrafas
quantidade_de_copos = (total_litros_de_refrigerante * LITRO_EM_ML) / capacidade_dos_copos
copos_que_faltam = total_de_pessoas - quantidade_de_copos

contexto = ''

if copos_que_faltam < 0:
    contexto = 'a mais'

else:
    contexto = 'faltantes'

print('-' * 20)

print(f"{round(quantidade_de_copos)} copos de {capacidade_dos_copos} ml")

print(f"""{abs(round(copos_que_faltam))} copos {contexto}.\n{abs(round((copos_que_faltam * capacidade_dos_copos) / 1000))} litros {contexto}.""")
