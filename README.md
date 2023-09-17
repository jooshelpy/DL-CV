# TASK8.3- You Only Look Once

# Task description

Create Object detection model (using YOLOv8 ultralytics framework), that detect Egyptian coins, (There are three classes One pound, Half pound, Quart pound).

# Process description

### Collecting data

This has been done through capturing images for the three coins in all the possible conditions for example when half of the coin is displayed and in a low photon environment. Moreover, some augmentation has been done to increase the dataset

### Cleaning data

Removing bad quality, useless, outliers, very dark environment images. Using different types of filters to get better images

### Labeling data

Using labelImg tool

### Training Modal

Using google colab and yolov8 framework

### Predict step

Using the best version of the model training to predict new images