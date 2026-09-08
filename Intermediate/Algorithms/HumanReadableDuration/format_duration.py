def format_duration(seconds):
    if seconds == 0:
        return "now"

    units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    ]

    parts = []

    for unit, value in units:
        amount, seconds = divmod(seconds, value)

        if amount:
            parts.append(f"{amount} {unit}{'s' if amount > 1 else ''}")

    if len(parts) == 1:
        return parts[0]

    return ", ".join(parts[:-1]) + " and " + parts[-1]


# Test
print(format_duration(0))       # now
print(format_duration(62))      # 1 minute and 2 seconds
print(format_duration(3662))    # 1 hour, 1 minute and 2 seconds
print(format_duration(31536000))  # 1 year
print(format_duration(132030240))  # 4 years, 68 days, 3 hours and 4 minutes
