def f(n, m, votes, prices):

    candidate_prices = [[] for i in range(m)]  #  0  m-1
    k = 0
    cnt = []
    for i in range(n):
        candidate_prices[votes[i]-1].append(prices[i])
    for i in range(m):
        candidate_prices[i].sort()
        k = max(k, len(candidate_prices[i]))
        cnt.append(len(candidate_prices[i]))
    k = k + 1
    min_cost = max(prices)*n
    while k > 0:
        target_vote = cnt[0]
        rest = []
        cost = 0
        #  第一类人
        for i in range(1, m):
            if cnt[i] >= k:
                for j in range(cnt[i]-k+1):
                    cost += candidate_prices[i][j]
                    target_vote += 1
                #抽取cnt[i]-k+1个最小的代价后，后面的代价也需要添加到rest里面去
                rest.extend(candidate_prices[i][cnt[i]-k+1:])
            else:
                rest.extend(candidate_prices[i])
        if target_vote > k:
            break
# 第二类人
        if target_vote < k:
            diff = k - target_vote
            if rest:
                rest.sort()
                for i in range(diff):
                    cost += rest[i]
        min_cost = min(min_cost, cost)
        k -= 1
    return min_cost

if __name__ == '__main__':
    n, m = input().strip().split()
    votes = []
    prices = []
    for _ in range(int(n)):
        vote, price = input().strip().split()
        votes.append(int(vote))
        prices.append(int(price))
    print(f(int(n), int(m), votes, prices))
