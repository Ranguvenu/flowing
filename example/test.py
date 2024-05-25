from datetime import datetime, timedelta

def add_five_minutes(current_time):
    return (datetime.strptime(current_time, "%Y-%m-%d %H:%M") + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M")

# Example usage
current_time = "2024-05-14 09:55"
new_time = add_five_minutes(current_time)
print("New Time:", new_time)
