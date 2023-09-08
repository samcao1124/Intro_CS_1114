DNA_FILE_NAME = "dna_sequence.txt"
FILE_OPEN_MODE = 'r'
A_INDEX, C_INDEX, T_INDEX, G_INDEX = 0, 1, 2, 3
COUNT_INDEX = 1
def get_file_contents(file_path):
    """
    Reads the contents of a single-line txt file.

    :param file_path: A string representing the path of the file
    :return: A string containing the contents of the file
    """
    file = open(file_path,'r')
    file_read = file.read().strip()
    file.close()
    return file_read




def update_frequencies(old_frequencies, new_sequence):
    """
    Updates a list of nucleotide frequencies to reflect the addition of a new sequence's nucleotides.

    :param old_frequencies: A list of frequency tuples
    :param new_sequence: A string representing a DNA sequence
    :return: An updated list of frequency tuples
    """
    update_list = []
    num_a = 0
    num_c = 0
    num_t = 0
    num_G = 0
    for dna in new_sequence:
        if dna == "A":
            num_a +=1
        elif dna == "C":
            num_c +=1
        elif dna == "T":
            num_t +=1
        elif dna == "G":
            num_G +=1
    a_values = old_frequencies[0][1]
    c_values = old_frequencies[1][1]
    t_values = old_frequencies[2][1]
    g_values = old_frequencies[3][1]
    new_a_value = a_values + num_a
    new_c_value = c_values + num_c
    new_t_value = t_values + num_t
    new_g_value = g_values + num_G
    update_list = [('A', new_a_value),('C', new_c_value),('T', new_t_value),('G', new_g_value)]
    return update_list








def main():
    """
    Just some sample behavior based on the README. Feel free to try your own.
    """
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    # new_sequence = "ACCCGTTA"
    new_sequence = get_file_contents(DNA_FILE_NAME)
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    print(new_frequencies)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
