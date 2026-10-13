#include <vector>

int trouver_equilibre(const std::vector<int>& releves) {

    long long somme_totale = 0;
    long long equilibre_gauche=0;

    if (releves.empty()){
        return -1;
    }

    for (int value : releves){
        somme_totale += value;
    }

    for (int i=0; i<releves.size(); i++){
        
        if (equilibre_gauche == somme_totale - equilibre_gauche - releves[i]){
            return i;
        }
        else{
            equilibre_gauche += releves[i];
        }
        
      
    }

    return -1;
  
}