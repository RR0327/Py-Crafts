print('\n'.join
      ([''.join
        ([('Friendshp'[(x-y)%8]
           if((x*0.05)**2+(y*0.1)**2-1)
           **3-(x*0.05)**2*(y*0.1)
           **3<=0 else' ')
           for x in range(-30,30)])
           for y in range (15,-15,-1)]))
print("Happy Friendship Day!")
# Output: A heart shape with the word "Friendshp" inside it, followed by a message "Happy Friendship Day!"
# ✅ Short Explanation of the Code
"""
The original code uses math to draw a heart-shaped curve in the terminal. It:

• Loops over a grid of (x, y) values.
• Uses a heart formula:
  ((x ⋅ 0.05)^2 + (y ⋅ 0.1)^2 - 1)^3 - (x ⋅ 0.05)^2 ⋅ (y ⋅ 0.1)^3 ≤ 0
• If a point falls inside the heart, it picks a letter from "Friendshp" using (x - y) % 8.
• If it's outside, it prints a space.
Then it prints "Happy Friendship Day!" after the heart.
"""

