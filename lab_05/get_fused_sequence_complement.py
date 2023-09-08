def get_fused_sequence_complement(sequence_a, sequence_b):
    fused_sequence = str()
    min_num = min(len(sequence_a), len(sequence_b))
    for i in range(min_num):
        fused_sequence = fused_sequence + sequence_a[i] + sequence_b[i]
    fused_sequence = fused_sequence + sequence_a[min_num:]
    if min_num == sequence_b:
        fused_sequence = fused_sequence + sequence_b[min_num]
    fused_sequence_new = str()
    for i in fused_sequence:
        fused_sequence_new = fused_sequence_new + get_complement(i)
    return fused_sequence_new

def get_complement(nucleotide):
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    else:
        return ' '





nucleotide = 'A'
complement = get_complement(nucleotide)

print(complement)

def main():
    """
    Just some sample behavior. Feel free to try your own!
    """
    sequence_a = "ACTGGGTA"
    sequence_b = "TTZAG"
    fused_sequence_complement = get_fused_sequence_complement(sequence_a, sequence_b)
    print(fused_sequence_complement)


# DO NOT WRITE CODE BELOW THIS LINE

if __name__ == '__main__':
    main()
