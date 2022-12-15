#include <iostream>
#include <queue>

using namespace std;


int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	priority_queue<int, vector<int>, greater<int> > pq;
	int n;
	cin >> n;
	if (n == 0) {
		cout << "0" << std::endl;
		return (0);
	}
	for (int i = 0; i<n; i++) {
		int j;
		cin >> j;
		pq.push(j);
	}
	int sum = 0;
	int ref = 0;
	while (1)
	{
		int a = pq.top();
		pq.pop();
		int b = pq.top();
		pq.pop();
		sum = a + b;
		ref += sum;
		if (pq.size() == 0)
			break;
		pq.push(sum);
	}
	cout << ref;

}
