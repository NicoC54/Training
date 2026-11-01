"""
EXERCISE 05 - kalman               Time limit: 35 min          No AI, no internet

Routine: read twice -> solve Part A's example by hand (3 steps) -> plan out loud
-> SIMPLE version first -> run every 5 min -> tick every requirement.

Context
-------
A drone hovers. A noisy barometer gives altitude measurements z_k.

Part A - kalman_1d(zs, x0, p0, q, r)          scalar filter, no numpy      (~15 min)
------------------------------------
State: altitude x (constant model: the drone should stay at the same altitude).
For each measurement z in zs:
    PREDICT:  x stays the same,          p = p + q
    UPDATE:   k = p / (p + r)
              x = x + k * (z - x)
              p = (1 - k) * p
Return the list of the estimates x after each update (same length as zs).

    kalman_1d([1, 1, 1], x0=0, p0=1, q=0, r=1)  ->  [0.5, 0.6667, 0.75]   (rounded)

Part B - kalman_cv(zs, dt, q, r)               constant velocity, numpy     (~20 min)
--------------------------------
State X = [position, velocity] (column vector, shape (2, 1)). Only the position is measured.
    F = [[1, dt],        H = [[1, 0]]        Q = q * identity(2)      R = [[r]]
         [0,  1]]
Start: X = [[0], [0]],  P = 10 * identity(2).
For each z:
    PREDICT:  X = F X            P = F P F^T + Q
    UPDATE:   y = z - H X        S = H P H^T + R
              K = P H^T S^-1     X = X + K y          P = (I - K H) P
Return the final X as a tuple (position, velocity) of floats.

    kalman_cv([0, 1, 2, 3, 4, 5], dt=1, q=0, r=0.01)  ->  velocity close to 1 (abs error < 0.05)

Constraints
-----------
  - Tests with `assert`: the two examples (use a tolerance), and for Part A:
    with r very large (1e9) the estimate barely moves from x0.
  - numpy reminders: np.array, A @ B (matrix product), A.T, np.linalg.inv, np.eye(n).
  - In a comment at the end:
        * what q and r represent physically, and what happens if q is too small;
        * why p decreases in Part A when q = 0, and why that is a problem in real flight.

Paste your code AND the terminal output in the chat, with the time taken.
"""
import numpy as np


def kalman_1d(zs, x0, p0, q, r):

    result = []

    

    for i in range(len(zs)):

        #predict

        p0 = p0 + q

        #update

        k = p0*(1/(p0 + r))
        x0 = x0 + k*(zs[i] - x0)
        p0 = (1 - k)*p0

        result.append(x0)

    return result
    

def kalman_cv(zs, dt, q, r):

    X = np.array([[0],[0]])

    F = np.array([[1,dt],[0,1]])

    H = np.array([[1,0]])

    P = np.array([[1e4,0],[0,1e4]])

    Q = q * np.eye(2)

    R = r 

    I = np.eye(2)




    for z in zs:

        #prediction

        X = F@X
        P = F@P@F.T + Q

        #update
        S = (H@P@H.T + R)
        S_inv = np.linalg.inv(S)
        K = P@H.T@S_inv

        X = X + K@(z- H@X)
        P = (I-K@H)@P

    return (X[0,0],X[1,0])

        
    


