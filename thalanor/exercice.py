test_intervals = [[0,30], [15,30], [30,60]]

def count_room(intervals):

    if intervals is None:
         return 0

    sorted_intervals = sorted(intervals, key = lambda k : k[0])

    counter_rooms = 0

    for i in range(len(sorted_intervals)):

        if i == 0:

            starting_time = sorted_intervals[i][0]
            ending_time = sorted_intervals[i][1]

            last_ending_time = ending_time


        if i >= 1 :

            starting_time = sorted_intervals[i][0]
            ending_time = sorted_intervals[i][1]

            if ending_time > last_ending_time:
                    last_ending_time = ending_time

            if starting_time < last_ending_time:
                counter_rooms+=1

        last_ending_time = ending_time

    return counter_rooms


print(count_room(test_intervals))

        

        

               

               
        