#include <iostream>
#include <vector>



int premier_paquet_unique(const std::vector<int>& paquets) {

    std::unordered_map<int,int> dict;

    if (paquets.empty()){
        return -1;
    }

    for (int value : paquets){
        if (dict.find(value) != dict.end()){
            dict[value] += 1;
        }
        else{
            dict[value] = 1;
        }

    }

    for (int value : paquets){
        if (dict[value] == 1){
            return value;
        }
    }
    
    return -1; 
}

