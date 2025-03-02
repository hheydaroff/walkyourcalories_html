def calculate_steps_to_burn_calories(weight_kg, calories_to_burn, walking_pace):
    """
    Calculate the number of steps needed to burn a specific number of calories.
    
    Parameters:
    weight_kg (float): Weight in kilograms
    calories_to_burn (float): Number of calories to burn
    walking_pace (str): Pace of walking ('slow', 'average', 'fast')
    
    Returns:
    int: Number of steps needed to burn the specified calories
    """
    # Define MET values based on walking pace
    met_values = {
        'slow': 2.8,      # Slow pace (0.9 m/s)
        'average': 3.5,   # Average pace (1.34 m/s)
        'fast': 5.0       # Fast pace (1.79 m/s)
    }
    
    # Get MET value for the given walking pace
    met = met_values.get(walking_pace.lower(), 3.5)  # Default to average if invalid pace
    
    # Calculate calories burned per step based on weight
    # On average, a person burns about 0.04 calories per step at average pace
    # Adjust based on weight and pace
    calories_per_step = (weight_kg / 70) * 0.04 * (met / 3.5)
    
    # Calculate steps needed
    steps_needed = int(calories_to_burn / calories_per_step)
    
    return steps_needed

def main():
    print("Steps to Burn Calories Calculator")
    print("--------------------------------")
    
    # Get user input
    try:
        weight = float(input("Enter your weight (kg): "))
        calories = float(input("Enter calories to burn: "))
        
        print("\nSelect walking pace:")
        print("1. Slow (0.9 m/s)")
        print("2. Average (1.34 m/s)")
        print("3. Fast (1.79 m/s)")
        
        pace_choice = input("Enter your choice (1-3): ")
        
        pace_map = {
            '1': 'slow',
            '2': 'average',
            '3': 'fast'
        }
        
        walking_pace = pace_map.get(pace_choice, 'average')
        
        # Calculate steps
        steps = calculate_steps_to_burn_calories(weight, calories, walking_pace)
        
        # Display result
        print(f"\nTo burn {calories} calories, you need to take approximately {steps:,} steps at a {walking_pace} pace.")
        print(f"This is roughly equivalent to {steps/2250:.1f} miles of walking.")
        
    except ValueError:
        print("Please enter valid numerical values for weight and calories.")

if __name__ == "__main__":
    main()