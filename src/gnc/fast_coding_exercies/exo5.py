class Actuator:
    # 1. Attribut de classe
    total_actuators = 0
    

    def __init__(self, actuator_id, max_power):
        # 2. Implémentez l'initialisation (et n'oubliez pas d'incrémenter l'attribut de classe)
        Actuator.total_actuators +=1
        self.actuator_id = actuator_id
        self.max_power = max_power
        self._current_power = 0


    # 3. Getter et Setter pour current_power (avec @property)
    @property
    def current_power(self):
        return self._current_power

    @current_power.setter
    def current_power(self,value)
    current_power(self,value):
        if not isinstance(value,(float,int)):
            raise ValueError("pas le bon type")
        if ((value < 0) or (value > self.max_power)):
            raise ValueError("Puissance hors limites")
        else:
            self._current_power = value
    

    # 4. Méthode de classe (Factory)
    @classmethod
    def parse_config(cls, config_str):
        array = config_str.split(':')
        identite = array[0]
        max_power = float(array[1])
        actuator = Actuator(identite,max_power)
        return actuator




        


# 5. Implémentez la classe enfant ReactionWheel (héritage + super() + attribut axis)

class ReactionWheel(Actuator):
    def __init__(self, actuator_id, max_power, axis): #je rajoute ce dont j'ai besoin ici dans mon novueau constructeur
        super().__init__(actuator_id, max_power) #je rapelle le constructeur du parent pour les variables qu'il me faut
        self.axis = axis



# 6. Surcharge de __str__ dans ReactionWheel

def __str__(self):
    return (f"[Roue axe {self.axis} ID: RW-{self.actuator_id} | puissance : {self.current_power}/{self.max_power}")


# --- BLOC DE TESTS (Ne pas modifier) ---
if __name__ == "__main__":
    try:
        # Test 1 : Factory et attributs de base
        a1 = Actuator.parse_config("MAIN_THRUST:250.0")
        print(f"Actionneur créé : {a1.actuator_id}, Max Power : {a1.max_power}")
        # Attendu : Actionneur créé : MAIN_THRUST, Max Power : 250.0

        # Test 2 : Héritage et super()
        rw1 = ReactionWheel("RW-X", 100.0, "X")
        print(rw1) 
        # Attendu : [Roue axe X] ID: RW-X | Puissance: 0.0/100.0

        # Test 3 : Attribut de classe global
        print(f"Total actionneurs : {Actuator.total_actuators}")
        # Attendu : Total actionneurs : 2

        # Test 4 : Encapsulation (Setter avec succès)
        rw1.current_power = 45.5
        print(f"Nouvelle puissance : {rw1.current_power}")
        # Attendu : Nouvelle puissance : 45.5

        # Test 5 : Encapsulation (Doit crasher en hors-limites)
        rw1.current_power = 150.0
        print("ÉCHEC : L'exception ValueError n'a pas été levée (Trop grand).")
    except ValueError as e:
        print(f"SUCCÈS : Exception interceptée ({e})")