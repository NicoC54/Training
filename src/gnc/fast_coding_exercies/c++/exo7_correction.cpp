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
    // Constructeur par défaut : pas besoin d'arguments, la capacité est dans le template
    CircularBuffer() = default;

    // Insertion par copie
    void push(const T& item) {
        m_data[m_head] = item;
        advance_head();
    }

    // Insertion par déplacement (move semantics)
    void push(T&& item) {
        m_data[m_head] = std::move(item);
        advance_head();
    }

    // Extraction FIFO : O(1)
    std::optional<T> pop() {
        if (empty()) {
            return std::nullopt;
        }

        T item = std::move(m_data[m_tail]);
        m_tail = (m_tail + 1) % Capacity;
        --m_size;
        return item;
    }

    // Dernier élément inséré
    [[nodiscard]] const T& latest() const {
        if (empty()) {
            throw std::underflow_error("Buffer is empty.");
        }
        // Le dernier élément inséré se trouve juste avant m_head
        std::size_t last_idx = (m_head == 0) ? (Capacity - 1) : (m_head - 1);
        return m_data[last_idx];
    }

    [[nodiscard]] std::size_t size() const noexcept {
        return m_size;
    }

    [[nodiscard]] bool empty() const noexcept {
        return m_size == 0;
    }

    [[nodiscard]] bool full() const noexcept {
        return m_size == Capacity;
    }

    void clear() noexcept {
        m_head = 0;
        m_tail = 0;
        m_size = 0;
    }

private:
    void advance_head() noexcept {
        m_head = (m_head + 1) % Capacity;
        if (m_size == Capacity) {
            // Tampon plein : l'élément le plus ancien est écrasé, la queue avance aussi
            m_tail = (m_tail + 1) % Capacity;
        } else {
            ++m_size;
        }
    }

    std::array<T, Capacity> m_data{};
    std::size_t m_head{0};
    std::size_t m_tail{0};
    std::size_t m_size{0};
};