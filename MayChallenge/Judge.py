def findjudge(n, trust) -> int:
    if len(trust) > 10000 or len(trust) < 1:
        return -1

    if len(trust) == 1:
        return trust[0][1]

    d = {}
    for i in range(len(trust)):
        d[trust[i][0]] = 0
        d[trust[i][1]] = 0
        print(d)

    for i in range(len(trust)):
        if trust[i][0] < 1 or trust[i][1] > n:
            return -1

        if trust[i][0] == trust[i][1]:
            return -1

        d[trust[i][0]] -= 1
        d[trust[i][1]] += 1

    for key, value in d.items():
        if value == n-1:
            return key

    return -1


print(findjudge(2, [[1,2]]))
print(findjudge(3, [[1,3],[2,3]]))
print(findjudge(3, [[1,3],[2,3],[3,1]]))
print(findjudge(3, [[1,2],[2,3]]))
print(findjudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(findjudge(1, []))




