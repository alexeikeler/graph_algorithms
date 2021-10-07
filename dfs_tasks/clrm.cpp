#include <iostream>
#include <vector>

using namespace std;


vector<vector<char>> graph;
vector<vector<int>> components;

int clusters_counter = 1;

bool bfs(int m, int n) {
    if (m < 0 || m >= graph.size())
        return false;
    if (n < 0 || n >= graph[0].size())
        return false;

    if (graph[m][n] == '.')
        return false;

    if (components[m][n] != 0)
        return false;

    components[m][n] = clusters_counter;

    bfs(m - 1, n); bfs(m, n - 1);
    bfs(m + 1, n); bfs(m, n + 1);

    return true;
}

int main(int argc, char *argv[]) {
    int n, m;
    char t;
    cin >> m >> n;

    graph.resize(m, vector<char>(n));
    components.resize(m, vector<int>(n));

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> t;

            graph[i][j] = t;
        }
    }

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (bfs(i, j)) {
                ++clusters_counter;
            }
        }
    }

    cout << clusters_counter - 1 << endl;

    return 0;
}