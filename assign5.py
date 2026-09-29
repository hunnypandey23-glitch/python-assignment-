x = input("Enter first sequence: ")
y = input("Enter second sequence: ")

m = len(x)
n = len(y)

dp = [["" for j in range(n + 1)] for i in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if x[i - 1] == y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + x[i - 1]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

lcs = dp[m][n]

print("LCS:", lcs)
print("Length of LCS:", len(lcs))