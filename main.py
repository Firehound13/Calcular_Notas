from helpers import alunos, calcular_media_total, atribuir_letra_nota, nota_media_classe
"""Calculadora de notas acadêmicas
pontuação:
90 = A
80 = B
70 = C
60 = D

"""

alunos = {
    'Leonardof':
         {
    'nome': 'Leonardo Feitosa'
    'trabalhos':'[60, 80, 90, 75]
    'provas':[80, 70]
    'laboratório':[60,80]
         },
    'Eduardob':
           {
     'nome':'Eduardo Bozza'
     'trabalhos':[40, 50]
     'provas':[70, 90]
     'laboratório':[80, 50]
           },
     'Larissac':
           {
    'nome':Larissa Castanhari
    'trabalhos':[80, 70, 65, 100]
    'provas':[70, 90]
    'laboratório':[80, 90]
           },
     'Franciscom':
             {
    'nome':'Francisco Mendes'
    'trabalhos':[80, 90, 50, 70]
    'provas':[70, 50]
    'laboratório':[90,60]
             }
             }

if _name__ == __main__:
# for looping no dicionário de alunos e calcular suas respectivas notas
   for aluno, detalhes in alunos.items():
       print(f"\n {alunos[aluno]['nome']}")
       print("--------")
       media_total_aluno = round(calcular_media_total[alunos][aluno], 1)
       print(f"Média de nota do(a) alunos é {alunos[aluno]['nome']")
       print(f"Notal final do aluno(a) é {alunos[aluno]['nome']} é:{atribuir_letra_nota[media_total_aluno]}")

# Calcula a média total
       media_classe = nota_media_classe

       print(f"Média da classe é: {round(media_classe), 1}")
       print(f"Nota final da classe é: {atribuir_letra_nota[media_classe]}")
