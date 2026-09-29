# 0/1 Knapsack using Bottom-Up and Top-Down

# Bottom-Up
def knapsack_bottom(weights, values, W):
    n = len(weights)

    dp = [[0] * (W + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Top-Down
def knapsack_top(weights, values, W, n, dp):

    if n == 0 or W == 0:
        return 0

    if dp[n][W] != -1:
        return dp[n][W]

    if weights[n - 1] <= W:
        dp[n][W] = max(
            values[n - 1] + knapsack_top(
                weights, values, W - weights[n - 1], n - 1, dp
            ),
            knapsack_top(weights, values, W, n - 1, dp)
        )
    else:
        dp[n][W] = knapsack_top(weights, values, W, n - 1, dp)

    return dp[n][W]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5

print("Bottom-Up:", knapsack_bottom(weights, values, W))

n = len(weights)
dp = [[-1] * (W + 1) for i in range(n + 1)]

print("Top-Down:", knapsack_top(weights, values, W, n, dp))