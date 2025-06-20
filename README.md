Translating written language in gcode.

Syntax of input file:
- do moving operations: "move"
  - "linear": move linear towards given coordinate
    - total: "move linear ..."
  - "home": do homing
    - total: "move home"
  - "not": wait
    - total: "move not ... millisecond" 
  - not implemented yet:
    - "clockwise":
    - "counterclockwise":    
- set settings: "set"
