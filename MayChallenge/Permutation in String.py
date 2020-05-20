from collections import Counter


def checkInclusion(s1: str, s2: str):
    ns, np = len(s2), len(s1)

    print(ns)
    print(np)
    if ns < np:
        return []

    p_count = Counter(s1)
    print(p_count)
    s_count = Counter()
    output = False
    # sliding window on the string s
    for i in range(ns):
        # add one more letter
        # on the right side of the window
        s_count[s2[i]] += 1
        print(s_count)
        # remove one letter
        # from the left side of the window
        print('i', i)
        if i >= np:
            if s_count[s2[i - np]] == 1:
                del s_count[s2[i - np]]
            else:
                s_count[s2[i - np]] -= 1
        # compare array in the sliding window
        # with the reference array
        if p_count == s_count:
            output = True

    return output


print(checkInclusion("ab", "eidbaooo"))
