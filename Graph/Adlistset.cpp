
#include<bits/stdc++.h>
using namespace std;
int main(){
int e,v1,v2,n;
cout<<"Enter the no of vertices : ";
cin>>n;
set<int,greater<int> >graph[n];
cout<<"Enter no of edges : ";
cin>>e;
cout<<"enter the edges : "<<endl;
while(e--)
{
    cin>>v1>>v2;
    graph[v1].insert(v2);
    graph[v2].insert(v1);
}
cout<<"Adjacency list : "<<endl;
for(int i=0;i<n;i++){
    cout<<"Vertex : "<<i+1<<" "<<"---> ";
    set<int,greater<int> > l=graph[i];
    for (auto i = l.begin(); i != l.end(); i++) {
    cout<<*i<<" ";
}
    cout<<endl;
}








return 0;
}
