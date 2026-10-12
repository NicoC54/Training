#include <iostream>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <chrono>

class TelemetryBuffer {
private:
    std::queue<double> q;
    std::mutex mtx;
    std::condition_variable cond_not_empty;
    std::condition_variable cond_not_full;
    size_t max_size;

public:
    // Constructeur définissant la taille maximale du buffer
    TelemetryBuffer(size_t size) : max_size(size) {}

    // 1. Implémentez la méthode push (Producteur)
    void push(double data) {
        std::unique_lock<std::mutex> lock(mtx);
        
        cond_not_full.wait(lock, [this](){return q.size()<max_size;});
        q.push(data);
        cond_not_empty.notify_one();



        // Votre code ici (Verrouiller, Attendre si plein, Ajouter, Notifier)
        
    }

    // 2. Implémentez la méthode pop (Consommateur)
    double pop() {
        std::unique_lock<std::mutex> lock(mtx);

        cond_not_empty.wait(lock, [this](){return q.size()>0;});
        double data = q.front();
        q.pop();
        cond_not_full.notify_one();
        return data;

        // Votre code ici (Verrouiller, Attendre si vide, Retirer, Notifier, Retourner)
        
    }
};

#ifndef RunTests
int main() {
    TelemetryBuffer buffer(3); // Buffer max de 3 éléments

    // Le producteur ajoute 5 éléments rapidement
    std::thread producer([&buffer]() {
        for (int i = 1; i <= 5; ++i) {
            double data = i * 10.5;
            buffer.push(data);
            std::cout << "Produit : " << data << std::endl;
        }
    });

    // Le consommateur lit 5 éléments lentement
    std::thread consumer([&buffer]() {
        for (int i = 1; i <= 5; ++i) {
            std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Simule un calcul GNC
            double data = buffer.pop();
            std::cout << "Consommé : " << data << std::endl;
        }
    });

    producer.join();
    consumer.join();
    
    return 0;
}
#endif