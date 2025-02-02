G90 G94 (absolute positioning, feed per min)
G17 (XY plane selection)
G20 (inch)
G28 G91 Z0 (return to home)
G90 (absolute positioning)
M8 (Coolant On)
M7 (air on)
S8000 M3  (spindle RPM, enable spindle)
G54 (work offset)
G0 X0.000 Y0.0000 Z0.000
M6 T1
S8000
F10
G43 H1 Z1
G1 Z-0.100
G0 Z3
G0 Z0.0000 (move to Z start)
G0 X0.0000 Y0.0000 (move to X/Y start)
G1 Z-0.1000 (move to next cutting depth)
G1 Y0.0000 (linear move in Y)
G1 X4.5000 (linear move in X)
G3 X4.5000 Y0.2500 I0 J0.125 (CW move)
G1 Y0.2500 (linear move in Y)
G1 X-0.5000 (linear move in X)
G2 X-0.5000 Y0.5000 I0 J0.125 (CCW move)
G1 Y0.5000 (linear move in Y)
G1 X4.5000 (linear move in X)
G3 X4.5000 Y0.7500 I0 J0.125 (CW move)
G1 Y0.7500 (linear move in Y)
G1 X-0.5000 (linear move in X)
G2 X-0.5000 Y1.0000 I0 J0.125 (CCW move)
G1 Y1.0000 (linear move in Y)
G1 X4.5000 (linear move in X)
G3 X4.5000 Y1.2500 I0 J0.125 (CW move)
G1 Y1.2500 (linear move in Y)
G1 X-0.5000 (linear move in X)
G2 X-0.5000 Y1.5000 I0 J0.125 (CCW move)
G1 Y1.5000 (linear move in Y)
G1 X4.5000 (linear move in X)
G3 X4.5000 Y1.7500 I0 J0.125 (CW move)
G1 Y1.7500 (linear move in Y)
G1 X-0.5000 (linear move in X)
G2 X-0.5000 Y2.0000 I0 J0.125 (CCW move)
G1 Y2.0000 (linear move in Y)
G1 X4.5000 (linear move in X)
G0 Z3.0000
M30
