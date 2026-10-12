
#include <vector>
#include <memory>

class Sensor {

    public:


        virtual std::vector<double> readData() const = 0;

        virtual ~Sensor() = default;

};


class IMUSensor : public Sensor {

    public:

        IMUSensor() = default;


        std::vector<double> readData() const override {

            return {1.0,2.0,3.0};

        }

};

class GPSSensor : public Sensor {

    public:

        GPSSensor() = default;

        std::vector<double> readData() const override {

            return {48.8,2.3};
    }

};


// 4. Complétez la fonction d'agrégation
std::vector<double> aggregateData(const std::vector<std::unique_ptr<Sensor>>& sensors) {

    std::vector<double> final_data;
    std::vector<double> data_extracted;
    for (const auto& sensor_ptr : sensors){
       data_extracted = sensor_ptr -> readData();
       for (const double& value : data_extracted){
            final_data.push_back(value);
       }
    }
    return final_data;
   
    
}



#ifndef RunTests
int main() {
    std::vector<std::unique_ptr<Sensor>> systemSensors;
    
    // Test basique fourni (ne modifiez pas le main pour la validation)
    systemSensors.push_back(std::make_unique<IMUSensor>());
    systemSensors.push_back(std::make_unique<GPSSensor>());
    
    std::vector<double> result = aggregateData(systemSensors);
    
    std::cout << "Données agrégées : ";
    for(double val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    // Résultat attendu : 1 2 3 48.8 2.3 
    
    return 0;
}
#endif