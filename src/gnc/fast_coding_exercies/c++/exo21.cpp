


void nettoyer_telemetrie(std::vector<int>& paquets){

    int index_ecriture = 0;

    for (int i = 0 ; i < paquets.size(); i++){
        if (paquets[i] != 0){
            paquets[index_ecriture] = paquets[i];
            index_ecriture++;
        }
    }

    for (int i = index_ecriture; i < paquets.size(); i++ ){
        paquets[i] = 0;
    }

    
}
