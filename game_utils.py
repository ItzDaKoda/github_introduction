def print_intro():
    print("=" * 40)
    print("        SIMPLE TEXT RPG GAME")
    print("=" * 40)
    print("Defeat all enemies to win the game.")
    print("Each turn, choose to attack, heal, or use a special attack.")
    print()


def show_status(player, enemy):
    print(f"\n{player.name}: {player.hp}/{player.max_hp} HP")
    print(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP\n")


def battle(player, enemy):
    special_used = False

    while player.is_alive() and enemy.is_alive():
        show_status(player, enemy)

        print("Choose an action:")
        print("1. Attack")
        print("2. Heal")
        print("3. Special Attack")

        choice = input("> ").strip()

        if choice == "1":
            damage = player.attack(enemy)
            print(f"{player.name} attacks {enemy.name} for {damage} damage!")

        elif choice == "2":
            player.heal(6)
            print(f"{player.name} heals for 6 HP!")

        elif choice == "3":
            if special_used:
                print("You already used your special attack this battle!")
                continue
            damage = player.special_attack(enemy)
            special_used = True
            print(f"{player.name} uses Special Attack on {enemy.name} for {damage} damage!")

        else:
            print("Invalid choice. Try again.")
            continue

        if enemy.is_alive():
            damage = enemy.attack(player)
            print(f"{enemy.name} attacks {player.name} for {damage} damage!")
        else:
            print(f"{enemy.name} has been defeated!")
            return True

    return player.is_alive()