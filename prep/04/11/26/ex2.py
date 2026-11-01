"""
EXERCISE 02 - flight_phases        Time limit: 20 min          No AI, no internet

Before coding: say your plan out loud in 30 s. Then write the first test.
Save (Ctrl+S) and run (python3 ex02_flight_phases.py) every 5 minutes.

Context
-------
You receive the altitude log of a drone flight:

    log = [(t, alt), ...]      t in seconds, alt in metres (floats)

The log is ALREADY sorted by t, with no duplicate timestamps.

Task
----
Write `flight_phases(log, v_thr)` that cuts the flight into phases.

  1. For each pair of consecutive samples, compute the vertical speed
         vz = (alt_2 - alt_1) / (t_2 - t_1)
     and classify the interval [t_1, t_2]:
         "climb"    if vz >  v_thr
         "descent"  if vz < -v_thr
         "hover"    otherwise
  2. MERGE consecutive intervals that have the same phase into one segment.
  3. Return a list of segments (phase, t_start, t_end), in time order.

Example (v_thr = 0.5)
---------------------
    log = [(0, 0), (1, 2), (2, 4), (3, 4), (4, 4.2), (5, 1)]
    vz per interval:  2, 2, 0, 0.2, -3.2
    result -> [("climb", 0, 2), ("hover", 2, 4), ("descent", 4, 5)]

Constraints
-----------
  - Fewer than 2 samples -> return [] (no interval, so no phase).
  - Add at least 3 tests with `assert` in the `if __name__ == "__main__":` block,
    including the example above and one edge case.
  - In a comment at the end, write:
        * the time complexity of your solution;
        * one real-world problem with this method on a noisy barometer
          and how you would fix it.

When done (or when the 20 min are over): paste your code AND the terminal output
in the chat, and say how long you took.
"""


def flight_phases(log, v_thr):

    last_time = log[0][0]
    last_alt = log[0][1]

    dictionnaire = {}

    result = []

    for sample in log[1:]:
        delta_time = sample[0] - last_time
        speed_z = (sample[1] - last_alt) / delta_time

        if speed_z > v_thr :
            phase = "climb"
            dictionnaire[sample[0]] =  phase #no duplicates

        elif speed_z < -v_thr:
            phase = "descent"
            dictionnaire[sample[0]] =  phase #no duplicates

        else:
            phase = "hover"
            dictionnaire[sample[0]] =  phase #no duplicates = no verification needed

        last_time = sample[0]
        last_alt = sample[1]


    items = list(dictionnaire.items())

    start_timestamp = log[0][0]          # start of the first interval
    end_timestamp, start_phase = items[0]


    for timestamp,phase in items[1:]:

        if phase == start_phase :
            end_timestamp = timestamp

        else:
            result.append((start_phase,start_timestamp,end_timestamp))
            start_timestamp = end_timestamp
            end_timestamp = timestamp  
            start_phase = phase

    result.append((start_phase, start_timestamp, end_timestamp)) 



    return result

        



        


        








if __name__ == "__main__":
    # TODO: your tests
    pass
