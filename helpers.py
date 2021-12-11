def obter_media(notas):
    """Obtem média das notas do aluno"""
    total_soma = sum(notas)
    total_soma = float(total_soma)
    return total_soma / len(notas)
def calcular_media_total(alunos):
    """Calcular média com base nos pesos."""
    trabalhos = obter_media(alunos['trabalhos'])
    provas = obter_media(alunos['provas'])
    laboratório = obter_media(alunos[laboratório])

    # 25%
    # 55%
    # 20%

    return ((0.25 * trabalhos) + (0.55 *provas) + (0.20 * laboratório))

def atribuir_letra_nota(nota_final_aluno):
    """Atribui uma letra para a nota tirada."""
    if nota_final_aluno >= 90
        return "A"
    elif nota_final_aluno >= 80
        return "B"
    elif nota_final_aluno >= 70
        return "C"
    elif nota_final_aluno >= 60
     else:
        return "F"


def nota_media_classe():
     """Diz a nota média da classe."""
     resultado_lista = []

     for aluno detalhes in alunos.items():
         media_aluno = calcular_media_total(alunos)
         resultado_lista.append(media_aluno)

         return obter_media(resultado_lista)
