"""
Máquina de Refrigerante.

Componentes:
- Olivia
- Guilherme
- Felipe
"""

LIMITE_GARRAFAS = 10
LIMITE_PESSOAS = 200
LITRO_EM_ML = 1000
ESPACAMENTO = 52

print("Atenção: Limite máximo de 10 garrafas e 200 pessoas.")

while True:
    print("=" * ESPACAMENTO)

    garrafas_refrigerante = float(input("Quantidade de garrafas de refrigerante: "))

    if garrafas_refrigerante > LIMITE_GARRAFAS or garrafas_refrigerante < 1:
        print("[!] Limite máximo permitido de 10 garrafas e mínimo de 1 garrafa!")
        continue

    break

while True:
    print("=" * ESPACAMENTO)

    capacidade_das_garrafas = float(input("Capacidade das garrafas (litros): "))

    if capacidade_das_garrafas <= 0:
        print("[!] Insira a capacidade das garrafas.")
        continue

    break

while True:
    print("=" * ESPACAMENTO)

    capacidade_dos_copos = float(input("Capacidade dos copos (mililitros): "))

    if capacidade_dos_copos < 50:
        print("[!] O mínimo de capacidade do copo é de 50 ml.")
        continue

    break

while True:
    print("=" * ESPACAMENTO)

    total_de_pessoas = float(input("Quantidade de pessoas no evento: "))

    if total_de_pessoas > LIMITE_PESSOAS or total_de_pessoas < 3:
        print("Limite máximo de 200 pessoas e mínimo de 3 pessoas!")
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
print(f"A máquina é capaz de produzir {round(quantidade_de_copos)} copos de {capacidade_dos_copos} ml.")
print(f"Refrigerante restante na máquina: {resto_na_maquina} ml.")

# no segundo placeholder, se faltam copos,
# o restante na máquina será descontado da soma da capacidade dos copos faltantes e
# se sobram copos, o resto será incluído na soma da capacidade dos copos que sobram.
if copos_que_faltam != 0:
    print(f"{contexto} {abs(round(copos_que_faltam))} copos"
          f"({abs(round((copos_que_faltam * capacidade_dos_copos - resto_na_maquina) / 1000, 2))} litros).")
