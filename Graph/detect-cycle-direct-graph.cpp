#include<bits/stdc++.h>
using namespace std;
class Graph{
int v;
list<int> *adj;
bool DFSUtil(int v,string color[]);
public:
    Graph(int v);

    bool isCyclic();
    void addedges(int v1,int v2);
};
Graph::Graph(int v){
this->v=v;
adj=new list<int>[v];

}
void Graph::addedges(int v1,int v2){
adj[v1].push_back(v2);
}

bool Graph::isCyclic(){
string *color=new string[v];
for(int i=0;i<v;i++){
    color[i]="White";
}
for(int i=0;i<v;i++){
    if(color[i]=="White")
        if(DFSUtil(i,color)==true)
        return true;
}
return false;
}

bool Graph::DFSUtil(int v,string color[]){
color[v]="Gray";
for(auto i=adj[v].begin();i!=adj[v].end();i++){
    if(color[*i]=="White")
        if(DFSUtil(*i,color))
        return true;
    else if(color[*i]=="Gray")
        return true;
}
color[v]="Black";
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
