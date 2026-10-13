#include <iostream>
#include <string>
#include <unordered_map>

int premier_signal_unique(const std::string& flux) {

    if (flux.size()==0){
        return -1;
    }

    std::unordered_map<char,int> letter_counter;

    for (char c : flux){
        if (letter_counter.find(c) != letter_counter.end()){
            letter_counter[c]+=1;
        }
        else{
            letter_counter[c]=1;
        }
        
    }

    for (int i = 0; i < flux.size(); i++){
        if (letter_counter[flux[i]]==1){
            return i;
        }
    }

    return -1;

}

// --- BLOC DE TESTS ---
int main() {
    // Test 1 : Unique au milieu
    std::cout << "Test 1 : " << premier_signal_unique("radar") << " (Attendu : 2)" << std::endl;

    // Test 2 : Aucun unique
    std::cout << "Test 2 : " << premier_signal_unique("aabb") << " (Attendu : -1)" << std::endl;

    // Test 3 : Unique au début
    std::cout << "Test 3 : " << premier_signal_unique("algorithme") << " (Attendu : 0)" << std::endl;

    // Test 4 : Edge Case (Chaîne vide)
    std::cout << "Test 4 : " << premier_signal_unique("") << " (Attendu : -1)" << std::endl;

    return 0;
}