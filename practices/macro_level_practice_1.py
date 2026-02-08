# This file demonstrates macro-level coding practices with poor practices.
# Refactor this code to follow the macro-level best practices outlined in Good_Coding_Practices.md

# Section 1: Hardcoded Variables
# Problem: Rectify the hardcoded values in the function below.

def calculate_total_price(price, weight):
    price = price * (1-0.1) # Applying discount
    price = price * 1.08 # Applying a tax
    shipping_cost = weight * 2.5 # Shipping cost
    return price + shipping_cost

# Section 2: Constants Not Defined at Top
# Problem: Constants are defined throughout the file. Define them appropriately.

def process_order(customer_name, items_count):
    print(f"Processing order for {customer_name}")
    if items_count > 100 :
        print("Order exceeds maximum items")
    if items_count >= 50 :
        print("Discount applied was too large, applying maximum discount")


# Section 3: Functions Not Grouped into Classes
# Problem: Related functions for processing a tif image are scattered. Group them into a class.
# This class should have an init funcition that takes in file path and folder path as parameters, and a run function that takes in the new_width and new_height, executing the full process.

import cv2
def load_image(file_path):
    img = cv2.imread(file_path)
    return img


def resize_image(img, new_width, new_height):
    resized_img = cv2.resize(img, (new_width, new_height))
    return resized_img


def save_image(image, output_folder_path, filename):
    full_path = f"{output_folder_path}/{filename}"
    cv2.imwrite(full_path, image)
    return f"Image saved to {full_path}"


def convert_to_3_channel(image):
    converted_img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return converted_img

def process_image(file_path, output_folder_path, new_width, new_height):
    img = load_image(file_path)
    resized_img = resize_image(img, new_width, new_height)
    converted_img = convert_to_3_channel(resized_img)
    save_status = save_image(converted_img, output_folder_path, "processed_image.png")
    return save_status

# Section 4: Similar Functions Not Grouped Together
# Problem: Related functions are scattered throughout the file. Reorganize them.


def format_date(day, month, year):
    """Format a date."""
    return f"{day}/{month}/{year}"


def calculate_total_price(price, quantity):
    """Calculate total price."""
    return price * quantity


def format_time(hour, minute, second):
    """Format a time."""
    return f"{hour}:{minute}:{second}"


def calculate_average(numbers):
    """Calculate average of numbers."""
    return sum(numbers) / len(numbers)


def is_valid_date(day, month, year):
    """Validate a date."""
    return 1 <= day <= 31 and 1 <= month <= 12 and year > 0

# Section 5: No Module Organization
# Problem: All these functions are in the main python file. Organize them into utils folder and import them here.

def calculate_area(radius):
    """Calculate area of a circle."""
    PI = 3.14159
    return PI * radius ** 2


def calculate_perimeter(radius):
    """Calculate perimeter of a circle."""
    PI = 3.14159
    return 2 * PI * radius


def convert_to_uppercase(text):
    """Convert text to uppercase."""
    return text.upper()


def convert_to_lowercase(text):
    """Convert text to lowercase."""
    return text.lower()

