def get_decoded_string_by_skip(corpus, step):
    result = corpus[step-1::step]
    return(result)




def main():
    """
    Just an example. Feel free to try your own, but note that the auto-grader will only be evaluating the function
    get_decoded_string_by_skip() and will completely ignore the main function!
    """
    test_corpus = "QnHTpSrGyXOodQpwvuYPzuvnicjNqdiKCzL KmnIFEKSijXuaoXNxp pykxh.VQwGokpwABnqhBSLitrXouuzlTIBm"
    test_step = 6

    print(get_decoded_string_by_skip(corpus=test_corpus, step=test_step))

# DO NOT WRITE CODE BELOW THIS LINEresult = corpus[step-1::step]
#     return (result)


if __name__ == '__main__':
    main()
