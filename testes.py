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
ESPACAMENTO = 42

while True:
    print("=" * ESPACAMENTO)

    garrafas_refrigerante = float(input("Quantidade de garrafas de refrigerante: "))

    if garrafas_refrigerante > LIMITE_GARRAFAS:
        print("[!] Limite máximo permitido de 10 litros!")
        continue

    break


print("=" * ESPACAMENTO)
capacidade_das_garrafas = float(input("Capacidade das garrafas (litros): "))

print("=" * ESPACAMENTO)
capacidade_dos_copos = float(input("Capacidade dos copos (mililitros): "))

while True:
    print("=" * ESPACAMENTO)

    total_de_pessoas = float(input("Quantidade de pessoas no evento: "))

    if total_de_pessoas > LIMITE_PESSOAS:
        print("Limite máximo de 200 pessoas!")
        continue

    break


total_litros_de_refrigerante = garrafas_refrigerante * capacidade_das_garrafas
quantidade_de_copos = (total_litros_de_refrigerante * LITRO_EM_ML) // capacidade_dos_copos
resto_na_maquina = (total_litros_de_refrigerante * LITRO_EM_ML) % capacidade_dos_copos
copos_que_faltam = total_de_pessoas - quantidade_de_copos

contexto = ''

if copos_que_faltam < 0:
    contexto = 'Sobrarão'

else:
    contexto = 'Faltarão'

print('-' * ESPACAMENTO + '\n' + '-' * ESPACAMENTO)

print(f"Quantidade de refrigerante: {total_litros_de_refrigerante} L.")
print(f"A máquina produzirá {round(quantidade_de_copos)} copos de {capacidade_dos_copos} ml.")
print(f"Quantidade de refrigerante restante na máquina: {resto_na_maquina} ml.")

# no segundo placeholder, se faltam copos, o restante na máquina será descontado da soma da capacidade dos copos faltantes e \
# se sobram copos, o resto será incluído na soma da capacidade dos copos que sobram.
if copos_que_faltam != 0:
    print(f"{contexto} {abs(round(copos_que_faltam))} copos ({abs(round((copos_que_faltam * capacidade_dos_copos - resto_na_maquina) / 1000, 2))} litros).")
