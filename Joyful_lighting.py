# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:33:33 2024

@author: Morteza
"""

import cv2
import numpy as np
import random
import time
import ctypes

# Get the monitor resolution
user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Create a video writer
out = cv2.VideoWriter('joyful_lights.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

# Countdown function
def countdown(image):
    for i in range(5, -1, -1):
        # Render text on the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 8
        font_thickness = 15
        text = str(i) if i > 0 else "Go!"
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        text_x = (width - text_size[0]) // 2
        text_y = (height + text_size[1]) // 2
        text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)
        
        # Show the image
        cv2.imshow('Joyful Lights', image)
        
        # Write the frame to the video writer
        out.write(image)
        
        # Wait for 1 second
        time.sleep(1)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Function to create colorful joyful lights
def create_joyful_lights(image):
    num_lights = 500
    light_radius = 20
    light_state = [random.choice([True, False]) for _ in range(num_lights)]
    duration = 60  # 60 seconds
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(num_lights):
            light_x = random.randint(0, width - 1)
            light_y = random.randint(0, height - 1)
            if light_state[i]:
                light_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            else:
                light_color = (0, 0, 0)
            cv2.circle(image, (light_x, light_y), light_radius, light_color, -1)
        cv2.imshow('Joyful Lights', image)
        out.write(image)
        cv2.waitKey(200)
        light_state = [not state if random.random() < 0.2 else state for state in light_state]
        image.fill(0)

# Create a black image
image = np.zeros((height, width, 3), dtype=np.uint8)

# Countdown
countdown(image)

# Generate joyful lights
create_joyful_lights(image)

# Release the video writer and close the OpenCV window
out.release()
cv2.destroyAllWindows()
