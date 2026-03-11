#Calculadora de Aprovação Escolar

nome = input("Digite o nome do Estudante: ")

soma_notas = 0
quantidade_trimestre = 3
meta_aprovacao = 180

#Coleta as notas dos 3 períodos
for i in range(1, quantidade_trimestre + 1):
    nota = float(input("Informe a nota{i}° período: "))
    soma_notas +=nota

print("-" * 30)
print(f"Estudante: {nome}")
print(f"Pontuação Total: {soma_notas}")

#Verifica o Status de aprovação
if soma_notas >= meta_aprovacao:
    print("Status: APROVADÃO! Parabens!")
else:
    pontos_faltantes
    meta_aprovacao - soma_notas
    print("Status: TENTE OUTRA VEZ!")
    print(f"Faltaram
    {pontos_faltantes}") pontos para
     atingir o minímo de
     {meta_aprovacao}."
