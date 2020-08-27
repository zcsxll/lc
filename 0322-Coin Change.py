from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        results = [amount + 1] * (amount + 1) #初始化全部答案为amount+1
        results[0] = 0 #第0个答案是0，循环从1开始
        for i in range(1, amount + 1): #依次计算1到amount的最优答案。这里是amount+1，因为range是左开右闭的
            for coin in coins: #每个最优答案的求取，都需要遍历全部的硬币
                if i >= coin: #如果某个硬币小于i，说明它可以是组成i的一部分
                    results[i] = min(results[i], results[i-coin] + 1) #是否使用这个硬币，取决于两个答案的大小
        # print(results) #至此，从1到amount的全部最优答案都有了
        return results[-1] if results[-1] <= amount else -1 #返回最有一个答案，如果它没有被更新过，说明它无法被组成

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11

    ret = Solution().coinChange(coins, amount)
    print(ret)

