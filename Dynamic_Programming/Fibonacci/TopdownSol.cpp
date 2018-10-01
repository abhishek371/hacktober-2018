#include<bits/stdc++.h>
//#define max 100
//int memo[max];
int fib(int n,int *memo){
if(memo[n-1]!=0){
    return memo[n-1];
}
else if(n==1||n==2){
    return 1;
}
else{
    int f=fib(n-1,memo)+fib(n-2,memo);
    memo[n-1]=f;
    return f;
}

}

using namespace std;
int main(){
int n;
cin>>n;
int memo[n]={0};
int result=fib(n,memo);
cout<<"Ans: "<<result<<endl;
return 0;
}
