#include<bits/stdc++.h>
using namespace std;
int main(){
 int t;
 cin>>t;
 while(t--){
    int n,a,b;
    cin>>n;
    vector<pair<int,int>>v;
    for(int i=0;i<n;i++){
        cin>>a>>b;
        v.push_back(make_pair(b,a));
    }
    sort(v.begin(),v.end());
    int c=0;
    for(int i=0;i<(n-1);i++){
        if((v[i].first<=v[i+1].second)&&(v[i].second>=v[i+1].first)){
            c++;
        }


    }
    cout<<c<<endl;



 }







}
