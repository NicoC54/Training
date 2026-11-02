def flight_phases(log, v_thr):

    if len(log) < 2:
        return []


    segments = []

    current_phase = None
    start_timestamp = None
    end_timestamp = None

    for i in range(1,len(log)):

        t1,z1 = log[i-1]
        t2,z2 = log[i]

        delta_time = t2 - t1
        delta_pos = z2 - z1
        speed_vz = delta_pos / delta_time

        if speed_vz > v_thr:
            phase = "climb"

        elif speed_vz < -v_thr:
            phase = "descending"

        else:
            phase = "hover"

        if (phase == current_phase):
            end_timestamp = t2

        else:
            if current_phase is not None:
                segments.append((current_phase, start_timestamp, end_timestamp))
            start_timestamp = t1
            end_timestamp = t2
            current_phase = phase

    segments.append((current_phase, start_timestamp, end_timestamp))

        


   
    return segments
