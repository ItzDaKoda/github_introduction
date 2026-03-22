from character import Player, Enemy
from game_utils import battle, print_intro


def main():
    print_intro()

    player_name = input("Enter your hero's name: ").strip()
    if not player_name:
        player_name = "Hero"

    player = Player(player_name, 30, 8, 2)

    enemies = [
        Enemy("Goblin", 15, 5, 1),
        Enemy("Skeleton", 20, 6, 1),
        Enemy("Dark Knight", 25, 7, 2),
    ]

    print(f"\nWelcome, {player.name}! Your adventure begins now.\n")

    for enemy in enemies:
        print(f"A wild {enemy.name} appears!")
        won = battle(player, enemy)

        if not won:
            print("\nGame Over. Your hero has fallen.")
            return

        player.heal(5)
        print(f"\n{player.name} survives the battle and recovers 5 HP.")
        print(f"Current HP: {player.hp}/{player.max_hp}\n")

    print(f"Congratulations, {player.name}! You defeated all the enemies!")


if __name__ == "__main__":
    main()