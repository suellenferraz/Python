notas = list(map(float, input().split(',')))

alunos_aprovados = 0
alunos_reprovados = 0

for nota in notas:
  if nota >= 5.0:
    alunos_aprovados += 1
  else:
    alunos_reprovados += 1

media = sum(notas) / len(notas)
    
print(f'Número de Alunos Aprovados: {alunos_aprovados}')
print(f'Número de Alunos Reprovados: {alunos_reprovados}')
print(f'Média da Turma: {media:.2f}')