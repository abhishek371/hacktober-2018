#include<bits/stdc++.h>
using namespace std;
int main(){
int t,n,v;
cin>>t;
while(t--){
    cin>>n;
    vector<int>a;
    map<int,int>ma;
    vector<int>b;
    map<int,int>mb;
    for(int i=0;i<n;i++){
        cin>>v;
        ma[v]++;
        a.push_back(v);
    }
    for(int i=0;i<n;i++){
        cin>>v;
        mb[v]++;
        b.push_back(v);
    }

    int flag=0;
    for(int i=0;i<n;i++){
        if(mb[a[i]]!=0){
            int k=abs(i-(n/2));
            int m=n/2;
            if(b[k+n/2]==a[i]||b[n/2-k]==a[i]){
                cout<<k<<endl;
                flag=1;
                break;
            }
        }


    }
    if(flag!=1){
        cout<<"-1"<<endl;
    }


}




}

