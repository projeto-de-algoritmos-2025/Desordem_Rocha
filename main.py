import random
from utils.inversions import count_inversions

from game.logic import gerar_lista, embaralhar_lista, avaliar_resposta

def play_game():
    print("🎮 Bem-vindo ao Jogo Desordem!")
    original = gerar_lista()
    embaralhada = embaralhar_lista(original)

    print(f"🔀 Lista embaralhada: {embaralhada}")
    print("✏️ Digite a nova ordem separando os números com espaço:")

    entrada = input("> ")

    try:
        resposta = list(map(int, entrada.strip().split()))
        inversoes, mensagem = avaliar_resposta(resposta, original)

        if inversoes is None:
            print(mensagem)
        else:
            print(mensagem)
            print(f"🔢 Lista ordenada correta: {sorted(original)}")

    except Exception as e:
        print("⚠️ Entrada inválida.")

if __name__ == "__main__":
    play_game()
