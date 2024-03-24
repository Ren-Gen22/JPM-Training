#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<string> arr;
    // vector<int> f;
    string st, find;
    int n, mini = INT_MAX, k;
    while (cin.peek() != '\n' && cin >> st)
    {
        arr.push_back(st);
    }
    cin >> k;
    cin >> find;
    n = arr.size();
    cout << "out" << endl;
    for (int i = 0; i < n; i++)
    {
        int mi;

        if (arr[i] == find)
        {
            // f.push_back(i);
            if (i == k)
            {
                mi = i;
            }
            else if (i < k)
            {
                mi = k - i;
            }
            else if (i > k)
            {
                mi = i - k;
            }
        }
        if (mi < mini)
        {
            mini = mi;
        }
    }

    cout << mini << endl;
    return 0;
}