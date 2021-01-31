def calcula_nota(object):
    object.nota = 0
    if object.questao_1 == object.gabarito.questao_1:
        object.nota += object.gabarito.peso_1
    if object.questao_2 == object.gabarito.questao_2:
        object.nota += object.gabarito.peso_2
    if object.questao_3 == object.gabarito.questao_3:
        object.nota += object.gabarito.peso_3
    if object.questao_4 == object.gabarito.questao_4:
        object.nota += object.gabarito.peso_4
    if object.questao_5 == object.gabarito.questao_5:
        object.nota += object.gabarito.peso_5
    return object.nota