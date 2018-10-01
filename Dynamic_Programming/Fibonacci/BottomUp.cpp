#include<bits/stdc++.h>
using namespace std;
int fib(int n){
int f1=1,f2=1,res;
for(int i=1;i<=n;i++){
    if(i==1||i==2)
        res=1;
    else{
        res=f1+f2;
        f1=f2;
        f2=res;

    }
}
return res;}
int main(){
int n;
cin>>n;
int result=fib(n);
cout<<"Ans : "<<result<<endl;




return 0;
}
