今天来重新做三数之和

题目：给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请你返回所有和为 `0` 且不重复的三元组。

 **注意：** 答案中不可以包含重复的三元组。

应该用双指针来做，先把给的nums进行排序，然后先定下一个数，跟左右指针相加，看是否等于0，如果等于就加入到ans里面，如果不等于就移动指针继续进行。有一个重要步骤就是要在total==0的时候避免重复，看nums[left] 和 nums[left + 1] （right指针同理）是否相等，如果相等要跳过。还有一个重要的点就是在for循环开始要有一个条件，保证定的第一个数字跟之前的数字不一样，如果一样的话就跳过本次循环，直接迭代到下一次循环。举例说明：

假设排序后的数组是：`[-1, -1, 0, 1, 2]`

**没有跳过重复的情况：**

* i=0: 固定第一个数 -1，找到 [-1, -1, 2] 和 [-1, 0, 1]
* i=1: 固定第一个数 -1（重复），找到 [-1, 0, 1]（重复！）

**有跳过重复的情况：**

* i=0: 固定第一个数 -1，找到 [-1, -1, 2] 和 [-1, 0, 1]
* i=1: 发现 nums[1] == nums[0]（都是-1），`continue` 跳过

完整代码：

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
              total = nums[i] + nums[left] + nums[right]

              if total == 0:
                ans.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                  left += 1
                while left < right and nums[right] == nums[right - 1]:
                  right -= 1
                left += 1
                right -= 1
              elif total < 0:
                left += 1
              else:
                right -= 1

        return ans

```
