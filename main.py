import random
from utils.inversions import count_inversions

def play_game():
    print("Bem-vindo ao Jogo Desordem!")
    original = random.sample(range(1, 8), 7)  # lista aleatória de 7 números
    scrambled = original.copy()
    random.shuffle(scrambled)

    print(f"Lista embaralhada: {scrambled}")
    print("Digite a nova ordem separando os números com espaço:")
    user_input = input("> ")

    try:
        user_list = list(map(int, user_input.strip().split()))
        if sorted(user_list) != sorted(original):
            print("❌ Os elementos não correspondem à lista original!")
            return
        inversions = count_inversions(user_list)
        print(f"✅ Sua lista tem {inversions} inversões.")
        if inversions == 0:
            print("🏆 Parabéns! Você ordenou perfeitamente!")
        else:
            print(f"🔢 A ordenação correta teria 0 inversões. Tente novamente!")
    except:
        print("⚠️ Entrada inválida.")

if __name__ == "__main__":
    play_game()
