#include<bits/stdc++.h>

using namespace std;

int minCoins(vector<int>& coins, int sum) {
    vector<int> dp(sum + 1, INT_MAX);
    dp[0] = 0;

    for (int i = 1; i <= sum; ++i) {
        for (int j = 0; j < coins.size(); ++j) {
            if (coins[j] <= i && dp[i - coins[j]] != INT_MAX) {
                dp[i] = min(dp[i], dp[i - coins[j]] + 1);
            }
        }
    }

    return dp[sum];
}

int main() {
    vector<int> coins = {1, 3, 6};
    int sum = 11; 

    int minCoinsRequired = minCoins(coins, sum);
    cout << "Minimum coins " << sum << " is: " << minCoinsRequired << endl;

    return 0;
}
