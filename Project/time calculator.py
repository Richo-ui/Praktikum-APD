def add_time(start, duration, starting_day=None):
    # Helper dictionaries
    days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_to = {day.lower(): index for index, day in enumerate(days_week)}

    # Split start time
    start_time, meridiem = start.split()
    start_hours, start_minutes = map(int, start_time.split(":"))

    # Convert start time to 24-hour format
    if meridiem == "PM":
        start_hours += 12 if start_hours != 12 else 0
    elif start_hours == 12:
        start_hours = 0  # Adjust for 12 AM to 0 hours

    # Split duration
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # Calculate new time
    total_minutes = start_minutes + duration_minutes
    new_minutes = total_minutes % 60
    extra_hours = total_minutes // 60

    total_hours = start_hours + duration_hours + extra_hours
    new_hours = total_hours % 24
    days_later = total_hours // 24

    # Determine the final AM/PM and convert back to 12-hour format
    if new_hours >= 12:
        new_meridiem = "PM"
        if new_hours > 12:
            new_hours -= 12
    else:
        new_meridiem = "AM"
        if new_hours == 0:
            new_hours = 12

    # Format time
    new_time = f"{new_hours}:{new_minutes:02d} {new_meridiem}"

    # Handle day calculation if starting day is provided
    if starting_day:
        day_start = day_to[starting_day.lower()]
        day_end = (day_start + days_later) % 7
        end_day = days_week[day_end]
        new_time += f", {end_day}"

    # Add notation for days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
print(add_time("4:00 PM", "30:00", "Monday"))