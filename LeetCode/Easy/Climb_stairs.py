from typing import List
# 回溯算法解决爬楼梯问题
def backtrack(choices: List[int], state: int, n: int, res: List[int]) -> int:
    """回溯"""
    if state == n:
        res[0] += 1
    for choice in choices:
        # 剪枝：不允许越过第 n 阶
        if state + choice > n:
            continue
        # 尝试：做出选择，更新状态
        backtrack(choices, state + choice, n, res)
        # 回退

def climbing_stairs_backtrack(n: int) -> int:
    """爬楼梯：回溯"""
    choices = [1, 2] 
    state = 0  
    res = [0]  
    backtrack(choices, state, n, res)
    return res[0]

if __name__ == "__main__":
    n = 6
    print(climbing_stairs_backtrack(n))  # 输出：13

# 深度优先搜索
def dfs(i: int) -> int:
    """搜索"""
    # 已知 dp[1] 和 dp[2] ，返回之
    if i == 1 or i == 2:
        return i
    # dp[i] = dp[i-1] + dp[i-2]
    count = dfs(i - 1) + dfs(i - 2)
    return count

def climbing_stairs_dfs(n: int) -> int:
    """爬楼梯：深度优先搜索"""
    return dfs(n)

if __name__ == "__main__":
    n = 6
    print(climbing_stairs_dfs(n))  # 输出：13


# 记忆化搜索
memo = {}
def memo_dfs(i: int) -> int:
    """记忆化搜索"""
    # 查备忘录，避免重复计算
    if i in memo:
        return memo[i]
    if i == 1 or i == 2:
        return i
    # dp[i] = dp[i-1] + dp[i-2]
    memo[i] = memo_dfs(i - 1) + memo_dfs(i - 2)
    return memo[i]
def climbing_stairs_memo(n: int) -> int:
    """爬楼梯：记忆化搜索"""
    return memo_dfs(n)
if __name__ == "__main__":
    n =  36
    print(climbing_stairs_memo(n))  # 输出：14930352



# 动态规划
def climbing_stairs_dp(n: int) -> int:
    """爬楼梯：动态规划"""
    if n <= 2:
        return n
    # dp[i] 表示到达第 i 阶的方法数
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        # 状态转移方程⭐️
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == "__main__":
    n =  36
    print(climbing_stairs_dp(n))  # 输出：14930352