def validate_input(calories, weight, pace):
    errors = []

    try:
        calories = float(calories) if calories and str(calories).strip() else None
        if calories is None or calories <= 0:
            errors.append("Calories must be a positive number.")
    except ValueError:
        errors.append("Invalid calories value. Please enter a number.")

    try:
        weight = float(weight) if weight and str(weight).strip() else None
        if weight is None or weight <= 0:
            errors.append("Weight must be a positive number.")
    except ValueError:
        errors.append("Invalid weight value. Please enter a number.")

    if not pace or pace not in ['slow', 'moderate', 'fast']:
        errors.append("Invalid pace. Choose 'slow', 'moderate', or 'fast'.")

    return errors