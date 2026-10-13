def max_requests(timestamps, window_size):
    # Rappel : timestamps est trié chronologiquement.
    # Objectif : O(N) avec une fenêtre glissante.
    
    # Votre code ici
    max_request = 0
    index_queue=0
    request = 0

    for index_tete in range(len(timestamps)):
        
       while (timestamps[index_tete] - timestamps[index_queue] > window_size):
            index_queue +=1

        request = index_tete - index_queue + 1

        if request>request_max:
            request_max = request

    return max_request

      
    
        





    

# Tests locaux
print(max_requests([1, 5, 5, 8, 12, 13, 14, 15], 5)) # Attendu : 4
print(max_requests([], 5))                           # Attendu : 0


