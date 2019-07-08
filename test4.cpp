#include <bits/stdc++.h>

using namespace std;

int main()
{
    // please write your code here
    string s;
    cin >> s;
    stack<char> a;
    for(int i=0; i<s.size(); i++){
        if (s[i]=='(' || s[i]=='[' ||s[i]=='{' ){
            a.push(s[i]);
        }
        else if (s[i]==')'){
            if (a.top() == '('){
                a.pop();
            }
            else
                return 0;
        }
        
        else if (s[i]=='}'){
            if (a.top() == '{'){
                a.pop();
            }
            else
                return 0;
        }
        
        else if (s[i]==']'){
            if (a.top() == '['){
                a.pop();
            }
            else
                return 0;
        }
    }
    
    if (a.empty())
        return 1;
    return 0;
}
