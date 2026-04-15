def is_subsequence(subseq, seq):
    i = 0
    j = 0

    while i < len(subseq) and j < len(seq):
        if subseq[i] == seq[j]:
            i += 1
        j += 1

    return i == len(subseq)


# пример
S_prime = ["купить Yahoo", "купить eBay", "купить Yahoo", "купить Oracle"]
S = ["купить Amazon", "купить Yahoo", "купить eBay", "купить Yahoo", "купить Yahoo", "купить Oracle"]

print(is_subsequence(S_prime, S))
