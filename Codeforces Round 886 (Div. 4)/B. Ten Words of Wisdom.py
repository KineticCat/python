def find_winner(responses):
    max_quality = 0
    winnerID = -1
    for i, response in enumerate(responses):
        words, quality = response
        if words<=10 and quality >= max_quality:
            max_quality =quality
            winnerID = i +1
    return winnerID

t = int(input())

for _ in range(t):

    n = int(input())
    responses = []
    for _ in range(n):
        words, quality = map(int, input().split())
        responses.append((words, quality))
    print(find_winner(responses))
