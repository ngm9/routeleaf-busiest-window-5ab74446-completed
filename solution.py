def busiest_window(deliveries: list[int], k: int) -> int:
    s = sum(deliveries[:k])
    ans = s 
    for i in range(k,len(deliveries)):
        s += deliveries[i] - deliveries[i-k]
        if s > ans :
            ans = s 
    return ans 
    