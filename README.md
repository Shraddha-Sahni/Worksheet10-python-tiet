# Worksheet10-python-tiet
Lab assignment 9 for python

Q1. Write a Python script to create a Tkinter window titled "Robot Control Panel" of size 500×400 with a yellow background.

Q2. Using Tkinter Canvas, draw a black point at coordinates (100,100). (Hint: use create_oval)

Q3. Plot the following robot path on a Tkinter Canvas using a polyline:
[(20,50), (100,120), (180,90), (250,150)] Use a blue line with width 3.

Q4. Write a Tkinter program that moves a point from left to right across the window using a loop (after() function).

Q5. Draw a simple robot on Tkinter Canvas using geometric shapes:
- Rectangle -> body
- Two circles -> wheels

Q6. Create a Tkinter window with:
- A Canvas
- A small circle (robot)
- Buttons: Up / Down / Left / Right
When clicked, the robot moves 10 pixels in that direction.

Q7. Simulate a bouncing ball in Tkinter:
- Start at (200,150)
- Radius = 15
- Move diagonally
- Bounce when hitting boundaries
(Hint: reverse velocity on collision)

Q8. Simulate a robot moving along a straight line:
- Initial position: (50,200)
- Target: (450,200)
- Constant velocity
- Update position using after()
Show the robot as a filled circle.

Q9. Draw the following Four-Bar Mechanism statically using Tkinter:
- Ground Link (A-D): 250 px
- Crank L2 = 120 px
- Coupler L3 = 150 px
- Rocker LA = 130 px
Given angle θ = 30°, compute and draw joints:
- A(150,300)
- B (end of crank)
- C (via circle intersection)
- D(400,300)
Draw all links with different colors.

Q10. Write a Tkinter program where:
- A robot (circle) is drawn on a Canvas
- User can press arrow keys
- Robot moves 5 pixels per key press
- Path is drawn behind robot
- Add a "RESET" button to clear the path
