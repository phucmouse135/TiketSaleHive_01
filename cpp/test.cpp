#include<bits/stdc++.h>
using namespace std;

// DEFINE 
#define ll long long
#define pb push_back
#define fi first
#define se second
#define all(x) x.begin(), x.end()

// CONST 
const ll INF = 1e18;
const int MOD = 1e9 + 7;
const int MAXN = 200000;

// Graph 


// Init 

int tknp(vector<int>& a , int x){
    int l= 0 , r = a.size() -1 ; 
    while( l <= r){
        int mid = l + (r-l) /2;
        if(a[mid] == x) return mid;
        else if (a[mid] < x) l = mid + 1 ;
        else r = mid -1 ; 
    }
    return -1;
}
// timf min giam r , tim max tang l 



void solve(){
}

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> map;
    for(string s: strs){
        string k = s;
        sort(k.begin(), k.end());
        map[k].push_back(s);
    }
    // vector<pair<string , vector<string>>> v(map.begin(), map.end());
    // sort(v.begin(), v.end() , [](auto &a , auto &b){
    //     return a.second.size() < b.second.size();
    // });
    vector<vector<string>> result;
    for(auto &p : map){
        result.push_back(p.second);
    }
    return result;
}

// prefix sum
int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> map;
    int n = nums.size();
    int ans = 0;
    int prefixSum[n];
    prefixSum[0] = nums[0];
    for(int i = 1; i<n; i++){
        prefixSum[i] = prefixSum[i-1] + nums[i];
    }
    for(int i =0 ; i<n; i++){
        if (prefixSum[i] == k)ans += 1;
        if(map.count(prefixSum[i] - k)){
            // cout<<i<<" ";
            ans += map[prefixSum[i] - k];
        }
        map[prefixSum[i]] += 1;
    }
    return ans;
}

int longestConsecutive(vector<int>& nums) {
    unordered_set<int> set(nums.begin(), nums.end());
    int result = 0;
    for(int i : set){
        if(set.find(i-1) != set.end()) continue;
        int length = 1;

        while(set.find(i+length) != set.end()){
            length +=1;
        }

        result = max(result, length);
    }        
    return result;
}

vector<vector<int>> threeSum(vector<int>& nums) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;

    for(int i = 0; i<n; i++){
        if(i > 0 && nums[i] == nums[i-1])continue;

        int j = i + 1 , k = n-1;
        while(j<k){
            int s = nums[i] + nums[j] + nums[k];
            if(s == 0){
                result.push_back({nums[i] , nums[j], nums[k]});
                // cout << nums[i]<<" "<< nums[j]<<" "<< nums[k]<<endl;
                j += 1;
                k -= 1;
                while(nums[j] == nums[j-1] && j < k)j+=1;
                while(nums[k] == nums[k+1] && j < k)k-=1;
            }
            else if (s < 0){
                j += 1;
            }
            else k -= 1;
        }
    }
    return result;
}

int maxArea(vector<int>& height) {
    int n = height.size();
    int l = 0 , r = n - 1 ;
    int maxArea = 0 ;

    while(l < r){
        maxArea = max(maxArea, min(height[l] , height[r]) * (r - l));

        if(height[l] < height[r])l+=1;
        else r -=1;
    }
    return maxArea;
}
int rightBinarySearch(vector<int>& nums, int x){
    int l = 0, r = nums.size()-1;

    int ans = -1 ; 
    while(l <= r){
        int mid = l + (r-l)/2;
        if(nums[mid] <= x){
            ans = mid ; 
            l = mid + 1;
        }
        else r = mid - 1;
    }
    return ans;
}

int leftBinarySearch(vector<int>& nums, int x){
    int l = 0, r = nums.size()-1;

    int ans = -1 ; 
    while(l <= r){
        int mid = l + (r-l)/2;
        if(nums[mid] >= x){
            ans = mid ; 
            r = mid - 1;
        }
        else l = mid + 1;
    }
    return ans;
}


vector<int> searchRange(vector<int>& nums, int target) {
    int left = leftBinarySearch(nums, target); 
    int right = rightBinarySearch(nums, target);
    if(left == -1 || right == -1) return {-1, -1};
    if(nums[left] != target) return {-1, -1};
    return {left, right};
}



int lengthOfLongestSubstring(string s) {
    unordered_set<char> set;
    int n = s.size();
    int l = 0 , r = 0;
    int result = 0;
    while(r < n){
        while(set.find(s[r]) != set.end() && l <= r){
            set.erase(s[l]);
            l++;
        }
        set.insert(s[r]);
        result = max(result , r - l + 1);
        r++;
    }
    return result;
}

bool visited[300][300];
void bfs(int x, int y , vector<vector<char>>& grid){
    int dx[4] = {0,0 , 1, -1};
    int dy[4] = {1 , -1 , 0 , 0};
    int n = grid.size();
    int m = grid[0].size();

    queue<pair<int, int>> q;
    q.push({x,y});
    visited[x][y] = 1;

    while(!q.empty()){
        pair<int, int> p = q.front();
        int x = p.first;
        int y = p.second;
        q.pop();

        for(int i = 0 ; i<4; i++){
                int xa = x + dx[i];
                int ya = y + dy[i];
                if(xa >= 0 && xa <n && ya >= 0 && ya < m && grid[xa][ya] =='1' && visited[xa][ya] == 0){
                    visited[xa][ya] = 1 ;
                    // cout<< "Visiting: "<<xa<<" "<<ya<<endl;
                    q.push({xa, ya});
                }
        }
    }

}

int numIslands(vector<vector<char>>& grid) {
    
    int n = grid.size();
    int m = grid[0].size();

    int count = 0 ;

    for(int i = 0 ; i <n ; i++){
        for(int j = 0 ; j<m; j++){
            if(visited[i][j] == 0 && grid[i][j] == '1'){
                // cout<<"Start BFS at: "<<i<<" "<<j<<endl;
                bfs(i, j , grid);
                count++;
            }
        }
    }
    return count;


}
void backtrack(vector<int>& candidates, int target, vector<vector<int>>& result , vector<int>& current, int idx, int sum){
    if(sum == target){
        for(auto &p : result)if (p == current) return;
        result.push_back(current);
        return;
    }

    if(sum > target || idx == candidates.size()) return;

    for(int i = idx; i < candidates.size(); i++){
        if(i > idx && candidates[i] == candidates[i-1])continue;
        current.push_back(candidates[i]);
        backtrack(candidates, target, result, current, i + 1, sum + candidates[i]);
        current.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> current;

    int sum = 0;
    sort(candidates.begin(), candidates.end());

    backtrack(candidates,target, result, current , 0, sum);

    return result;
}

int jump(vector<int>& nums) {
    vector<int> dp(nums.size(), 1e7 + 1);
    dp[0] = 0;
    int n = nums.size();
    for(int i = 0; i < n;i++){
        int k = nums[i];
        int m = min(n, i + k + 1);
        for(int j = i + 1; j < m; j++){
            dp[j] = min(dp[j], dp[i] + 1);
        }
    }
    return dp[n-1];
}

void backtrack2(vector<int>& nums , vector<vector<int>>& result , vector<int>& current, vector<int>& check, int idx){
    if(current.size() == nums.size()){
        result.push_back(current);
        return;
    }

    for(int i = 0; i < nums.size(); i++){
        if(i > 0 && nums[i] == nums[i-1] && check[i-1] == 0) continue;
        if(check[i] == 0){
            current.push_back(nums[i]);
            check[i] = 1;
            backtrack2(nums, result, current, check , i);
            check[i] = 0 ;
            current.pop_back();
        }
    }
}

vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> result; 
    vector<int> current; 
    vector<int> check(11, 0);
    backtrack2(nums, result , current ,check , 0);
    return result;
}

void rotate(vector<vector<int>>& matrix) {
    int n = matrix.size();
    int m = matrix[0].size();
    
    vector<vector<int>> temp(m, vector<int>(n));
    for(int i=0; i<m ; i++){
        vector<int> k;
        for(int j = n - 1 ; j >= 0; j--){
            k.push_back(matrix[j][i]);
        }
        temp[i] = k;
    }

    matrix = temp ;

}

int maxSubArray(vector<int>& nums) {
    long long maxS = -1e9 - 7;
    long long s = 0 ;
    for(int i=0 ; i<nums.size(); i++){
        s += nums[i];
        if(s < 0){
            maxS = max(maxS , s);
            s = 0;
        }
        else {
            maxS = max(maxS , s);
        }
    }
    return maxS;
}

vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> result(n , vector<int>(n, 0));
    int i = 0, k = 0 ;
    while(i < (int) n/2 + 1){
        for(int j= i ; j< n - i; j++){
            result[i][j] = ++k;
        }

        for(int j = i + 1 ; j < n - i; j++){
            result[j][n-i] = ++k;
        }

        for(int j = n - i - 1; j >= i ; j --){
            result[n-i][j] = ++k;
        }

        for(int j = n-i - 1; j > i ; j--){
            result[j][i]= ++k;
        }
        i++;
    }       
    return result; 
}

bool canJump(vector<int>& nums) {
    int maxReach = 0 ;
    for(int i=0; i< nums.size(); i++){
        if(i > maxReach) return false;
        maxReach= max(maxReach, i + nums[i]);
    }
    return true;
}


vector<vector<int>> merge(vector<vector<int>>& intervals) {
    stack<pair<int, int>> st; 
    sort(intervals.begin(), intervals.end());

    for(int i = 0; i<intervals.size() ; i++){
        
        if(!st.empty() && st.top().second >= intervals[i][0]){
                pair<int, int> k = st.top();
                st.pop();
                int n = min(intervals[i][0] , k.first);
                int m = max(intervals[i][1], k.second);
                st.push({n,m});
                cout<< "Merging: "<<n<<" "<<m<<endl;
        }
        else{
            st.push({intervals[i][0], intervals[i][1]});
        }
    }

    vector<vector<int>> result;
    while(!st.empty()){
        pair<int, int> k = st.top(); 
        st.pop();
        vector<int> temp; 
        temp.push_back(k.first);
        temp.push_back(k.second);
        result.push_back(temp);
    }
    sort(result.begin(), result.end());
    return result;


}

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    intervals.push_back(newInterval);
    return merge(intervals);
}

int qhd(string word1, string word2){
    vector<vector<int>> dp(word1.size()+1, vector<int>(word2.size()+1, 0));
    int n = word1.size();
    int m = word2.size();

    for(int i =1 ; i<n; i++){
        dp[i][0] = i;
    }
    for(int j = 1; j <=m ; j++){
        dp[0][j] = j;
    }


    for(int i = 1 ; i<= word1.size(); i++){
        for(int j = 1; j <= word2.size(); j++){
            if(word1[i-1] == word2[j-1]){
                dp[i][j] = dp[i-1][j-1];
            }
            else {
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j] , dp[i][j-1]))+1;
            }
        }
    }     
    return dp[n][m];
}



int minDistance(string word1, string word2) {
    vector<vector<int>> dp(word1.size()+1, vector<int>(word2.size()+1));
    int n = word1.size();
    int m = word2.size();

    for(int i =1 ; i<=n; i++){
        dp[i][0] = i;
    }
    for(int j = 1; j <=m ; j++){
        dp[0][j] = j;
    }


    for(int i = 1 ; i<= word1.size(); i++){
        for(int j = 1; j <= word2.size(); j++){
            if(word1[i-1] == word2[j-1]){
                dp[i][j] = dp[i-1][j-1];
            }
            else {
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j] , dp[i][j-1]))+1;
            }
        }
    }     
    return dp[n][m];
}

void setZeroes(vector<vector<int>>& matrix) {
    int n = matrix.size();
    int m = matrix[0].size();


    vector<vector<int>> result(n, vector<int>(m, 0));
    int dx[n]; 
    int dy[m];
    for(int i = 0 ; i<n; i++)dx[i] = 0; 
    for(int j = 0 ; j<m; j++)dy[j] = 0;

    for(int i = 0 ; i<n;i++){
        for(int j = 0 ; j<m; j++){
            if(matrix[i][j] == 0){
                // cout<< "Found zero at: "<<i<<" "<<j<<endl;
                dx[i] = 1; 
                dy[j] = 1;
            }
        }
    }

    for(int i = 0 ; i<n; i++){
        for(int j = 0 ; j<m; j++){
            if(dx[i] == 1 || dy[j] == 1){
                result[i][j] = 0;
            }
            else result[i][j] = matrix[i][j];
        }
    }
    matrix = result ;
}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // solve();
    // test setZeroes
    vector<vector<int>> matrix = {
        {1,1,1},
        {1,0,1},
        {1,1,1}
    };
    setZeroes(matrix);

    for(int i = 0 ; i< matrix.size(); i++){
        for(int j = 0 ; j< matrix[0].size(); j++){
            cout<< matrix[i][j]<<" ";
        }
        cout<<endl;
    }





    return 0;

}