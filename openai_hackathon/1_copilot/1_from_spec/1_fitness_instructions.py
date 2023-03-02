"""
Add type hints to all your functionality and use mypi to test for correctness.

"""
from random import choice
import numpy as np

"""
    Compute the total intensity of a workout.
    Workout is a struct containing intensity and number of repetitions
"""
def compute_workout_intensity(workout: tuple[str, int, int]) -> int:
    # workout[0] is the name of the workout
    # workout[1] is the number of repetitions
    # workout[2] is the intensity
    return workout[1] * workout[2]

"""
    Compute the total intensity of a routine for any number of workouts.
    Routine is a list of workouts.
"""
def compute_routine_intensity(routine: list[tuple[str, int, int]]) -> int:
    return sum([compute_workout_intensity(workout) for workout in routine])

"""
    Compute the total intensity for any number of days that has any number routines which is a list of workouts.
"""
def compute_week_intensity(week: dict[str, list[tuple[str, int, int]]]) -> int:
    return sum([compute_routine_intensity(routine) for routine in week.values()])

"""
    Pick a workout for a body part.
"""
def pick_workout(workouts_per_body_part: dict, body_part: str) -> tuple[str, int, int]:
    # Pick a random workout for the body part
    return choice(workouts_per_body_part[body_part])

"""
    Plan a week of workouts given a list of body parts and a list of days of the week.
"""
def plan_week(workouts_per_body_part: dict, intensity: tuple[int, int]) -> int: 
    # Create a list of days of the week
    days = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}

    def populate_week(days: dict, workouts_per_body_part: dict, week_intensity: int = 0):
        # Loop through the keys of workouts_per_body_part
        for body_part in workouts_per_body_part.keys():
            # Pick a workout for the body part
            workout = pick_workout(workouts_per_body_part, body_part)
            workout_intensity = compute_workout_intensity(workout)    
            print(workout, workout_intensity)     

            # When the total intensity of the week is less than the maximum intensity add a workout to the week
            if week_intensity + workout_intensity < intensity[1]:
                # Draw a random key from days
                day = choice(list(days.keys()))

                # Assign the workout to the day
                days[day].append(workout) 
                week_intensity += workout_intensity

                # When minimum intensity is reached, return the days
                if week_intensity > intensity[0]:
                    return days

        # Recursively call itself such that minimum intensity is reached
        return populate_week(days, workouts_per_body_part, week_intensity)

    return populate_week(days, workouts_per_body_part)              

# Main function
if __name__ == "__main__":
    # Define a minimum and maximum weekly intensity
    intensity = (100, 200)

    # List of possible repititions containing random integers between 1 and 5.
    possible_repetitions = [1, 2, 3, 4, 5]

    # List of possible intensities containing random integers between 1 and 20.
    possible_intensities = [1, 5, 10, 15, 20]

    # Dictionary of body parts with a list of workouts for each body part where a workout contains a random pick from possible_repetitions and a random pick from possible_intensities.
    workouts_per_body_part = {
        "arms": 
            [("pushups", choice(possible_repetitions), choice(possible_intensities)),
            ("pullups", choice(possible_repetitions), choice(possible_intensities)),
            ("dips", choice(possible_repetitions), choice(possible_intensities))],
        "legs":
            [("squats", choice(possible_repetitions), choice(possible_intensities)),
            ("lunges", choice(possible_repetitions), choice(possible_intensities)),
            ("calf raises", choice(possible_repetitions), choice(possible_intensities))],
        "core": 
            [("planks", choice(possible_repetitions), choice(possible_intensities)),
            ("crunches", choice(possible_repetitions), choice(possible_intensities)),
            ("side planks", choice(possible_repetitions), choice(possible_intensities))],
    }

    # Create a plan for the week using workouts_per_body_part and intensity
    week = plan_week(workouts_per_body_part, intensity)
    print(week)
    print(compute_week_intensity(week))
