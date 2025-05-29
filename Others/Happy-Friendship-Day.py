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
