//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  
  public:
    int maxLength(string& str) {
        int ans=0;
        int op=0,cl=0;
        for(int i=0;i<str.size();i++)
        {
            if(str[i]=='(')
            {
                op++;
            }
            else
            {
                cl++;
            }
            
            if(op==cl)
            {
              ans=max(ans,op);
            }
            if(cl>op)
            {
                op=0;
                cl=0;
            }
        }
        op=0,cl=0;
        for(int i=str.size()-1;i>=0;i--)
        {
            if(str[i]=='(')
            {
                op++;
            }
            else
            {
                cl++;
            }
            
            if(op==cl)
            {
                ans=max(ans,op);
            }
            if(op>cl)
            {
                op=0;
                cl=0;
            }
        }
        
        return ans*2;
    }

};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        cin >> S;

        Solution ob;
        cout << ob.maxLength(S) << "\n";
    }
    return 0;
}
// } Driver Code Ends