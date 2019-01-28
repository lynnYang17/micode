#include <iostream>
#include <cmath>
using namespace std;

int gonglu[512][512];
int tielu[512][512];
int main()
{
    // please write your code here
    int n, m, a, b;
    for(int i=1;i<=400;i++)
    {
        for(int j=1;j<=400;j++)
        {
            gonglu[i][j] = 1000000000;
            tielu[i][j] = 1000000000;
        }
    }
    for(int i=1;i<=400;i++)
    {
    	gonglu[i][i] = 0;
        tielu[i][i] = 0;
    }
    cin >> n >> m;
    while(m--)
    {
        cin >> a >> b;
    	tielu[a][b] = 1;
        tielu[b][a] = 1;
    }
    for(int i=1;i<=n;i++)
    {
    	for(int j=i+1;j<=n;j++)
        {
        	if(tielu[i][j] != 1)
            {
            	gonglu[i][j] = 1;
                gonglu[j][i] = 1;
            }
        }
    }

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout<<gonglu[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout<<tielu[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
    for(int k=1;k<=n;k++)
    {
    	for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
            	if(gonglu[i][j]>gonglu[i][k]+gonglu[k][j])
                {
                	gonglu[i][j] = gonglu[i][k]+gonglu[k][j];
                }
                if(tielu[i][j]>tielu[i][k]+tielu[k][j])
                {
                	tielu[i][j] = tielu[i][k]+tielu[k][j];
                }
            }
        
        }
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout<<gonglu[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout<<tielu[i][j]<<" ";
        }
        cout<<endl;
    }
    int ans;
    ans = max(tielu[1][n], gonglu[1][n]);
    if (ans > 1000000)
    {
    	cout<<"-1"<<endl;
    }
    else
        cout<<ans<<endl;
    return 0;
}
