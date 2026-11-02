def flight_phases(log, v_thr):
    if len(log) < 2:
        return []

    segments = []
    current_phase = None
    start_time = None
    end_time = None

    for i in range(1, len(log)):
        t1, alt1 = log[i - 1]
        t2, alt2 = log[i]
        vz = (alt2 - alt1) / (t2 - t1)

        if vz > v_thr:
            phase = "climb"
        elif vz < -v_thr:
            phase = "descent"
        else:
            phase = "hover"

        if phase == current_phase:
            end_time = t2                                               # same phase: extend
        else:
            if current_phase is not None:
                segments.append((current_phase, start_time, end_time))  # close the OLD one
            current_phase = phase                                       # open the new one
            start_time = t1
            end_time = t2

    segments.append((current_phase, start_time, end_time))              # ALWAYS close the last one
    return segments
