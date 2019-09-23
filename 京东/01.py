# -*- coding:utf-8 -*-

if __name__ == "__main__":
    n = 5
    i = 0
    N = 1e5+5

    lyst = []
    while i < n:
        lyst.append(list(map(int, input().split())))



#include<bits/stdc++.h>
using namespace std;


const int maxn = 1e5+5;
const int inf = 0x3f3f3f3f;
int a1[maxn], n, min_n[maxn], max_x[maxn];

int main()
{
    ios::sync_with_stdio(0);
        cin>>n;
    int j;
    for(j=1; j<=n; j++)
        cin>>a1[j];
    min_n[n] = a1[n];
    for(j=n-1; j>=1; j--)
        min_n[j] = min(min_n[j+1], a1[j]);
    max_x[1] = a1[1];
    for(j=2; j<=n; j++)
        max_x[i] = max(max_x[i-1], a1[i]);
    int ans = 1;
    for(j=2; j<=n; j++)
        if(max_x[i-1] <= min_n[i]) ans++;
            cout<<ans<<endl;
    return 0;
}
