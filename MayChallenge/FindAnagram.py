from collections import Counter


def findAnagrams(s: str, p: str):
    ns, np = len(s), len(p)
    print(ns)

    if ns < np:
        return []

    p_count = Counter(p)
    print('p_count',p_count)
    s_count = Counter()

    output = []
    # sliding window on the string s
    for i in range(ns):
        print('i', i)
        print('np', np)
        # add one more letter
        # on the right side of the window
        s_count[s[i]] += 1
        print('s_count',s_count)
        # remove one letter
        # from the left side of the window
        if i >= np:
            if s_count[s[i - np]] == 1:
                del s_count[s[i - np]]
            else:
                s_count[s[i - np]] -= 1
        # compare array in the sliding window
        # with the reference array
        if p_count == s_count:
            output.append(i - np + 1)
            print('output', output)

    return output


print(findAnagrams("cbaebabacd","abc"))
print(findAnagrams("abab","ab"))
