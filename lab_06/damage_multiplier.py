def get_damage_multiplier(pokemon_level, pokemon_speed):
    import random
    Random_number = random.randrange(0,256)
    Threshold_number = (pokemon_speed / 2)
    Multiplier_damage = (2*pokemon_level + 5) / (pokemon_level + 5)
    if Threshold_number > Random_number:
        Multiplier_damage
        return (Multiplier_damage)
    else:
        return (1)









def main():
    """
    Just an example. Feel free to try your own, but note that the auto-grader will only be evaluating the function
    get_damage_multiplier() and will completely ignore the main function!
    """

    pokemon_name = "Chandelure"
    pokemon_move_name = "Shadow Ball"
    pokemon_level = 100
    pokemon_speed = 80

    number_of_tests = 20

    for test_number in range(number_of_tests):
        # Testing this several times to get a feel for its behavior. Feel free to change the number of tests!
        damage_multiplier = get_damage_multiplier(pokemon_level, pokemon_speed)

        print("Test #{}: {}'s {}'s damage will be multiplied by {}!".format(test_number + 1, pokemon_name,
                                                                            pokemon_move_name.lower(),
                                                                            damage_multiplier))


# DO NOT WRITE CODE BELOW THIS LINE

if __name__ == '__main__':
    main()
