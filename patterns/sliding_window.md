[121. Best Time to Buy and Sell Stock](../../problems/0121-best-time-to-buy-and-sell-stock/)

1.  buyPrice = min(buyPrice, i)
2.  profit = max(profit, i - buyPrice)

[3. Longest Substring Without Repeating Characters](../../problems/0003-longest-substring-without-repeating-characters/)

1. Move l only when there's a duplicate in char sequence
  ```python3
        for r in range(len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l += 1
