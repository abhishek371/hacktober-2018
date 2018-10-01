#include<bits/stdc++.h>
using namespace std;
class graph{
int v;
list<int> *adj;
public:
graph(int v);
void addedges(int v1,int v2);
void DFS(int src);
void DFSUtil(int v,bool visited[]);
};
graph::graph(int v){
this->v=v;
adj=new list<int>[v];
}

void graph::addedges(int v1,int v2){
adj[v1].push_back(v2);
//adj[v2].push_back(v1);
}

void DFS(int src){

bool *visited=new bool[src];
for(int i=0;i<src;i++){
    visited[i]=false;
}
void graph::DFSUtil(int src,bool visited[]);
{
   visited[src]=true;
   cout<<src<<" ";
   for(auto i=adj[src].begin();i!=adj[src].end();i++){
    if(visited[*i]!=true){
        visited[*i]=true;

    }
   }

}

}





int main(){
Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    cout << "Following is Depth First Traversal"
            " (starting from vertex 2) \n";
    g.DFS(2);

    return 0;











return 0;
}
