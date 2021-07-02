"""
File:       images.py
Author:     Sergio Gomez
Project:    07 & 08 Prove: Assignment Milestone
Purpose:    This program takes a selected image with a green background
            and inserts it over another selected image
"""
# Import the library we will need
from PIL import Image

# Set colors styles for text
yellow = chr(27)+'[1;33m'
white = chr(27)+'[0;37m'
green = chr(27)+'[0;32m'
red = chr(27)+'[0;31m'
bold = chr(27)+'[1;37m'
normal = chr(27)+'[0;37m'

# Define a list for the first menu items (images with green background)
green_image_menu = ['Boat', 'Cactus', 'Cat', 'Small Cat', 'Harvester', 'Hiker', 'Penguin', 'Space Shuttle']

# Define a list with the names of the files as they appear in the directory. The order is the same as the list of items in the first menu
green_image_jpg = ['boat.jpg', 'cactus.jpg', 'cat.jpg', 'cat_small.jpg', 'harvester.jpg', 'hiker.jpg', 'penguin.jpg', 'spaceshuttle.jpg']

# Define a list for the second menu items (background images)
backg_image_menu = ['Beach', 'Desert', 'Earth', 'Field', 'Forest', 'Snowscape', 'Sunset']

# Define a list with the names of the files as they appear in the directory. The order is the same as the list of items in the second menu
backg_image_jpg = ['beach.jpg', 'desert.jpg', 'earth.jpg', 'field.jpg', 'forest.jpg', 'snowscape.jpg', 'sunset.jpg']

# Define a list with the options of the menu program
task_options = ['Merge both images', 'Insert the first image over the second by selecting the place', 'Play with colors']

# Define a list with the options of corners
corner_options = ['Top-Left', 'Top-Right', 'Bottom-Left', 'Bottom-Right']

# Define a list of possible colors for the combined image
colors_options = ['Grey', 'More Red', 'More Green', 'More Blue', 'More Yellow']

# ----------------------------------------------------------------------------- intro()
# Displays the welcome screen and instructions.
# Uses bold, normal, yellow and white variables to decorate the text.
def intro():
    print()
    print('        |   ' + bold + 'Instructions' + normal)
    print(yellow + ' Play   ' + white + '|   Select an image with a green background from the menu. Then select')
    print(yellow + ' with   ' + white + '|   a background image where you want to insert the first image.')
    print(yellow + 'Images  ' + white + '|   Finally select the operation.')
    print('        |   Have fun!')

# ----------------------------------------------------------------------------- show_menu_items()
# Displays the items for the first menu that contains the background images.
# Uses green, white, yellow and red variables to decorate the text.
# Receives a string for the title and a list for the items of the menu
def show_menu_items(title, menu_items):
    print()
    print(green + title + white)
    for i in range(len(menu_items)):
        print(yellow + f'{i + 1}' + white + '. ' + menu_items[i])
    print()

# ----------------------------------------------------------------------------- select_menu_item()
# Allows the user to select a menu item. Verify that what is entered is correct. 
# It receives a list of the menu items and returns the response in the user_choise variable.
def select_menu_item(menu_items):
    correct = False
    while not correct:
        user_choise = int(input('Please, enter your choise '))
        if user_choise < 1 or user_choise > len(menu_items):
            print(red + '> Select an option between 1 and ' + str(len(menu_items)) + white)
        else:
            correct = True
    return(user_choise)

# ----------------------------------------------------------------------------- start()
# This is the main function of the program
def start():
    # Show the first menu to select the image with green background
    title = 'Images with Green Background'
    show_menu_items(title, green_image_menu)
    user_image = select_menu_item(green_image_menu)

    # Show the second menu to select the backgroubd image
    title = 'Background Images'
    show_menu_items(title, backg_image_menu)
    user_backg = select_menu_item(backg_image_menu)
    
    # Show the third menu to select a task to perform with the images
    title = 'Operations with Images'
    show_menu_items(title, task_options)
    user_task = select_menu_item(task_options)

    # Open, load and get the image size for the green background image
    green_image = green_image_jpg[user_image - 1]
    image1 = Image.open(green_image)
    width1, height1 = image1.size
    pixels1 = image1.load()

    # Open, load and get the image size for the background image
    backg_image = backg_image_jpg[user_backg - 1]
    image2 = Image.open(backg_image)
    width2, height2 = image2.size
    pixels2 = image2.load()

    # Create a new image with the same size of the first image and green background
    image_combined = Image.new('RGB', image1.size, color = (99,191,99))
    width, height = image_combined.size
    pixels_combined = image_combined.load()

    if user_task == 1:   # ---------------------------------------------------- Choice #1 - Just combine both images
        # Step 1: Create a new image and insert the first image over the second
        for x in range(0, width1):
            for y in range(0, height1):
                r, g, b = pixels1[x, y]
                if r < 100 and g > 190 and b < 100:
                    pixels_combined[x, y] = pixels2[x, y]
                else:
                    pixels_combined[x, y] = pixels1[x, y]

        # Step 2: Save & show the result
        image_combined.save('result.jpg')
        image_combined.show()

    elif user_task == 2: # ---------------------------------------------------- Choice #2 - Select where to put the image
        
        # Setp 1: Ask the user in which corner they want to put the image
        title = 'Select in which corner you want to put the image'
        show_menu_items(title, corner_options)
        user_corner = select_menu_item(corner_options)
     
        # Setp 2: Set the starting margins for finding the figure
        left = width1
        right = 0
        top = height1
        bottom = 0

        # Step 3: Find the edges of the figure in the green background image
        for x in range(0, width1):
            for y in range(0, height1):
                (r, g, b) = pixels1[x, y]
                if  not (r < 100 and g > 190 and b < 100):       # If the pixel is not green it means that it found the figure
                    if x < left : left = x                      # If the value of x is less than left, then update left successively until the end
                    if x > right : right = x                    # Same concept as above for x
                    if y < top : top = y                        # Same concept as above for y
                    if y > bottom : bottom = y                  # Same concept as above for y
        
        # Step 4: Copy from image1 the rectangle of the figure into the combined image
        for x in range(left, right):
            for y in range(top, bottom):
                r, g, b = pixels1[x, y]
                if user_corner == 1:
                    pixels_combined[x - left, y - top] = (r, g, b)
                elif user_corner == 2:
                    pixels_combined[x + (width1 - right), y - top] = (r, g, b)
                elif user_corner == 3:
                    pixels_combined[x - left, y + (height1 - bottom)] = (r, g, b)
                else:
                    pixels_combined[x + (width1 - right), y + (height1 - bottom)] = (r, g, b)

        # Step 5: Merge the new image with the background
        for x in range(0, width2):
            for y in range(0, height2):
                r, g, b = pixels_combined[x, y]
                if r < 100 and g > 190 and b < 100:
                    pixels_combined[x, y] = pixels2[x, y]

        # Step 6: Save & show the result
        image_combined.save('result.jpg')
        image_combined.show()

    else: # ------------------------------------------------------------------- Choice #3 - Play with colors
        # Merge both images and show the result in greyscale

         # Setp 1: Ask the user to select the final color of the result
        title = 'Select the color of your preference'
        show_menu_items(title, colors_options)
        user_color = select_menu_item(colors_options)

        # Step 2: Examine the image with a green background.
        # If the pixel is green, copy the corresponding pixel from the background image into the new image,
        # otherwise, copy the corresponding pixel from the image with a green background into the new image.
        for x in range(0, width1):
            for y in range(0, height1):
                r, g, b = pixels1[x, y]
                if r < 100 and g > 190 and b < 100:
                    pixels_combined[x, y] = pixels2[x, y]
                else:
                    pixels_combined[x, y] = pixels1[x, y]
        
        # Step 3: Convert the new image to the color selected
        if user_color == 1:     # --------------------------------------------- Grey
            # Use de 'convert' function from the library to convert to greyscale with the parameter L
            image_combined = image_combined.convert('L')

        elif user_color == 2:   # --------------------------------------------- More red
            for x in range(0, width1):
                for y in range(0, height1):
                    r, g, b = pixels_combined[x, y]
                    pixels_combined[x, y] = (255, g, b)

        elif user_color == 3:   # --------------------------------------------- More green
            for x in range(0, width1):
                for y in range(0, height1):
                    r, g, b = pixels_combined[x, y]
                    pixels_combined[x, y] = (r, 255, b)
        elif user_color == 4:   # --------------------------------------------- More blue
            for x in range(0, width1):
                for y in range(0, height1):
                    r, g, b = pixels_combined[x, y]
                    pixels_combined[x, y] = (r, g, 255)
        else:                   # --------------------------------------------- More yellow
            for x in range(0, width1):
                for y in range(0, height1):
                    r, g, b = pixels_combined[x, y]
                    pixels_combined[x, y] = (255, 255, b)
        
        # Step 4: Save & show the result
        image_combined.save('result.jpg')
        image_combined.show()    

    play_again()
    
# Ask the user if they want to try other images
def play_again():
    for i in range(5):
        print()
    correct = False
    while not correct:
        answer = input('Would you like to try again with other images? (Y or N) ').lower()
        if answer == 'y':
            # if player typed "y" start the game from the beginning
            correct = True
            start()
        elif answer == 'n':
            # if user types "n", exit() the program
            print('\nThanks for playing with us. We hope to see you again.')
            print()
            exit()
        else:
            print('I do not understand. Your possible options are Y or N')

# ----------------------------------------------------------------------------- START THE APP
intro()
start()
