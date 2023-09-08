def get_vowel_frequency(corpus):
    """
    Returns a list of frequency percentages for a corpus's vowels.

    :param corpus: Any valid Python string
    :return: List of frequency percentages
    """

    corpus.lower()
    sentence = corpus.lower()
    num_a = 0
    num_e = 0
    num_i = 0
    num_o = 0
    num_u = 0
    letter_only = ""
    freq_list = ""
    for letter in sentence:
        if letter.isalpha():
            letter_only += letter
    for letter in letter_only:
        if letter == "a":
            num_a +=1
        elif letter == "e":
            num_e +=1
        elif letter == "i":
            num_i +=1
        elif letter == "o":
            num_o +=1
        elif letter == "u":
            num_u +=1
    freq_a_percentage = round(((num_a / len(letter_only))*100),2)
    freq_e_percentage = round(((num_e / len(letter_only))*100),2)
    freq_i_percentage = round(((num_i / len(letter_only))*100),2)
    freq_o_percentage = round(((num_o / len(letter_only))*100),2)
    freq_u_percentage = round(((num_u / len(letter_only))*100),2)
    freq_list = [['a',freq_a_percentage],['e',freq_e_percentage],['i',freq_i_percentage],['o',freq_o_percentage],['u',freq_u_percentage]]
    return freq_list











def main():
    """
    Just some sample behavior based on the README. Feel free to try your own.
    """
    sample_text = "Do you hear the people sing?"
    vowel_frequencies = get_vowel_frequency(sample_text)
    print(vowel_frequencies)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
