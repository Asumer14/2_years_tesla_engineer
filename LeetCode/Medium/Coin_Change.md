继续来看动态规划相关的题，今天看这个零钱兑换。题目说有不同面值的coin，存在数组coin里面，然后有一个目标值amount，要求用最少的硬币数来凑到amount，最开始的想法就是用贪心策略，总是选择amount下最大的面值来凑，但不一定每次都能得到最优解，比如有1，2，5，7，10面值的硬币，amount=14，贪心算法的话会选10 -> 2 -> 2，这样的话需要三张，但其实用7面值的两张就够了。这就是为什么我们在面对这道题的时候必须选择动态规划来解决而不是贪心策略。

具体做的话，首先需要定义一个数组dp用来存放组成小于amount的每一个金额的最优解。初始化：

```python
def coinChange(self, coins: List[int], amount: int) -> int:

	dp = [amount + 1] * (amount + 1)
	dp [0] = 0
```

然后用两层循环来更新dp数组中的每一个值：

```python
for i in range(1, amount + 1):
	for coin in coins:
		if i >= coin:
			dp[i] = min(dp[i], dp[i - coin] + 1)
```

dp[i - coin] + 1 这行代码的含义是凑出金额[i - coin] 的最少硬币数，然后+1就是加上当前选择的这枚硬币，在所有可能的硬币选择中，找到硬币数最少的方案。

最后判断一下是否可以组成amount，如果凑不出就return-1:
```python
if dp[amount] == amount + 1:
	return - 1
else:
	return dp[amount]
```
