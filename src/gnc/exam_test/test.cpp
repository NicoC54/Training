// ==============================================================================
// EXERCISE 1: Algorithm - Target Distance (Contiguous Waypoints)
// ==============================================================================
// Context:
// You are analyzing a pre-planned flight route represented as a vector of integers, 
// where each integer represents the distance between consecutive waypoints.
// You need to determine if there is ANY contiguous sub-path (a sequence of 
// adjacent waypoints) whose total distance equals exactly a given `target_distance`.
//
// Task:
// Write a function `hasTargetSum(route, target_distance)` that returns true 
// if such a contiguous sub-path exists, and false otherwise.
//
// Constraints:
// - The array can contain up to 100,000 positive integers.
// - Your algorithm must be efficient. An O(N^2) solution will fail the performance tests.
//
// Examples:
// - route = {2, 4, 1, 5, 2}, target = 10 -> Returns true (4 + 1 + 5 = 10)
// - route = {1, 2, 3}, target = 4 -> Returns false

#include <vector>

class RouteAnalyzer {
public:
    static bool hasTargetSum(const std::vector<int>& route, int targetDistance) {

        int index_queue = 0;
        int somme = 0;
        
        for (int index_tete = 0; index_tete<route.size() ; index_tete++){

            somme +=route[index_tete];

            if (somme < targetDistance){
                continue;
            }
            else if (somme > targetDistance){
                somme-=route[index_queue];
                index_queue ++;
            }
            if (somme ==targetDistance){
                return true;
            }
        }
        return false;
    }
};

// ==============================================================================
// EXERCISE 2: OOP & Multi-threading - Thread-Safe Telemetry Buffer
// ==============================================================================
// Context:
// You need to implement a `TelemetryBuffer` class that stores the latest altitude 
// readings. This class will be accessed by multiple threads simultaneously 
// (one thread writing data, multiple threads reading data).
//
// Task:
// Implement the `TelemetryBuffer` class with the following requirements:
// 1. `addReading(altitude)`: Adds a new altitude integer to the buffer.
// 2. `getLatest()`: Returns the most recently added altitude. If the buffer 
//    is empty, it should throw a std::logic_error.
// 3. Thread Safety: Ensure that multiple threads can call `addReading` and 
//    `getLatest` simultaneously without data corruption.

#include <vector>
#include <stdexcept>
#include <mutex>

class TelemetryBuffer {
public:
    TelemetryBuffer() {
        // TODO: Initialize if needed
    }

    void addReading(int altitude) {
        // TODO: Implement this function
    }

    int getLatest() const {
        // TODO: Implement this function
        return 0;
    }
    
private:
    // TODO: Add necessary member variables (buffer, mutex, etc.)
};