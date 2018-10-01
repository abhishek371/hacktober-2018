#include<bits/stdc++.h>
using namespace std;
int main(){
int e,v1,v2,n;
cout<<"Enter the no of vertices : ";
cin>>n;
vector<int>graph[n];
cout<<"Enter no of edges : ";
cin>>e;
cout<<"enter the edges : "<<endl;
while(e--)
{
    cin>>v1>>v2;
    graph[v1].push_back(v2);
    graph[v2].push_back(v1);
}
cout<<"Adjacency list : "<<endl;
for(int i=0;i<n;i++){
    cout<<"Vertex : "<<i+1<<" "<<"---> ";
    for(int j=0;j<graph[i].size();j++)
        cout<<graph[i][j]<<" ";

    cout<<endl;
}








return 0;
}
