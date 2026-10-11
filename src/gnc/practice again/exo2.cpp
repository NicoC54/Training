/* ============================================================================
 * EXERCICE 4 : La File Concurrente (Producteur / Consommateur)
 * ============================================================================
 *
 * CONTEXTE :
 * Concevoir une structure de données permettant de faire transiter des messages 
 * entre deux threads différents (un thread qui écrit, un thread qui lit) sans 
 * risquer de corrompre la mémoire (Data Race) et sans gaspiller le CPU.
 *
 * CAHIER DES CHARGES :
 *
 * 1. Généricité : 
 *    La classe doit être un template acceptant n'importe quel type de donnée (T).
 *
 * 2. Ajout (Producteur) : 
 *    - void push(T element)
 *    Permet à un thread d'ajouter une donnée de manière sécurisée en fin de file.
 *
 * 3. Extraction bloquante (Consommateur) : 
 *    - T wait_and_pop()
 *    Permet à un autre thread de récupérer et retirer la donnée la plus ancienne.
 *    CONTRAINTE : Si la file est vide, le thread appelant doit être "endormi" 
 *    par l'OS (pas de boucle infinie type "while(empty) {}"). Il doit être 
 *    réveillé instantanément dès qu'un push() est effectué.
 *
 * 4. État : 
 *    - bool empty() const
 *    Permet de savoir si la file est vide à un instant T (doit aussi être thread-safe).
 *
 * CONTRAINTES :
 * - Sécurité totale : Data Race impossible.
 * - Efficacité CPU : Zéro busy-waiting.
 * ============================================================================
 */

 template <typename T> class Communicator{

    public:

        Communicator(){};

        void push(T element){

            {
            std::lock_guard<std::mutex> lock(safe);
            q.push(element);
            }

            cond.notify_one();
        }

        T wait_and_pop(){

            std::unique_lock<std::mutex> lock(safe);

            cond.wait(lock, [this](){return !(q.empty());});

            T element = q.front();
            q.pop();


            return element;
        }

        bool empty() const {
            std::lock_guard<std::mutex> lock(safe);
            return q.empty();

        }

    private:

        mutable std::mutex safe;
        std::condition_variable cond;
        std::queue<T> q;

 };
