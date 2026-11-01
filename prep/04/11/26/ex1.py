"""
EXERCISE 01 - clean_track          Time limit: 25 min          No AI, no internet

Context
-------
You receive raw position measurements of a drone from a log:

    samples = [(t, x, y), ...]      t in seconds, x and y in metres (floats)

The log is messy:
  - samples may arrive OUT OF ORDER (not sorted by t);
  - some samples share the SAME TIMESTAMP (duplicates);
  - some samples are OUTLIERS (GPS jumps).

Task
----
Write `clean_track(samples, v_max)` that:

  1. Sorts the samples by time and removes duplicate timestamps
     (choose and justify a rule: keep the first one? average them? ...).
  2. Walks through the sorted samples and computes the speed (norm, m/s)
     between each sample and the LAST VALID sample.
  3. Rejects a sample as an outlier if that speed is greater than v_max.
     A rejected sample is NOT used as the reference for the next ones.
  4. Returns a tuple (valid, rejected):
        valid    -> list of (t, x, y) kept, sorted by time
        rejected -> list of the timestamps t that were rejected

Constraints
-----------
  - The first sample (after sorting) is assumed valid.
  - Handle edge cases: empty list, a single sample.
  - Add at least 3 tests with `assert` in the `if __name__ == "__main__":` block.
  - In a comment at the end, write:
        * the time complexity of your solution;
        * one weakness of the "first sample is valid" assumption
          and how you would fix it with more time.

When done (or when the 25 min are over): paste your code in the chat,
even if it is incomplete, and say how long you took.
"""


import numpy as np

def clean_track(samples, v_max):

    #keep the first sampel for a timestamp

    if not samples:
        return [],[]

    dictionnaire = {}
    rejected=[]
 
    sorted_samples = sorted(samples, key=lambda item : item[0])

    for sample in sorted_samples:
        if sample[0] not in dictionnaire:
            dictionnaire[sample[0]] = (sample[1], sample[2])


      # NEW: the first sample is the starting reference (assumed valid)
    first = sorted_samples[0]
    valid = [first]
    last_timestamp = first[0]
    last_x = first[1]
    last_y = first[2]


    for key,value in dictionnaire.items():

        delta_time = key - last_timestamp

        
        if (delta_time) !=0:


            speed_x = (value[0] - last_x)/delta_time
            speed_y = (value[1] - last_y)/delta_time

            norm = np.sqrt(speed_x**2 + speed_y**2)
            if norm > v_max:
                rejected.append(key)

            else:
                valid.append((key,value[0],value[1]))
                last_timestamp = key
                last_x = value[0]
                last_y = value[1]
            

        



    return (valid,rejected)

        


#O(n)log(n) : sorting thats cost the much, for the rest; complexity one loop for working with a dictionnary, not index searching. another loop for dictionnary 
#for the assuming first timestamp is valid : maybe best would be to average the x and y values on same timestamp : problem is also that is this measurement is aberrant hten it doesnt work



if __name__ == "__main__":

    v, r = clean_track([(0, 0, 0), (1, 1, 0), (2, 100, 0), (3, 2, 0)], 10)
    print(v, r)
    assert r == [2] and v == [(0, 0, 0), (1, 1, 0), (3, 2, 0)]
    assert clean_track([], 10) == ([], [])
    print("OK")


    
    pass
