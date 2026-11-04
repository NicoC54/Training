"""
EXERCISE 07 - sensor sync              Time limit: 30 min          No AI, no internet

Routine: read twice -> example by hand -> FIRST TEST -> code -> RUN every 3-4 min.
Rule: never paste code without the terminal output.

Context
-------
Two sensors log the same quantity at different times, e.g. altitude from a barometer and
from GNSS. Each log is a list of (t, value), sorted by t, no duplicate t.
To compare them you must evaluate one log at the timestamps of the other.

Part A - interpolate(samples, t)                                       (~12 min)
--------------------------------
Linear interpolation of the log at time t.
  - t exactly equal to a sample time -> that sample's value
  - t between two samples            -> linear interpolation between them
  - t before the first or after the last sample, or empty log -> None (no extrapolation)

    s = [(0, 0.0), (2, 10.0), (4, 10.0)]
    interpolate(s, 1)    -> 5.0
    interpolate(s, 3)    -> 10.0
    interpolate(s, 4)    -> 10.0
    interpolate(s, 5)    -> None

Part B - align(a, b, latency_b=0.0)                                    (~13 min)
-----------------------------------
Sensor b is late: the value it logs at time t was actually measured at t - latency_b.
For each (t, va) in a, find vb = value of b at the SAME physical instant, i.e. interpolate b
at t + latency_b. Skip the points where vb is None.
Return a list of (t, va, vb).

    a = [(0, 0.0), (1, 5.0), (2, 10.0), (3, 12.0)]
    b = [(0.5, 0.0), (1.5, 5.0), (2.5, 10.0)]
    align(a, b, latency_b=0.5) -> [(0, 0.0, 0.0), (1, 5.0, 5.0), (2, 10.0, 10.0)]
    align(a, b)                -> [(1, 5.0, 2.5), (2, 10.0, 7.5)]

Constraints
-----------
  - Tests with `assert` for every example (floats: math.isclose).
  - In a comment at the end:
        * the complexity of your interpolate, and how to make it O(log n) (hint: bisect);
        * at Elistair you synchronised logs from several sources: what goes wrong in an
          estimator if one sensor's latency is ignored?
"""


def interpolate(samples, t):

    if not samples or t < samples[0][0] or t > samples[-1][0]:
                return None

    if len(samples)==1:
                return samples[0][1]

    for i in range(1, len(samples)):

        

        if samples[i][0] == t:
            return samples[i][1]

        

        elif samples[i][0] > t:
            last_mes = samples[i-1][1]
            pente = (samples[i][1] - samples[i-1][1]) /(samples[i][0]-samples[i-1][0])
            delta = t - samples[i-1][0]
            interpolated = last_mes + pente * delta
            return interpolated


def align(a, b, latency_b=0.0):
    b_corrected = []
    for sample in b:
        correct_time = sample[0] - latency_b
        correct_value = sample[1]
        b_corrected.append((correct_time,correct_value))

    result = []

    for i in range(len(a)):
        time_a = a[i][0]
        value_a = a[i][1]
     

        value_b = interpolate(b_corrected, time_a)
        if value_b is not None:
            result.append((time_a, value_a, value_b))

    return result

       
       
        


    



if __name__ == "__main__":
    # TODO: your tests
    pass
