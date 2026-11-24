def busiest_window(deliveries: list[int], k: int) -> int:
    s = sum(deliveries[:k])
    ans = s 
    for i in range(k,len(deliveries)):
        s += deliveries[i] - deliveries[i-k]
        if s > ans :
            ans = s 
    return ans 
    
    """ we are given a list of dsily delivery counts and window size k , 
    and we need to find the maximum total deliveries across any k ,
     consecutive days 
    we used a fixed size sliding first i calculate the sum of the 1st k days
     and
     store as curr window sum and best ans so far , thne as i loop from index
      k to the end of th elist ,
      i sslide th ewindow one step at a time , adding  new day entering window and
       subtracting the day leaving it updating the max whnever the new 
       sum is higher 
    that brings the tc down to n , awith space big o 1 ,
     it handles edge cases like k = 1 k =e entire list length all seroes etc , 
    the problme guarantees , 1<= k <= n and because ans starts at the first
     windows sum rather than 0
     it would work properly if negative numbers were allowd """