import random
from utils.inversions import count_inversions

def gerar_lista(tamanho=6, intervalo=(1, 20)):
    return random.sample(range(intervalo[0], intervalo[1] + 1), tamanho)

def embaralhar_lista(lista):
    copia = lista.copy()
    random.shuffle(copia)
    return copia

def avaliar_resposta(resposta, original):
    if sorted(resposta) != sorted(original):
        return None, "❌ Os números inseridos não correspondem à lista original!"

    inversoes = count_inversions(resposta)
    mensagem = f"✅ Sua lista tem {inversoes} inversões."

    if inversoes == 0:
        mensagem += "\n🏆 Parabéns! Você ordenou perfeitamente!"
    elif inversoes <= 3:
        mensagem += "\n🥈 Muito bem! Você chegou perto!"
    else:
        mensagem += "\n📉 Sua ordenação ainda pode melhorar. Tente novamente!"

    return inversoes, mensagem
