/* ============================================================================
 * EXERCICE 4 : Implémentation d'un Buffer Circulaire Générique (Ring Buffer)
 * ============================================================================
 *
 * CONTEXTE :
 * Dans les systèmes temps réel (audio, réseaux, acquisition de données), 
 * il est fréquent de recevoir des flux continus de données. Un "buffer circulaire" 
 * (ou ring buffer) permet de stocker ces données dans une structure de taille 
 * fixe, en écrasant les données les plus anciennes si nécessaire, sans jamais 
 * avoir besoin de réallouer de la mémoire (FIFO).
 *
 * CAHIER DES CHARGES :
 *
 * 1. Classe template 'CircularBuffer<T>' :
 *    - La classe doit être générique pour accepter n'importe quel type de donnée (T).
 *
 * 2. Constructeur :
 *    - Prend en paramètre la capacité maximale (size_t) du buffer.
 *    - Le stockage interne doit être géré par un std::vector<T> dont la taille
 *      est fixée une seule fois à l'initialisation.
 *
 * 3. Méthode 'push' :
 *    - Prend un élément de type T en paramètre.
 *    - Ajoute l'élément dans le buffer. 
 *    - Si le buffer est PLEIN, la méthode doit lever une exception de type 
 *      'std::overflow_error' (incluse dans <stdexcept>).
 *
 * 4. Méthode 'pop' :
 *    - Retire et retourne l'élément le plus ancien du buffer.
 *    - Si le buffer est VIDE, la méthode doit lever une exception de type
 *      'std::underflow_error'.
 *
 * 5. Méthodes d'inspection :
 *    - 'is_empty()' : retourne true si le buffer ne contient aucun élément.
 *    - 'is_full()' : retourne true si le buffer a atteint sa capacité maximale.
 *    - 'size()' : retourne le nombre d'éléments actuellement stockés.
 *    - 'capacity()' : retourne la capacité maximale du buffer.
 *
 * CONTRAINTES :
 * - Les opérations 'push' et 'pop' doivent s'exécuter en temps constant O(1).
 *   (Indice : il faut utiliser des indices de lecture et d'écriture qui "tournent").
 * - Const-correctness stricte.
 * - Le code doit être implémenté entièrement dans le fichier d'en-tête (typique des templates).
 * - C++17 minimum.
 * ============================================================================
 */


//idée de l'exo : si on travaille avec un array, pop et insérer une donnée ne cessite des boucles for en O(n) : trop long : une utilise une astuce de génie index d'écriture et de lecture

 template <typename T, size_t Capacity> class CircularBuffer{

    public:


        CircularBuffer() = default;

    //par copie
    void push (const T& element){

        if (full()){
            throw std::overflow_error("buffer plein");
        }
        else{
            m_array[m_head] = element;
        }
        

    }
    //par déplacement
    void push (T&& element){
        if (full()){
            throw std::overflow_error("buffer plein");
        }
        else{
            m_array[m_head] = std::move(element);
            advance_head();

        }
    }

    T pop(){
        if (empty()){
            throw std::underflow_error("buffer vide");
        }
        else{

            T last_value = m_array[m_tail];
            m_tail = (m_tail + 1) % Capacity;
            m_size --;
            return last_value;
            
        }
    }

        bool empty(){
            return m_size == 0;

        }

      bool full(){
          return m_size == Capacity;

     }


     size_t size(){
        return m_size;
  
    }
     size_t capacity(){
        return Capacity;
     }
 
    private:

        std::array<T,Capacity> m_array{};
        size_t m_tail{0};
        size_t m_head{0};
        size_t m_size{0};


        void advance_head(){

            m_head = (m_head+1)%Capacity; // on fait une boucle avec modulo : dès que l'index arrive en bout de tableau il revient à l'index 0

            if (m_size == Capacity){
                m_tail = (m_tail +1) % Capacity;
            }

            else{
                m_size++;
            }
        }


 };