接雨水这个题我之前也做过，但现在还是不太会了，重新来思考一下。

刚看了下题解，动态规划这个我感觉还挺神奇的，我打算学习一下这个解法，然后解决之后后面一定要记得再自己做一遍，然后理解这个动态规划算法。

就是从左往右遍历一遍数组，看看每个位置能积水的最大值是多少，再从右往左遍历一遍，最后这两个数组中取每个位置的最小值并减去柱子本身的高度，就是这个位置能接到的雨水量，把每个位置的加起来就得到最终结果。

我又重新复习了一遍，理解更多了。就是从左往右刷一遍，不太好用语言表达，直接用代码来表示吧。


```python
# 29/10/2025
n = len(height)
leftMax = [0] * n
rightMax = [0] * n

leftMax[0] = height[0]
for i in range(1, n):
	leftMax[i] = max(height[i], leftMax[i - 1])

rightMax[n-1] = height[n-1]
for i in range(n-2, -1, -1):
	rightMax[i] = max(height[i], rightMax[i + 1])

total = 0
for i in range(n):
	total += min(leftMax[i], rightMax[i]) - height[i]
```
