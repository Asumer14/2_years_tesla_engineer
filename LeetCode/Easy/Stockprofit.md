# 买卖股票的最佳时机

### 暴力解法

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      # violent solution
      profit = 0
      for i in range(len(prices)):
        for j in range(1, len(prices)-2):
          if prices[j] - prices[i] >= 0:
            profit = max(profit, prices[j] - prices[i])

      return profit
    
```

### 只经历一次循环


 **问题** ：我们真的需要双重循环吗？

* 能不能在一次遍历中同时记录最低买入价和最大利润？
* 遍历时，如果当前价格比之前的最低价格还低，就更新最低价格
* 否则，计算当前利润并更新最大利润

最低买入价、最大利润

在从左至右遍历中，不断的更新minimum值和max_profit

```python
      ## Optimize (one loop, dynamic programming)
      minimum = float('inf')
      max_profit = 0

      for price in prices:
        minimum = min(minimum, price)
        max_profit = max(max_profit, price - minimum)
  
      return max_profit

```
