def translate(original_word,index):
    vovels = "aeiou"
    if original_word[0].lower() in vovels:
        result = original_word + "ma"
    else:
        result = original_word[1:]+original_word[0]+ "ma"
    result += "a"*index



def translate_sentence_to_goat_latin(original_sentence):
    num_space = original_sentence.count(" ")
    space_index = original_sentence.find(" ")
    start_index = -1
    final_result = ""
    for word_num in range(num_space+1):
        original_word = original_sentence[start_index+1 :space_index]
        final_result += translate_sentence_to_goat_latin(original_word,word_num + 1)+" "

        start_index = space_index
        space_index = original_sentence.find(" ", space_index+1)
        if space_index == -1:
            space_index = len(original_sentence)
    return final_result





def main():
    """
    Just an example. Feel free to try your own, but note that the auto-grader will only be evaluating the function
    translate_sentence_to_goat_latin() and will completely ignore the main function!
    """

    print(translate_sentence_to_goat_latin("I speak Goat Latin"))

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
