class TimeMap {
public:
    unordered_map<string,vector<pair<string,int>>> my_map;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        my_map[key].push_back({value,timestamp});
    }
    
    string get(string key, int timestamp) {
        if (my_map.find(key) == my_map.end()) {
            return "";
        }
        int left=0, right=my_map[key].size()-1;
        
        while(left<=right){
            int mid = left+(right-left)/2;
            if(timestamp==my_map[key][mid].second){
                return my_map[key][mid].first;
            }
            else if(timestamp>my_map[key][mid].second){
                left = mid+1;
            }
            else{
                right = mid-1;
            }
        }
        if (right >= 0) {
            return my_map[key][right].first;
        }
        return "";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */