"""
EXERCISE 03 - imu_spikes           Time limit: 30 min          No AI, no internet

Routine: read twice -> solve the example by hand -> plan out loud -> code + run every 5 min -> edge cases.

Context
-------
You receive the vertical acceleration of a drone sampled at a fixed rate:

    signal = [a0, a1, a2, ...]      list of floats

Part A - moving_average(signal, w)                                    (~10 min)
----------------------------------
Return the list of the means of every window of w CONSECUTIVE samples.
Only full windows count, so the result has len(signal) - w + 1 elements.
  - w <= 0 -> raise ValueError
  - len(signal) < w -> return []

    moving_average([1, 2, 3, 4], 2)  ->  [1.5, 2.5, 3.5]

Part B - detect_spikes(signal, w, thr)                                (~15 min)
--------------------------------------
For every index i >= w, compare signal[i] with the mean of the w samples
BEFORE it (signal[i-w] ... signal[i-1]).
If abs(signal[i] - that mean) > thr, index i is a spike.
Return the list of spike indices.

    signal = [1, 1, 1, 1, 10, 1, 1]
    detect_spikes(signal, 3, 3)  ->  [4]

Constraints
-----------
  - At least 3 tests with `assert`, including the two examples and one edge case.
  - Floats: compare with a tolerance, e.g. abs(a - b) < 1e-9, or math.isclose.
  - In a comment at the end:
        * the complexity of Part A as you wrote it, and how to make it O(n)
          if it is not (hint: running sum);
        * in Part B, what goes wrong if TWO spikes follow each other closely,
          and how you would fix it (hint: think about ex01).

Paste your code AND the terminal output in the chat, with the time taken.
"""


def moving_average(signal, w):

    if w <= 0:
             raise ValueError("w must be positive")

    if len(signal) < w:
        return []


    means = []


    start_window_index = 0
    size = 1
    total_sum = signal[0]
    mean_value = total_sum / size

    if size == w:
        means.append(mean_value)
    

    for i in range(1, len(signal)):

        if size < w:
            size+=1
            total_sum += signal[i]
            mean_value = total_sum / size

        else:
            total_sum -= signal[start_window_index]
            total_sum += signal[i]
            start_window_index+=1
            mean_value = total_sum / size


        if size == w:
            means.append(mean_value)

    return means



def detect_spikes(signal, w, thr):

    if len(signal) < w:
        print("signal is not big enough in size comapred to w")
        return []

    if thr <0:
        print("thr is negative")

    spike_index = []

    means = moving_average(signal, w)
    start_means_index = 0

    for i in range(w,len(signal)):

        if abs(signal[i] - means[start_means_index]) > thr:
            spike_index.append(i)

        start_means_index+=1

    return spike_index




 

if __name__ == "__main__":
    import math

    result = moving_average([1,2,3,4],2)
    expected = [1.5,2.5,3.5]
    assert len(result)==len(expected)
    assert all(math.isclose(a, b) for a, b in zip(result, expected)), result

    

    assert moving_average([1,2],3) == []
    assert moving_average([],1) == []
    assert moving_average([5, 6], 1) == [5.0, 6.0]


     # Part A: w <= 0 must raise ValueError
    try:
        moving_average([1, 2], 0)
        assert False, "w = 0 should raise ValueError"
    except ValueError:
        pass

    # Part B: example from the statement
    assert detect_spikes([1, 1, 1, 1, 10, 1, 1], 3, 3) == [4]

    # Part B: edge cases
    assert detect_spikes([1, 1], 3, 3) == []               # shorter than the window
    assert detect_spikes([1, 1, 1], 3, 3) == []            # no sample after the first window
    assert detect_spikes([2, 2, 2, 2, 2], 2, 0.5) == []    # flat signal: no spike

    print("all tests pass")

    #comments : on est en complexité O(n) optimale (somme glissante), car 10 et 10 font partie de la nouvelle moyenne mobile : donc lecart entre la moyenen mobile et la valeur normale est enorme.
    #rajouter une condition : si la mesure est aberrante lignorer dans le calcul de moyenne

