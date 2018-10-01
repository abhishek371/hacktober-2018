#include<bits/stdc++.h>
using namespace std;
int main(){
int e,v1,v2,n;
cout<<"Enter the no of vertices : ";
cin>>n;
vector<vector<int>>graph(n,vector<int>(n));
cout<<"Enter no of edges : ";
cin>>e;
cout<<"enter the edges : "<<endl;
while(e--)
{
    cin>>v1>>v2;
    graph[v1][v2]=1;
    graph[v2][v1]=1;
}
cout<<"Adjacency Matrix : "<<endl;
for(int i=0;i<n;i++){
    cout<<"Vertex : "<<i+1<<" "<<"---> ";
    for(int j=0;j<n;j++){
        cout<<graph[i][j]<<" ";
    }
    cout<<endl;
}







return 0;
}
