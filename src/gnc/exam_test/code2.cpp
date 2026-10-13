#include <queue>
#include <string>
#include <mutex>
#include <condition_variable>

class TelemetryQueue {
private:
    std::queue<std::string> queue_;
    std::mutex mutex_;
    std::condition_variable cond_var_;

public:
    // Ajouter un message à la file (appelé par les threads Navigation, Payload, etc.)
    void enqueue(const std::string& message) {
        std::lock_guard<std::mutex> lock(mutex_);
        queue_.push(message);
        cond_var_.notify_one();
        // TODO: Protéger l'accès, ajouter à la file, et prévenir le consommateur
    }

    // Récupérer un message (appelé par le thread Télémétrie)
    // Doit attendre de manière "passive" si la file est vide
    std::string dequeue() {
         std::unique_lock<std::mutex> lock(mutex_);
         cond_var_.wait(lock, [this](){return !(queue_.empty());});
         std::string msg = queue_.front();
         queue_.pop();
        return msg;
    }
};