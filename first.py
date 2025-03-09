import pyjokes

print("hello world")
jokes = pyjokes.get_joke()
print(jokes)

# Question-1: printing a poem...

print('''Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark,
Lights the traveller in the dark.
Though I know not what you are,
Twinkle, twinkle, little star.

Twinkle, twinkle, little star.
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star.
How I wonder what you are.
How I wonder what you are.''')

# Question-2: using REPL in terminal and Printing 5's table

# Question-3: insall an external module and perform an operation

import pyttsx3
engine = pyttsx3.init()
engine.say("Good to go chief...!")
engine.runAndWait()

# Question-4: 

import os

# Specify the path to the directory
directory_path = 'D:\java programs'  

# Get the list of files and folders in the directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
