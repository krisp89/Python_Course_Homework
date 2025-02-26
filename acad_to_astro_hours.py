
# # Task:
# Write a Python program that calculates the total duration (in astronomical hours) of a Python course consisting of 64 academical hours, including the respective breaks.
# Given:
# 1 astronomical hour = 60 minutes
# 1 academical hour = 40 minutes
# The course is structured in sessions, where:
# Each session consists of 4 academical hours
# Each session includes a 20-minute break
# Expected Output
# Total duration in astronomical hours: 48.00
# Copy
# Requirements:
# Your solution should be readable and easy to maintain.
# Write your code in: HW/acad_to_astro_hours.py.

#I have used GPT to find a solution to this and to understand the logic

def calculate_total_duration(total_acad_hours):
    # Calculate the total number of sessions
    num_sessions = total_acad_hours // 4
    
    # Calculate the total academical time (excluding breaks)
    total_acad_time = total_acad_hours * 40  # 1 academical hour = 40 minutes
    
    # Calculate the total break time
    total_break_time = num_sessions * 20  # Each session has a 20-minute break
    
    # Calculate the total duration in minutes
    total_minutes = total_acad_time + total_break_time
    
    # Convert the total duration to astronomical hours
    total_astro_hours = total_minutes / 60  # 1 astronomical hour = 60 minutes
    
    return total_astro_hours

# Main program
total_acad_hours = 64
total_astro_hours = calculate_total_duration(total_acad_hours)
print(f"Total duration in astronomical hours:{total_astro_hours:.2f}")