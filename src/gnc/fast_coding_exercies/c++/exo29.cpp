


#include <vector>

class MovingTotal {


private:

        std::deque<int> moyenne_glissante;
        int somme_totale = 0;
        std::unordered_map<int,bool> present;

public:
    void append(const std::vector<int>& list) {

        for (const int& value : list){

        moyenne_glissante.push_back(value);
        somme_totale+= value;

        if (moyenne_glissante.size()>3){
            somme_totale-= moyenne_glissante.front();
            moyenne_glissante.pop_front();
        }
        if (moyenne_glissante.size()==3){
            present[somme_totale]=true;
        }
    }
}

    bool contains(int total) {
        if (present.count(total)){
            return true;
        }
        // Ton code ici
        return false;
    }





};