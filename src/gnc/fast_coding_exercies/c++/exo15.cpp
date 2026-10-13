std::vector<int> trouver_paire_calibration(const std::vector<int>& releves, int cible){
    std::unordered_map<int,int> dict;

    for (size_t i=0; i<releves.size(); i++){

        int complement = cible - releves[i];
        if (dict.find(complement) != dict.end()){
            return {dict[complement], static_cast<int>(i)};
        }

        dict[releves[i]] = i;

    }
    return {};

}