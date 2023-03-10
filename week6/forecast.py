"""Синоптикът и времето
Тъй като времето през месец март стана толкова непредвидимо, синоптиците си измислиха нова формула, по която да предсказват какво ще има утре - сняг, дъжд или слънце.

Формулата е проста:

Взимаме колкото си искаме поредни дни, в които знаем дали е валяло, пекло или трупало (за простота, всеки ден се случва само по 1 такова събитие)
Ако е валяло повече от колкото е пекло или трупало, утре пак ще вали.
Ако е пекло повече, от колкото е валяло или пък трупало утре пак ще пече.
Ако е трупало повече, от колкото е валяло или пътк пекло, утре пак ще трупа.
Ако пък има 2 събития с равна бройка срещания (които са по-големи от 3тото събитие), за взетия период от време, то утре ще се случи 3тото събитие.
Ако пък има 3 събития с равна бройка срещания, за взетия период от време, то утре ще бъде това, което е било на последния ден.
Събитията се обозначават като низове:

"sunshine"
"rain"
"snow"
Във файла forecast.py, напишете функцията forecast(days), която връща низ, което ще съотвества на времето утре.

Примери:

Ако имаме days = ["snow", "snow", "rain", "sunshine"], то утре ще вали сняг, защото "snow" се среща най-много пъти.
Ако имаме days = ["rain", "rain", "snow", "snow", "sunshine", "sunshine"], то утре пак ще пече слънце, защото имаме 3 събития с еднакъв брой срещания
Ако имаме days = ["rain", "rain", "sunshine", "sunshine"], то утре ще вали сняг. Да. Март е.

"""


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


days_weather = ["rain", "rain", "snow", "snow", "snow", "sunshine", "sunshine", ]
print(forecast(days_weather))
