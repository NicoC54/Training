#include <vector>

vector<vector<int>> merge(vector<vector<int>>& intervals) {

    std::vector<std::vector<int> merged;

    if (intervals.empty()){
        return {};
    }
    std::sort(intervals.begin(),intervals.end());

    merged.push_back(intervals[0]);

    for (int i = 1 ; i <intervals.size(); i++){

        if (intervals[i][0] <= merged.back()[1]){
            if (merged.back()[1]<intervals[i][1]){
                merged.back()[1] = intervals[i][1];
            }
        }
        else{
            merged.push_back(intervals[i]);
        }
    }
    return merged;

}