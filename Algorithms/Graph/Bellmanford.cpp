#include<bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
struct node
{

    int first,second,third;
};
int main(){
int v,k;
cin>>v;
cin>>k;
int e,v1,v2,v3;
cin>>e;
vector<node>d;
while(e--)
{
    cin>>v1>>v2>>v3;
    d.push_back({v1-1,v2-1,v3});
    d.push_back({v2-1,v1-1,v3});
}
vector<int>dist(v,INF);
dist[0]=0;
for (int i = 1; i <= v-1; i++)
{
for (int j = 0; j < d.size(); j++)
{
int u = d[j].first;
int v = d[j].second;
int weight =d[j].third;
int m=dist[u] + weight;
int q=m/k;
if(q%2!=0){
    m=k*(q+1);
}
if (dist[u] != INF && m< dist[v])
   dist[v] = m;
}
}
/*for(int i=0;i<dist.size();i++){
    cout<<dist[i]<<endl;
}*/
cout<<dist[v-1]<<endl;


}
