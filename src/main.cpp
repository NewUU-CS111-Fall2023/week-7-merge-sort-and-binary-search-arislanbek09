/*
 * Author: Arislanbek Kalbaev
 * Date: December 1, 2023
 * Name: Arisanbek Kalbaev
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <queue>
using namespace std;

int main() {
    cout << "Task 1" << endl;

    cout << "Implemented in Python" << endl;

    cout << "Task 2" << endl;

    cout << "Implemented in Python" << endl;

    cout << "Task 3" << endl;



    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        vector<int> A(N);
        vector<int> B(M);

        for (int i = 0; i < N; ++i) {
            cin >> A[i];
        }

        for (int i = 0; i < M; ++i) {
            cin >> B[i];
        }

        vector<int> merged;
        merge(A.begin(), A.end(), B.begin(), B.end(), back_inserter(merged), greater<int>());

        for (int i = 0; i < merged.size(); ++i) {
            cout << merged[i] << " ";
        }
        cout << endl;
    }

    //O((N + M) * log(N + M))

    cout << "Task 4" << endl;

    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int left = matrix[0][0], right = matrix[n - 1][n - 1];

        while (left < right) {
            int mid = left + (right - left) / 2;
            int count = 0;
            int j = n - 1;

            for (int i = 0; i < n; ++i) {
                while (j >= 0 && matrix[i][j] > mid) {
                    j--;
                }
                count += (j + 1);
            }

            if (count < k) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    int main() {
        int n, k;
        cin >> n >> k;

        vector<vector<int>> matrix(n, vector<int>(n));

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> matrix[i][j];
            }
        }

        int result = kthSmallest(matrix, k);

        cout << result << endl;
    // O(k * log(min(n, k))) where n = number of elements, k = elements in each row


    cout << "Task 5" << endl;



    return 0;
}
