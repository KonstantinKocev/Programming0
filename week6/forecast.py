def forecast(days):
    counter_snow = 0
    counter_rain = 0
    counter_sunshine = 0
    for weather in days:
        if weather == "snow":
            counter_snow += 1
        if weather == "rain":
            counter_rain += 1
        if weather == "sunshine":
            counter_sunshine += 1
    if counter_rain == counter_sunshine == counter_snow:
        return "Tomorrow will be " + days[-1]
    else:
        return max_found_weather(counter_rain, counter_sunshine, counter_snow)


def max_found_weather(counter_rain, counter_sunshine, counter_snow):
    max_found = (counter_sunshine, counter_rain, counter_snow)
    if max(max_found) == counter_sunshine:
        return "Tomorrow will be sunshine."
    if max(max_found) == counter_snow:
        return "Tomorrow will be snow."
    if max(max_found) == counter_rain:
        return "Tomorrow will be rain."


days_weather = ["snow", "snow", "rain", "rain", "sunshine", "sunshine"]
print(forecast(days_weather))
