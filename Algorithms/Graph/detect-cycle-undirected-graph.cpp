#include<bits/stdc++.h>
using namespace std;
class Graph{
    int v;
    list<int> *adj;
    bool isCyclicUtil(int v,bool visited[],int parent);
public:
    Graph(int v);
    void addedges(int v1,int v2);
    bool isCyclic();
};
Graph::Graph(int v){
this->v=v;
adj=new list<int>[v];
}

void Graph::addedges(int v1,int v2){
adj[v1].push_back(v2);
adj[v2].push_back(v1);
}

bool Graph::isCyclic(){
bool *visited=new bool[v];
for(int i=0;i<v;i++){
    visited[i]=false;
}
for(int i=0;i<v;i++){
    if(!visited[i])
        if(isCyclicUtil(i,visited,-1))
        return true;
    }
return false;
}

bool Graph::isCyclicUtil(int v,bool visited[],int parent){
visited[v]=true;
for(auto i=adj[v].begin();i!=adj[v].end();i++){
    if(!visited[*i])
    {
        if(isCyclicUtil(*i,visited,v))
            return true;
    }
    else if(parent!=*i)
        return true;
}
return false;


}
int main(){
    int n,e,v1,v2;
cout<<"Enter no of vertices : ";
cin>>n;
cout<<"Enter no of edges : ";
cin>>e;
cout<<"Enter edges : ";
Graph G(n);
while(e--){
    cin>>v1>>v2;
    G.addedges(v1,v2);
}
bool c=G.isCyclic();
if(c){
    cout<<"Graph contains a cycle"<<endl;
}
else
{
    cout<<"Graph doesnt contain a cycle"<<endl;
}














return 0;
}
