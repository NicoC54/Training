"""
EXERCISE 01 - clean_track          Time limit: 15 min (REDO)          No AI, no internet

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

import math

def clean_track(samples, v_max):

    if len(samples)==0:
        return ([],[])
    
    dictionnaire = {}

    rejected = []
    valid = []

    sorted_samples = sorted(samples, key = lambda item : item[0])

    for sample in sorted_samples :

        timestamp = sample[0]
        x_pos = sample[1]
        y_pos = sample[2]

        if timestamp not in dictionnaire.keys():
            dictionnaire[timestamp] = (x_pos,y_pos)

    list_mes = list(dictionnaire.items())

    start_timestamp = list_mes[0][0]
    start_xpos = list_mes[0][1][0]
    start_ypos = list_mes[0][1][1]

    valid.append((start_timestamp,start_xpos,start_ypos))

    for timestamp,pos in list_mes[1:]:

        delta_time = timestamp - start_timestamp
        speed_x = (pos[0] - start_xpos)/delta_time
        speed_y = (pos[1] - start_ypos)/delta_time

        speed_norm = math.sqrt(speed_x**2 + speed_y**2)

        if speed_norm > v_max:
            rejected.append(timestamp)
            

        else:
            valid.append((timestamp,pos[0],pos[1]))

            #update last timestamp and position measure for new speed calculation
            start_xpos = pos[0]
            start_ypos = pos[1]
            start_timestamp = timestamp

    return valid,rejected








  


if __name__ == "__main__":
    # TODO: your tests
    pass
