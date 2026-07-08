class Solution {
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int m = s.size();
        int n = queries.size();
        long long MOD = 1e9 + 7;

        vector<long long> pre(m + 1, 0);
        vector<long long> preV(m + 1, 0);
        vector<int> preCnt(m + 1, 0);
        vector<long long> power(m + 1, 1);

        for (int i = 1; i <= m; i++) {
            power[i] = (power[i - 1] * 10) % MOD;
        }

        for (int i = 0; i < m; i++) {
            int d = s[i] - '0';

            pre[i + 1] = pre[i] + d;
            preCnt[i + 1] = preCnt[i] + (d != 0);

            if (d == 0) {
                preV[i + 1] = preV[i];
            } else {
                preV[i + 1] = (preV[i] * 10 + d) % MOD;
            }
        }

        vector<int> result(n);

        for (int i = 0; i < n; i++) {
            int l = queries[i][0];
            int r = queries[i][1];

            int len = preCnt[r + 1] - preCnt[l];

            long long start = preV[l];
            long long end = preV[r + 1];

            long long x = (end - (start * power[len]) % MOD + MOD) % MOD;
            long long sum = pre[r + 1] - pre[l];

            result[i] = (x * sum) % MOD;
        }

        return result;
    }
};