import time
import random

def print_delayed(text, delay=0.5):
    """Função para imprimir texto com um atraso por linha."""
    for line in text:
        print(line)
        time.sleep(delay)

def print_typing_effect(text, typing_speed=0.05):
    """Função para simular o efeito de digitação."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(typing_speed)
    print()

def obter_informacoes_do_personagem():
    personagem = {}
    
    personagem["Nome"] = input("Nome do jogador: ")
    personagem["Genero"] = input("Seu Gênero: ")
    personagem["Idade"] = input("Idade: ")

    return personagem

def print_ficha_personagem(personagem):
    ficha_text = [
        "==================================================",
        "                   FICHA DE USUÁRIO               ",
        "==================================================",
        f"Nome: {personagem['Nome']}",
        f"Gênero: {personagem['Genero']}",
        f"Idade: {personagem['Idade']}",
        "==================================================",
        "                      FIM                         ",
        "=================================================="
    ]

    print_delayed(ficha_text, delay=0.2)

def introduzir_vila_e_primeira_missao(nome):
    vila_text = [
        f"{nome}, ao sair da pequena taverna onde você descansou, a luz do sol banha a praça central da vila.",
        "Aos poucos, você percebe o ambiente ao seu redor: casas de madeira, lojas pequenas e um poço no centro.",
        "Os aldeões caminham lentamente, cuidando de suas tarefas diárias, mas há um certo ar de tensão no ar...",
        "Um velho se aproxima de você, com um olhar preocupado.",
        f"Velho: 'Ah, {nome}, ouvi falar das suas habilidades. Precisamos da sua ajuda!'",
        "'Algo estranho está acontecendo na floresta ao norte. As pessoas estão desaparecendo, e quem volta, não é o mesmo.'",
        "'Você poderia investigar para nós? Estou preocupado com o que possa estar acontecendo lá...'"
    ]
    print_delayed(vila_text, delay=2)

    aceitar = input("\nVocê aceita a missão? (sim/não): ").strip().lower()
    
    if aceitar == "sim":
        print_delayed([
            "Velho: 'Obrigado! Sabia que podia contar com você. Por favor, vá agora, antes que mais alguém desapareça...'", 
            "Você se dirige para a floresta, com a missão de descobrir o que está causando tanto medo na vila..."
        ], delay=2)
    else:
        print_delayed([
            "Velho: 'Entendo... Espero que mude de ideia, mas cuidado ao andar por aqui. As coisas não estão normais.'", 
            "Você decide explorar mais a vila antes de tomar uma decisão."
        ], delay=2)

def selecionar_personagem(personagem):
    # Seleção de personagem com loop para garantir escolha válida
    while True:
        print(f"\n\nSelecione seu Personagem, {personagem['Nome']}:")
        print(" (1) Mago\n (2) Necromante\n (3) Arqueiro\n (4) Paladino\n (5) Fada\n (6) Bárbaro\n (7) Gnomo")

        opcao_classe = int(input("Opção: "))

        if 1 <= opcao_classe <= 7:
            print("===================================")
            print("       Boa escolha, jogador!       ")
            print("===================================")
            break
        else:
            print("Opção inválida! Por favor, escolha um número entre 1 e 7.")

    # Define as estatísticas do personagem com base na classe escolhida
    if opcao_classe == 1:
        hp_p = 200
        atk_p = 60
        mana_p = 90
    elif opcao_classe == 2:
        hp_p = 180
        atk_p = 120
        mana_p = 110
    elif opcao_classe == 3:
        hp_p = 170
        atk_p = 110
        mana_p = 80
    elif opcao_classe == 4:
        hp_p = 220
        atk_p = 85
        mana_p = 70
    elif opcao_classe == 5:
        hp_p = 160
        atk_p = 95
        mana_p = 130
    elif opcao_classe == 6:
        hp_p = 240
        atk_p = 75
        mana_p = 60
    elif opcao_classe == 7:
        hp_p = 100
        atk_p = 50
        mana_p = 150

    # Sistema de armas para cada personagem
    armas = {
        1: ["Cajado Arcano", "Varinha Mística", "Livro de Feitiços", "Orbe de Mana"],
        2: ["Foice da Morte", "Tomo dos Mortos", "Cajado das Almas", "Manto da Ocultação"],
        3: ["Arco Longo", "Besta Leve", "Flechas Envenenadas", "Adaga Curta"],
        4: ["Espada Longa", "Martelo de Guerra", "Escudo Sagrado", "Lança Divina"],
        5: ["Varinha Encantada", "Cajado das Fadas", "Orbe de Luz", "Bênção da Luz"],
        6: ["Machado Duplo", "Clava Pesada", "Espada de Duas Mãos", "Escudo de Ferro"],
        7: ["Faca Curta", "Estilingue", "Bastão Mágico", "Poções Explosivas"]
    }

    # Exibir as opções de armas para a classe escolhida
    print("\n -_-_-_-_-_- Escolha suas armas: -_-_-_-_-_-")
    armas_selecionadas = []

    # Limita a seleção a no máximo 2 armas
    for i in range(2):
        print(f"\nArmas disponíveis para seu Personagem:" )
        for idx, arma in enumerate(armas[opcao_classe], start=1):
            print(f"({idx}) {arma}")
        
        escolha_arma = int(input("Escolha o número da arma: "))
        
        # Adiciona a arma escolhida à lista de armas do jogador
        if 1 <= escolha_arma <= len(armas[opcao_classe]):
            armas_selecionadas.append(armas[opcao_classe][escolha_arma - 1])
            armas[opcao_classe].pop(escolha_arma - 1)  # Remove a arma escolhida das opções disponíveis
        else:
            print("Opção inválida. Tente novamente.")
        
        # Se não houver mais armas disponíveis, termina a seleção
        if not armas[opcao_classe]:
            print("Todas as armas disponíveis já foram escolhidas.")
            break

    print(f"\nAs armas selecionadas para {personagem['Nome']} são: {', '.join(armas_selecionadas)}")
    return opcao_classe, armas_selecionadas

def dialogo_adicional_com_npc(personagem):
    npc_text = [
        f"{personagem['Nome']}, você retorna à praça central da vila após preparar-se para a missão.",
        "O velho está esperando por você, com um olhar preocupado e ansioso.",
        "Velho: 'Ah, você voltou! Espero que esteja pronto para o que vem pela frente...'",
        "'A floresta ao norte está cheia de perigos, e as criaturas que lá habitam estão mais agressivas do que nunca.'",
        "'Fique atento e use suas habilidades com sabedoria. Não sabemos o que pode estar à espreita.'",
        "'Aqui está um pequeno suprimento para ajudá-lo em sua jornada. Boa sorte!'"
    ]
    print_delayed(npc_text, delay=2)

def batalha(personagem, opcao_classe):
    print("\nVocê chega à floresta e começa a explorar. De repente, uma criatura feroz aparece diante de você!")

    criaturas = [
        {"Nome": "Goblin", "HP": 50, "Ataque": 10},
        {"Nome": "Lobo Selvagem", "HP": 70, "Ataque": 15},
        {"Nome": "Esqueleto", "HP": 60, "Ataque": 12},
        {"Nome": "Orc", "HP": 80, "Ataque": 18},
        {"Nome": "Espírito", "HP": 40, "Ataque": 20},
        {"Nome": "Troll", "HP": 100, "Ataque": 25},
        {"Nome": "Dragão Menor", "HP": 120, "Ataque": 30}
    ]

    # Escolha aleatória do inimigo
    criatura = random.choice(criaturas)
    print(f"\nVocê está enfrentando um {criatura['Nome']}!")

    hp_jogador = {
        1: 200,
        2: 180,
        3: 170,
        4: 220,
        5: 160,
        6: 240,
        7: 100
    }[opcao_classe]
    
    atk_jogador = {
        1: 60,
        2: 120,
        3: 110,
        4: 85,
        5: 95,
        6: 75,
        7: 50
    }[opcao_classe]
    
    print(f"\nSeu HP: {hp_jogador} | HP do {criatura['Nome']}: {criatura['HP']}")
    
    while hp_jogador > 0 and criatura["HP"] > 0:
        acao = input("\nEscolha uma ação (atacar/fugir): ").strip().lower()
        
        if acao == "atacar":
            dano = random.randint(0, atk_jogador)
            criatura["HP"] -= dano
            print(f"\nVocê atacou o {criatura['Nome']} e causou {dano} de dano!")
            
            if criatura["HP"] > 0:
                dano_recebido = random.randint(0, criatura["Ataque"])
                hp_jogador -= dano_recebido
                print(f"O {criatura['Nome']} atacou você e causou {dano_recebido} de dano.")
                
                print(f"\nSeu HP: {hp_jogador} | HP do {criatura['Nome']}: {criatura['HP']}")
            else:
                print(f"\nVocê derrotou o {criatura['Nome']}!")
                break
        elif acao == "fugir":
            print("\nVocê tentou fugir, mas a criatura é rápida! Você precisa lutar ou encontrar uma maneira de escapar.")
        else:
            print("Ação inválida! Escolha 'atacar' ou 'fugir'.")
    
    if hp_jogador <= 0:
        print("\nVocê foi derrotado... O que resta de sua jornada não pode ser mais salvo. A vila está em perigo.")
    elif criatura["HP"] <= 0:
        print("\nVocê venceu a batalha! A criatura caiu e você pode continuar sua missão.")

def main():
    # Exibir a introdução e obter as informações do personagem
    text_lines = [
        "==================================================",
        "===========  Bem vindo ao Auraden Ring ===========",
        "===========   Um mundo de fantasia e   ===========",
        "===========    criaturas incríveis,    ===========",
        "===========   numa terra distante se   ===========",
        "===========    encontra uma pequena    ===========",
        "===========   vila onde sua história   ===========",
        "===========          começa:           ===========",
        "==================================================",
    ]
    print_delayed(text_lines, delay=0.2)

    personagem = obter_informacoes_do_personagem()
    print_ficha_personagem(personagem)
    
    introduzir_vila_e_primeira_missao(personagem["Nome"])

    opcao_classe, armas_selecionadas = selecionar_personagem(personagem)

    dialogo_adicional_com_npc(personagem)

    batalha(personagem, opcao_classe)

if __name__ == "__main__":
    main()
