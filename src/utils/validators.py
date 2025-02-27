from src.config import Config

def validate_input(calories, weight, pace):
    errors = []
    
    try:
        calories = float(calories)
        if calories < Config.MIN_CALORIES or calories > Config.MAX_CALORIES:
            errors.append(f"Calories must be between {Config.MIN_CALORIES} and {Config.MAX_CALORIES}")
    except ValueError:
        errors.append("Invalid calories value")

    try:
        weight = float(weight)
        if weight < Config.MIN_WEIGHT or weight > Config.MAX_WEIGHT:
            errors.append(f"Weight must be between {Config.MIN_WEIGHT} and {Config.MAX_WEIGHT} kg")
    except ValueError:
        errors.append("Invalid weight value")

    if pace not in Config.MET_VALUES:
        errors.append(f"Invalid pace. Choose from: {', '.join(Config.MET_VALUES.keys())}")

    return errors