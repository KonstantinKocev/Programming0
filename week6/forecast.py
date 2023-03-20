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
    elif counter_sunshine < counter_snow and counter_sunshine < counter_rain\
            or counter_snow < counter_sunshine and counter_snow < counter_rain\
            or counter_rain < counter_sunshine and counter_rain < counter_snow:
        return min_weather(counter_rain, counter_sunshine, counter_snow)
    else:
        return two_less_one_stay(counter_rain, counter_sunshine, counter_snow)


def two_less_one_stay(counter_rain, counter_sunshine, counter_snow):
    if counter_rain > counter_sunshine and counter_rain > counter_snow:
        return "Tomorrow will be rain."
    if counter_sunshine > counter_snow and counter_sunshine > counter_rain:
        return "Tomorrow will be sunshine."
    if counter_snow > counter_rain and counter_snow > counter_sunshine:
        return "Tomorrow will be snow."


def min_weather(counter_rain, counter_sunshine, counter_snow):
    if counter_rain < counter_sunshine and counter_rain < counter_snow or counter_rain == 0:
        return "Tomorrow will be rain."
    if counter_snow < counter_sunshine and counter_snow < counter_rain or counter_snow == 0:
        return "Tomorrow will be snow."
    if counter_sunshine < counter_snow and counter_sunshine < counter_rain or counter_sunshine == 0:
        return "Tomorrow will be sunshine."


days_weather = ["rain", "sunshine", "snow", "snow"]
print(forecast(days_weather))
