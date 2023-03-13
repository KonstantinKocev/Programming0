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
        return one_less_two_stay(counter_rain, counter_sunshine, counter_snow)
    else:
        return two_less_one_stay(counter_rain, counter_sunshine, counter_snow)


def two_less_one_stay(counter_rain, counter_sunshine, counter_snow):
    all_weathers = (counter_sunshine, counter_rain, counter_snow)
    if max(all_weathers) == counter_sunshine:
        return "Tomorrow will be sunshine."
    if max(all_weathers) == counter_snow:
        return "Tomorrow will be snow."
    if max(all_weathers) == counter_rain:
        return "Tomorrow will be rain."


def one_less_two_stay(counter_rain, counter_sunshine, counter_snow):
    all_weathers = (counter_sunshine, counter_rain, counter_snow)
    new_weathers = []
    if min(all_weathers) == counter_snow:
        new_weathers += "rain", "sunshine"
    if min(all_weathers) == counter_rain:
        new_weathers += "snow", "sunshine"
    if min(all_weathers) == counter_sunshine:
        new_weathers += "snow", "rain"
    return "Tomorrow will be " + new_weathers[-1]


days_weather = ["snow", "snow", "rain", "rain", "sunshine", "sunshine"]
print(forecast(days_weather))
