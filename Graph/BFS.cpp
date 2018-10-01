#include<bits/stdc++.h>
using namespace std;
class Graph
{
   int v;
   list<int> *adjlist;

   public:
   Graph(int v);
   void addedges(int v1,int v2);
   void BFS(int src);
};

Graph::Graph(int v){
this->v=v;
adjlist=new list<int>[v];
}

void Graph::addedges(int v1,int v2){
adjlist[v1].push_back(v2);
}


void Graph::BFS(int src){
bool *visited = new bool[v];
for(int i=0;i<v;i++){
    visited[i]=false;
}
queue<int>q;
visited[src]=true;
q.push(src);
while(!q.empty()){
    int v=q.front();
    cout<<v<<" ";
    q.pop();
    list<int>::iterator i;
    for(i=adjlist[v].begin();i!=adjlist[v].end();i++){
        if(visited[*i]==false){
            q.push(*i);
            visited[*i]=true;
        }
    }
}
}

int main(){
Graph g(4);
    g.addedges(0, 1);
    g.addedges(0, 2);
    g.addedges(1, 2);
    g.addedges(2, 0);
    g.addedges(2, 3);
    g.addedges(3, 3);

    cout << "Following is Breadth First Traversal "
         << "(starting from vertex 2) \n";
    g.BFS(2);

    return 0;
}


