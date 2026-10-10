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

#pragma once

template <typename T> class ThreadSafeQueue {
public:
    ThreadSafeQueue() = default;
    ~ThreadSafeQueue() = default;

    // TODO: Implémenter push(T element)
    void push (T element){

        {
        std::lock_guard<std::mutex> lock(safe);
        file.push(element);
        }

        m_cond_var.notify_one();
        
    }
    
    // TODO: Implémenter wait_and_pop()

    T wait_and_pop(){

        std::unique_lock<std::mutex> lock(safe);

        m_cond_var.wait(lock, [this](){return !file.empty();});
    
        T value = file.front();
        file.pop();

        return value;
        }

    // TODO: Implémenter empty()

    bool empty() const {
        {
        std::lock_guard<std::mutex> lock(safe);
        return file.empty();
        }
    }

private:
    mutable std::mutex safe;
    std::queue<T> file;
    std::condition_variable m_cond_var;
        // TODO: Déclarer le conteneur sous-jacent et les primitives de synchronisation
};

