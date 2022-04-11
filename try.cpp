#include<bits/stdc++.h>
vector<vector<int>> optimizeMemoryUsage(int k, vector<int> download, vector<int> game)
{
    // Write your code here 
    vector<vector<int>> ans;
    for(int i=0;i<download.size();i++){
        vector<int> val;
        if(download[i]==k){
            ans.push_back({i,-1});
        }
        
        int need = k-download[i];
        for(int j=0;j<game.size();j++){
            if(game[j]==k){
            ans.push_back({-1,i});
                
            }
            if(game[j]==need){
                val = {i,j};
                ans.push_back(val);
            }
        }
    }
    return ans;
}
int main(){
    vector<int> download={2,1,5,9};
    vector<int> game={9,2,4};
    vector<int> ans =optimizeMemoryUsage(8,download,game);
    for(auto i:ans){
        cout<<i<<endl;
    }
}