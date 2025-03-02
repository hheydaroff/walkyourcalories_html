def calculate_steps(calories, weight, height, pace):
    # Constants for MET values (Metabolic Equivalent of Task)
    MET_SLOW = 2.9
    MET_MODERATE = 3.3
    MET_FAST = 3.9

    # Choose MET based on pace
    if pace == 'slow':
        met = MET_SLOW
    elif pace == 'moderate':
        met = MET_MODERATE
    elif pace == 'fast':
        met = MET_FAST
    else:
        raise ValueError("Invalid pace. Choose 'slow', 'moderate', or 'fast'.")

    # Calculate calories burned per minute
    calories_per_minute = (met * 3.5 * weight) / 200

    # Calculate total minutes needed to burn the given calories
    minutes = calories / calories_per_minute

    # Estimate steps based on height and pace
    # A rough estimate is that a person takes about 2000 steps to walk a mile
    # and an average person walks about 3 miles per hour at a moderate pace
    steps_per_minute = 2000 / 20  # 2000 steps per mile / 20 minutes per mile

    # Adjust steps per minute based on height and pace
    height_factor = height / 170  # 170 cm is average height
    if pace == 'slow':
        steps_per_minute *= 0.8 * height_factor
    elif pace == 'fast':
        steps_per_minute *= 1.2 * height_factor

    # Calculate total steps
    steps = int(minutes * steps_per_minute)

    return steps