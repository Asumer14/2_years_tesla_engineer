边界情况：1) 只有一间房子，就偷它  2) 只有两间房子，就偷那个更值钱的
对于大于两间房 (k>2) 的情况：

1. 偷窃第 k 间房屋，那么就不能偷窃第 k−1 间房屋，偷窃总金额为前 k−2 间房屋的最高总金额与第 k 间房屋的金额之和。
2. 不偷窃第 k 间房屋，偷窃总金额为前 k−1 间房屋的最高总金额。
   在两个选项中选择偷窃总金额较大的选项，该选项对应的偷窃总金额即为前 k 间房屋能偷窃到的最高总金额。

用 dp[i] 表示前 i 间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：


```mathematica
dp[i]=max(dp[i−2]+nums[i],dp[i−1])
```

最后返回的答案为：**dp[n-1]** 代码如下：

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
      n = len(nums)
      if not nums:
        return 0
      if n == 1:
        return nums[0]
    
      dp = [0] * n
      dp[0] = nums[0]
      dp[1] = max(nums[0], nums[1])

      for i in range(2, n):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
  
      return dp[n-1]
```
