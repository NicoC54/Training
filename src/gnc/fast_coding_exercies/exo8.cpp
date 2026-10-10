/* ============================================================================
 * EXERCICE 2 : Pipeline d'acquisition et gestionnaire de capteurs hétérogènes
 * ============================================================================
 *
 * CONTEXTE :
 * Dans un système embarqué de navigation / robotique, le module d'estimation
 * d'état reçoit des données issues d'une suite de capteurs hétérogènes
 * (centrales inertielles, baromètres, GNSS).
 * L'architecture logicielle doit permettre d'enregistrer dynamiquement des
 * capteurs variés et d'interroger l'ensemble de la suite de manière uniforme.
 *
 * CAHIER DES CHARGES :
 *
 * 1. Structure 'Measurement' :
 *    - std::string sensor_name
 *    - double timestamp_sec
 *    - std::vector<double> values
 *
 * 2. Interface 'ISensor' :
 *    - Interface abstraite pure (non instanciable).
 *    - Méthode de lecture : renvoie un 'Measurement' pour un timestamp donné.
 *    - Méthode d'identification : renvoie le nom du capteur sous forme de std::string.
 *    - Destructeur approprié pour une classe de base polymorphique.
 *
 * 3. Capteur IMU ('ImuSensor') :
 *    - Hérite de 'ISensor'.
 *    - Constructeur prenant un nom (std::string) et une fréquence (double, en Hz).
 *    - La méthode de lecture renvoie un Measurement contenant 3 valeurs simulant
 *      une accélération : {0.0, 0.0, 9.81}.
 *
 * 4. Capteur Barométrique ('BarometerSensor') :
 *    - Hérite de 'ISensor'.
 *    - Constructeur prenant un nom (std::string) et une pression au sol (double, en hPa).
 *    - La méthode de lecture renvoie un Measurement contenant 1 valeur scalaire :
 *      {1013.25}.
 *
 * 5. Gestionnaire de capteurs ('SensorManager') :
 *    - 'add_sensor' : enregistre un nouveau capteur en prenant la propriété exclusive
 *      de l'instance via un pointeur intelligent standard.
 *    - 'poll_all' : interroge chaque capteur enregistré au timestamp fourni et
 *      retourne l'ensemble des mesures collectées dans un std::vector<Measurement>.
 *    - 'sensor_count' : retourne le nombre de capteurs actuellement enregistrés.
 *
 * CONTRAINTES :
 * - Gestion mémoire déterministe, zéro fuite.
 * - Utilisation des fonctionnalités modernes de C++ (ownership, override, const-correctness).
 * - C++17 minimum.
 * ============================================================================
 */

#include <cstddef>
#include <memory>
#include <string>
#include <utility>
#include <vector>

// 1. Structure de données
struct Measurement{

     std::string sensor_name;
     double timestamp_sec;
     std::vector<double> values;
};

class ISensor{

    public: 

        virtual Measurement getMeasurement(double timestamp_sec) const  = 0;
           
        virtual std::string getName() const = 0;
    
        virtual ~ISensor() = default;

};


class IMUSensor : public ISensor{

    public :

        IMUSensor(std::string name, double hz) : IMU_name(name), freq(hz){};

        Measurement getMeasurement(double timestamp_sec) const override {

            Measurement accelero;
            accelero.sensor_name = IMU_name;
            accelero.values = {0.0,0.0,9.81};
            accelero.timestamp_sec = timestamp_sec;
            return accelero;
        }

        std::string getName() const override{
            return IMU_name;

        }

    private:

        std::string IMU_name;
        double freq;

};

class BaroSensor : public ISensor{


     public :

        BaroSensor(std::string name, double pres) : baro_name(name), pression(pres){};

        Measurement getMeasurement(double timestamp_sec) const override {

            Measurement baro;
            baro.sensor_name = baro_name;
            baro.values = {1013.25};
            baro.timestamp_sec = timestamp_sec;
            return baro;
        }

        std::string getName( ) const override{

            return baro_name;

        }

    private:

        std::string baro_name;
        double pression;


};

class SensorManager{
    public:
        SensorManager() = default;

    void add_sensor(std::unique_ptr<ISensor> sensor_ptr){
        sensors.push_back(std::move(sensor_ptr));
    }


    
    std::vector<Measurement> poll_all(double timestamp_sec) const{

        std::vector<Measurement> mesures{};

        for (auto& sensor_ptr : sensors){
            Measurement mesure = sensor_ptr->getMeasurement(timestamp_sec);
            mesures.push_back(mesure);
        }
        return mesures;
    }

    size_t sensor_count() const{
        return sensors.size();
    }

    private:
        std::vector<std::unique_ptr<ISensor>> sensors{};

};



