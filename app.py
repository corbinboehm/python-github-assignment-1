# Simple study time tracker program

# Welcome message
print("Welcome to my Python program!")

# Ask the user for daily study hours
hours = input("How many hours did you study today? ")

# Convert input to a number with error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Calculate weekly estimate
weekly_hours = hours * 7

# Display result clearly
print(f"You are on track to study {weekly_hours} hours this week.")