[只出现一次的数字](https://leetcode.cn/problems/single-number/)

遇到这种题的时候我总是下意识的去想enumerate，然后看哪个数字是出现了一次的，需要改变这种下意识，还有！字典是没有append操作的，我每次像sb一样老是去写append...


在这个问题中，**不需要**使用 `enumerate`，因为：

* 我们只需要数字本身，不需要索引
* `enumerate` 会返回 `(index, value)` 元组，但我们只需要 `value`

代码实现

```python
def singleNumber(self, nums: List[int]) -> int:
    count = {}
    for num in nums:
      if num in count:
        count[num] += 1
      else:
        count[num] = 1
    for num, freq in count.items():
      if freq == 1:
        return num
```

想想还有没有优化空间？（位运算）

核心思想：**异或运算 (XOR)**

异或运算的特性：

* `a ^ a = 0` (相同数字异或为0)
* `a ^ 0 = a` (任何数字与0异或还是本身)
* 异或运算满足交换律和结合律

代码示例：

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # 等价于 result = result ^ num
        return result
```

```
# Dry run
初始: result = 0
0 ^ 4 = 4
4 ^ 1 = 5
5 ^ 2 = 7
7 ^ 1 = 6
6 ^ 2 = 4
最终返回 4
```

* 所有成对出现的数字异或后都会变成0
* 最后只剩下那个单独的数字

在面试的时候，这个问题，面试官想听到的都是位运算这个算法。
