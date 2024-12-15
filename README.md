# L-System-Python
A program that creates and draws simple two variable L-systems in Python using a combination of Scheme tail recursion and Python turtle graphics.

The script takes a few parameters needed to create an L-system: 
1. An axiom, or starting string
2. The rules each 0 and 1 correspond to; What every variable expands into each recursion
3. How many iterations or recursions it should generate (Since Python's recursive depth isn't very high, you can't go much higher than 4-6 for some of the more complex systems. Increase at your own risk!)
4. The angle for each rotation
5. If the L-system is a special case:
   t: Binary tree. Doesnt have +/- constant support but makes [ and ] turn the cursor a fixed 45 degrees ([ 45 left, ] 45 right)
   p: "Plant" (Named so after a particular plant-shaped L-system using it). The 0 variable no longer draws forward.
If no special case then just hit enter

After these parameters are entered, the shape should begin drawing in real time. The window parameters can be altered in the "draw()" function if you'd like to have a larger/smaller screen space.

This was a fun project to work on! Seeing it all come together in a visual way was very satisfying. If I had more time, I would have created functionality for more variables, and a dedicated "hold" variable, but there was already some limitations within Scheme that made that difficult. Seeing as the aim of this project was to incorporate Scheme and functional programming in general we had to work around what we knew it order to create an interesting result in a timely manner. Despite this, I'm quite happy with the result, and I hope you have fun tinkering around with various combinations!
