#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'''Notas do aluno: 
Nota 1: {nota1}
Nota 2: {nota2}
Nota 3: {nota3}
Nota 4: {nota4}''')
print(f'A média final do aluno foi de: {media}')
