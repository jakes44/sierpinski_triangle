# Sierpinski Triangle Generator using "chaos game"

The Sierpinksi triangle is a fractal and set with the shape of an equilateral triangle. It is made by recursively subdividing the triangle into smaller equilateral triangles. 

My naive implementation uses what is called the chaos game. This is done by picking a random point within the triangle, finding the midpoint between that point and a random vertex, and plotting that midpoint. That midpoint is saved as the starting position and the process repeats. 

To clear up some noise, I throw out every 4th point. Not that great, but it helps. 
### Images (There is a video of it in action in the repository)
![Best Pixel](/best_chaos.png)
![Ok Pixel](/lots_of_dots.png)

### What its done with
Implemented in python using matplotlib animations. Good stuff. 

### Wikipedia articles used for reference 
* [Sierpinski Triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle)
* [Chaos Game](https://en.wikipedia.org/wiki/Chaos_game)
* [Barycentric Coordinates](https://en.wikipedia.org/wiki/Barycentric_coordinate_system)
