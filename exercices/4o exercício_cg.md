**Conceptual Understanding**

Explain why it is necessary to use `glTranslatef(0, 0, -5)` after setting
the projection with `gluPerspective`.

If we remove `gluPerspective`, what happens to the visualization?
Explain the mathematical reason.

What does each vertex below represent in 3D space?

`glVertex3f(0, 1, 0)`

`glVertex3f(-1, -1, 0)`

`glVertex3f(1, -1, 0)`

Draw the Cartesian plane on paper and mark the points.

**Applied Mathematics**

Determine whether the triangle is defined clockwise or counterclockwise.

Hint: use the cross product.

What is the area of the triangle formed by these three points?

**Color Interpolation**

Explain why the interior of the triangle is not divided into three solid
colors.

If all the vertices have the same color, what happens? Justify based on
linear interpolation.

**Code Modification**

Modify the code.

Explain what the graphics pipeline is.

**Extra Challenge (for advanced students)**

Create a second triangle shifted along the X axis.
