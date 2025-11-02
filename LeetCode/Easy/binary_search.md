二分查找

**有序**是必要条件， 想象猜数字游戏，目标是猜一个数字，出题人会告诉你你猜的数字和target比起来是大是小，所以只要你每一次都猜中间的那个数胜率就是最高的。

```markdown
给定一个 n个元素有序的（升序）整型数组nums和一个目标值 target ，写一个函数搜索 nums 中的 target ，如果 target 存在返回下标，否则返回 `-1`。

你必须编写一个具有 `O(log n)` 时间复杂度的算法。
```

要做的就是把target和nums数组的中位数做对比，如果target大，下一次循环中就跟右半部分的中位数做对比，如果循环了‘n/2’次还是没有找到target的话就返回 ‘-1’

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
      n = len(nums)
      left, right = 0, n - 1

      while left <= right:

        mid = (left + right) // 2
        if target == nums[mid]:
          return mid
        elif target < nums[mid]:
          right = mid - 1
        else:
          left = mid + 1

      return -1
```


非常好！你的代码写得很棒！👍

让我分析一下你的代码为什么是正确的：

**优点：**

1. **边界处理正确** ：使用 `left <= right` 作为循环条件，确保能处理所有情况
2. **中间位置计算正确** ：`mid = (left + right) // 2` 是标准的二分查找中间位置计算
3. **边界更新正确** ：

* `target < nums[mid]` → `right = mid - 1`
* `target > nums[mid]` → `left = mid + 1`

1. **返回值正确** ：找到时返回下标 `mid`，没找到返回 `-1`

 **时间复杂度** ：O(log n)，符合题目要求
 **空间复杂度** ：O(1)，只用了常数空间

 **代码风格** ：

* 缩进清晰
* 变量命名合理
* 逻辑结构清晰

你的代码已经是一个标准的二分查找实现，而且通过了测试，完全正确！
