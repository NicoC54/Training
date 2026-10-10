#pragma once

#include <array>
#include <cstddef>
#include <optional>
#include <stdexcept>
#include <utility>

template <typename T, std::size_t Capacity>
class CircularBuffer {
    static_assert(Capacity > 0, "Capacity must be greater than zero.");

public:
    // Constructeur default car on a initialisé nos variables dans le private avec valeurs
    CircularBuffer() = default;

    // Insertion
    void push(const T& item) {
        array[head] = item; // on copie intégralement item dans array[head]
        advance_head();
    }

    void push(T&& item) {
        array[head] = std::move(item); // utile si on a un item lourd : on déplace juste item sans copie = couper - coller
        advance_head();
    }

    // Extraction (FIFO)
    std::optional<T> pop() {
        // si on fait un pop avec un array vide = erreur
        if (empty()) {
            return std::nullopt; // on retourne un paquet vide
        } else {
            // on fait un couper coller = plus rapide; on considere que array[tail] nest plus traité par notre tableau et la prochaine fois qu'il sera traité on va le remplacer
            T item = std::move(array[tail]);
            // incremente tail car on vient de recup la valeur la plus ancienne
            tail = (tail + 1) % Capacity;
            m_size--;
            return item;
        }
    }

    // Consultation du dernier élément inséré
    const T& latest() const {
        if (empty()) {
            // on renvoie une exception error
            throw std::underflow_error("erreur : aucune valeur dans le buffer");
        }
        // le dernier element ajouté et head -1 sauf lorsque head vaut 0 et est egal a capacity-1
        size_t last_index = (head == 0) ? (Capacity - 1) : (head - 1);

        return array[last_index];
    }

    // Méthodes d'état
    std::size_t size() const noexcept {
        return m_size;
    }

    bool empty() const noexcept {
        return m_size == 0;
    }

    bool full() const noexcept {
        return m_size == Capacity;
    }

    void clear() noexcept {
        m_size = 0;
        head = 0;
        tail = 0;
    }

private:
    size_t tail{0};
    size_t head{0};
    size_t m_size{0};
    std::array<T, Capacity> array{};

    // après un push on fait un advance head : cette methode remet à jour l'index des itérateurs : head et tail (head+1%cap et tail+1%cap ssi on a array qui est full)
    void advance_head() noexcept {
        head = (head + 1) % Capacity; // modulo capacity, complexité O(1), donne toujours le prochain index du tableau à modifier
        
        // si le tableau est deja rempli on avance le tail
        if (full()) {
            tail = (tail + 1) % Capacity;
        }
        // si le tableau n'est pas deja rempli :
        else { 
            m_size++;
        }
    }
};