#include <vector>
#include <iostream>
#include <cmath>

std::vector<double> clean_sensor_data(const std::vector<double>& data, double max_diff) {

    if (data.empty()){
        return {};
    }

    double valeur_valide = data[0];
    std::vector<double> data_corrected;
    data_corrected.push_back(data[0]);

    for (int i = 1; i<data.size(); i++){

        if (std::abs(data[i] - valeur_valide) > max_diff){
            data_corrected.push_back(valeur_valide);
        }
        else{
            data_corrected.push_back(data[i]);
            valeur_valide = data[i];
        }
    }
    return data_corrected;
}

// Exemple pour vous tester localement (main non requis pour TestDome, juste pour vous)
int main() {
    std::vector<double> test_data = {10.0, 10.5, 11.0, 50.0, 11.2, 11.5};
    std::vector<double> result = clean_sensor_data(test_data, 2.0);
    // Devrait afficher: 10 10.5 11 11 11.2 11.5
}
