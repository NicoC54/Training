/**
 * ============================================================================
 * EXERCICE 5 : Le Décodeur de Trame Binaire (Parsing UART)
 * ============================================================================
 *
 * OBJECTIF :
 * Écrire une fonction capable d'analyser un buffer d'octets bruts provenant
 * d'une liaison série matérielle (UART), d'y détecter un message valide et
 * de le convertir en une structure C++ propre et fortement typée.
 *
 * SPÉCIFICATIONS DU PROTOCOLE :
 * Les trames reçues font exactement 8 octets (ordonnancement Little-Endian) :
 *   - Octet 0   : Header 1 (toujours 0xAA)
 *   - Octet 1   : Header 2 (toujours 0x55)
 *   - Octets 2-3: ID du capteur (entier non signé 16 bits, uint16_t)
 *   - Octets 4-7: Mesure de température (flottant 32 bits IEEE 754, float)
 *
 * ATTENDUS :
 * 1. Définir la structure `TemperaturePacket` contenant l'ID et la température.
 * 2. Implémenter `decode_frame(...)` retournant `std::optional<TemperaturePacket>`.
 * 3. Valider rigoureusement :
 *      - La taille du buffer (doit être exactement de 8 octets).
 *      - La présence des octets magiques (Header 1 = 0xAA, Header 2 = 0x55).
 *      - La non-nullité du buffer source.
 * 4. Contrainte stricte de typage & alignement :
 *      - NE PAS faire de `reinterpret_cast<float*>` sur le buffer brut (cela
 *        violerait la règle de strict aliasing et poserait des risques
 *        d'Undefined Behavior liés à l'alignement mémoire).
 *      - Privilégier `std::memcpy` ou `std::bit_cast` (C++20).
 *
 * COMPILATION :
 *   g++ -std=c++17 -Wall -Wextra -Werror exercice5_decodeur_uart.cpp -o decodeur
 * ============================================================================
 */

#include <iostream>
#include <vector>
#include <cstdint>
#include <optional>
#include <cstring>
#include <cassert>
#include <cmath>

// ============================================================================
// 1. STRUCTURE DE SORTIE
// ============================================================================
struct TemperaturePacket {
    uint16_t sensor_id;
    float    temperature;
};

// ============================================================================
// 2. FONCTION DE DÉCODAGE (À IMPLÉMENTER)
// ============================================================================
/**
 * @brief Décode une trame UART binaire de 8 octets.
 * 
 * @param buffer Pointeur vers le premier octet de la trame reçue
 * @param size   Nombre d'octets reçus dans le buffer
 * @return std::optional<TemperaturePacket> Le paquet décodé si valide,
 *                                          std::nullopt sinon.
 */
std::optional<TemperaturePacket> decode_frame(const uint8_t* buffer, size_t size) {
    // ÉTAPE 1 : Vérifier la validité du buffer et sa taille (exactement 8 octets)
    // TODO: ...
    if ( (buffer==nullptr) ||(size !=8) ){
        return std::nullopt;
    }

    // ÉTAPE 2 : Valider les octets de synchronisation (0xAA et 0x55)
    // TODO: ...

    if ((buffer[0]!=0xAA) || (buffer[1]!=0x55)){
       return std::nullopt;

    }

    // ÉTAPE 3 : Extraire l'ID du capteur (uint16_t, Little-Endian)
    // Astuce : Reconstitution par décalage de bits ou copie mémoire sûre :
    uint16_t id = (static_cast<uint16_t>(buffer[2])) | (static_cast<uint16_t>(buffer[3]) << 8);
    // TODO: ...

    // ÉTAPE 4 : Extraire la température (float 32 bits, IEEE 754 Little-Endian)
    // Attention : utiliser std::memcpy(&temp, &buffer[4], sizeof(float))
    //             afin d'éviter tout Undefined Behavior lié à l'alignement.

    uint32_t data = ((static_cast<uint32_t>(buffer[4]))) | (static_cast<uint32_t>(buffer[5])<<8) | (static_cast<uint32_t>(buffer[6])<<16) |(static_cast<uint32_t>(buffer[7]) << 24);
    float temperature = std::bit_cast<float>(data);
    
    // TODO: ...

    // ÉTAPE 5 : Renvoyer le paquet empaqueté dans un std::optional
    // TODO: return TemperaturePacket{id, temp};
    TemperaturePacket packet;
    packet.sensor_id = id;
    packet.temperature = temperature;

    return packet; // Remplacer par l'implémentation
}

