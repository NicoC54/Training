"""
EXERCISE 06 - Track (a Python class)    Time limit: 30 min          No AI, no internet

Routine: read twice -> plan out loud -> write the FIRST TEST -> code -> RUN every 3-4 min.
Rule: never paste code without the terminal output.

Context
-------
A ground radar tracks an incoming drone. You write a small class that stores the radar
measurements of ONE target and predicts where it will be, assuming constant velocity
(useful to compensate radar latency: the measurement at time t is used to aim at t + delay).

Write a class `Track` with:

  __init__(self, max_age)
      max_age: seconds after the last measurement beyond which the track is "stale".
      The track starts with no measurement.

  update(self, t, x, y) -> bool
      Add a radar measurement (t in s, x and y in m).
      If t is NOT strictly greater than the last stored time (out of order or duplicate),
      ignore it and return False. Otherwise store it and return True.

  velocity(self) -> (vx, vy) or None
      Velocity from the LAST TWO stored measurements. None if fewer than 2 measurements.

  predict(self, t) -> (x, y) or None
      Predicted position at time t:
        - no measurement      -> None
        - one measurement     -> that position (no velocity known yet)
        - two or more         -> last position + velocity * (t - last time)

  is_stale(self, t) -> bool
      True if there is no measurement, or if t - last time > max_age.

Example
-------
    tr = Track(max_age=1.0)
    tr.predict(0)            -> None
    tr.update(0.0, 0, 0)     -> True
    tr.predict(5)            -> (0, 0)
    tr.update(1.0, 10, 5)    -> True
    tr.update(0.5, 99, 99)   -> False        (out of order, ignored)
    tr.velocity()            -> (10.0, 5.0)
    tr.predict(1.5)          -> (15.0, 7.5)
    tr.is_stale(1.8)         -> False
    tr.is_stale(2.5)         -> True

Constraints
-----------
  - Tests with `assert` for every line of the example (floats: math.isclose).
  - In a comment at the end:
        * why predicting with constant velocity matters when the radar has 100 ms of latency
          and the target flies at 50 m/s (give the error in metres without prediction);
        * one limitation of using only the last two measurements, and a better approach.
"""


class Track:

    def __init__(self,max_age):
       self.max_age = max_age
       self.measurement = []

    def predict(self, t):
          if len(self.measurement) ==0:
              return None
          elif len(self.measurement) == 1:
              return (self.measurement[0][1],self.measurement[0][2])
          else:
              speed_x_y = self.velocity()
              previous_time = self.measurement[-1][0]
              predicted_x = self.measurement[-1][1] + speed_x_y[0] * (t - previous_time)
              predicted_y = self.measurement[-1][2] + speed_x_y[1] * (t - previous_time)

              return (predicted_x, predicted_y)
              

    def update(self, t, x, y):
        if self.measurement and t <= self.measurement[-1][0]:
            return False
        else:
            self.measurement.append((t,x,y))
            return True
           
        


    def velocity(self):
        if len(self.measurement) < 2:
            return None

        last_x = self.measurement[-1][1]
        last_y = self.measurement[-1][2]
        last_time = self.measurement[-1][0]
        
        previous_x = self.measurement[-2][1]
        previous_y = self.measurement[-2][2]
        previous_time = self.measurement[-2][0]
        
        speed_x = (last_x - previous_x) / (last_time-previous_time)
        speed_y = (last_y - previous_y) / (last_time-previous_time)

        return (speed_x,speed_y)
    

    def is_stale(self, t) -> bool :
        if len(self.measurement) == 0 :
            return True

        previous_time = self.measurement[-1][0]
        delta_time = t - previous_time

        if delta_time > self.max_age:
            return True
        else:
            return False


        



if __name__ == "__main__":
    import math
    tr = Track(max_age=1.0)
    assert tr.predict(0) is None
    assert tr.update(0.0, 0, 0) is True
    assert tr.predict(5) == (0, 0)
    assert tr.update(1.0, 10, 5) is True
    assert tr.update(0.5, 99, 99) is False
    assert tr.velocity() == (10.0, 5.0)
    px, py = tr.predict(1.5)
    assert math.isclose(px, 15.0) and math.isclose(py, 7.5)
    assert tr.is_stale(1.8) is False
    assert tr.is_stale(2.5) is True
    print("all tests pass")
