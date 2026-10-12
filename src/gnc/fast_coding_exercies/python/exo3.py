class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        # L'appel à self.x, self.y, self.z passe par les setters automatiquement !
        self.x = x
        self.y = y
        self.z = z

    # 1. Implémentez la property 'x' et son setter (avec validation)
    # Répétez le principe pour y et z (tu peux te contenter de faire x pour l'exercice si tu as compris le principe)
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        if not isinstance(value,(float,int)):
            raise ValueError("pas un float ou un int")

        else:
            self._x = value
    


    
    # 2. Surcharge de l'opérateur d'addition (+)
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        
    # 3. Surcharge de l'opérateur de multiplication par un scalaire (*)
    def __mul__(self, scalar):
         return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    # 4. Surcharge de l'opérateur d'égalité (==)
    def __eq__(self, other):
        if ((self.x == other.x) and (self.y == other.y) and (self.z == other.z)):
            return True

        else:
            return False

    # 5. Représentations
    def __str__(self):
        return(f" Vector3D(x={self.x},y={self.y},z={self.z})")
        

    def __repr__(self):
        return(f"Vector3D({self.x},{self.y},{self.z})")
        


# --- BLOC DE TESTS (Ne pas modifier) ---
if __name__ == "__main__":
    v1 = Vector3D(1.0, 2.0, 3.0)
    v2 = Vector3D(4.0, 5.0, 6.0)
    
    # Test Addition
    v3 = v1 + v2
    print(f"Addition : {v3}") # Attendu : Vector3D(x=5.0, y=7.0, z=9.0)
    
    # Test Multiplication
    v4 = v1 * 2
    print(f"Multiplication : {repr(v4)}") # Attendu : Vector3D(2.0, 4.0, 6.0)
    
    # Test Égalité
    v5 = Vector3D(1.0, 2.0, 3.0)
    print(f"Égalité : {v1 == v5}") # Attendu : True
    
    # Test Validation (doit crasher avec une ValueError)
    try:
        v1.x = "Test"
        print("ÉCHEC: La validation n'a pas marché.")
    except ValueError as e:
        print(f"SUCCÈS: Exception interceptée ({e})")