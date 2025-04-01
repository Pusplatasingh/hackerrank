def matchingStrings(strings, queries):

    string_count = {s: strings.count(s) for s in set(strings)}
    return [string_count.get(query, 0) for query in queries]

if __name__ == "__main__":
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    q = int(input())
    queries = [input().strip() for _ in range(q)]
    
    results = matchingStrings(strings, queries)
    for result in results:
        print(result)
