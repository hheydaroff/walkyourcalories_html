from src.config import Config

def calculate_steps(calories: float, weight: float, pace: str) -> int:
    # Get MET value based on pace
    met = Config.MET_VALUES[pace]

    # Calculate calories burned per minute
    kcal_per_minute = (met * 3.5 * weight) / 200

    # Calculate calories burned per step
    kcal_per_step = kcal_per_minute / Config.STEPS_PER_MINUTE

    # Calculate total steps
    steps = int(calories / kcal_per_step)

    return steps