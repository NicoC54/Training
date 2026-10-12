class SensorData:
    # 1. Déclarez l'attribut de classe ici

    total_sensors = 0
    
    def __init__(self, timestamp, value):
        self.timestamp = int(timestamp)
        self.value = float(value)
        self.sensor_type = "GENERIC"
        total_sensors +=1

    # 3. Implémentez la méthode de classe "Factory"
    @classmethod
    def from_telemetry(cls, telemetry_str):
        parts = telemetry_str.split('-')

        if len(parts) != 3:
            raise ValueError("Format de télémétrie invalide")

        name = parts[0]
        timestamp = parts[1]
        value = parts[2]

        if name == "RADAR":
            radar = RadarData(timestamp,value)
            return radar
        elif name == "LIDAR" telemetry_str:
            lidar = LidarData(timestamp,value)
            return lidar

        else:
            raise ValueError("Type de capteur inconnu")


# 4. Implémentez LidarData (hérite de SensorData)

class LidarData(SensorData):
    def __init__(self,timestamp,value):
    # 1. On appelle le __init__ de SensorData pour initialiser timestamp/value et le compteur
        super().__init__(timestamp, value)
    # 2. On écrase spécifiquement le type pour cette instance
        self.sensor_type = "LIDAR"

# 5. Implémentez RadarData (hérite de SensorData)
class RadarData(SensorData):
    def __init__(self,timestamp,value):
        super().__init__(timestamp,value)
        self.sensor_type = "RADAR"
   


# --- BLOC DE TESTS (Ne pas modifier) ---
if __name__ == "__main__":
    try:
        # Test 1 : Instanciation via le constructeur alternatif
        s1 = SensorData.from_telemetry("LIDAR-1001-12.5")
        s2 = SensorData.from_telemetry("RADAR-1002-99.9")
        
        # Vérification des types
        print(f"s1 est un {type(s1).__name__} (Type interne: {s1.sensor_type})") 
        # Attendu : s1 est un LidarData (Type interne: LIDAR)
        
        print(f"s2 est un {type(s2).__name__} (Type interne: {s2.sensor_type})") 
        # Attendu : s2 est un RadarData (Type interne: RADAR)

        # Test 2 : Attribut de classe
        print(f"Total capteurs créés : {SensorData.total_sensors}") 
        # Attendu : Total capteurs créés : 2

        # Test 3 : Gestion d'erreur
        s3 = SensorData.from_telemetry("CAMERA-1003-0.0")
        print("ÉCHEC : L'exception ValueError n'a pas été levée.")
    except ValueError as e:
        print(f"SUCCÈS : Exception interceptée ({e})")