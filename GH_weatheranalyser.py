# PARTE 01 - TEMPERATURES
import random
daily_temperatures = [random.randint(0, 35) for _ in range(30)]
print("Daily Temperatures: ", daily_temperatures)

# Find the day with the lowest temperature.
min_temp = None
min_day = None
for day, temperature in enumerate(daily_temperatures, start=1):
    if min_temp is None or temperature < min_temp:
        min_temp = temperature
        min_day = day
print("Day with the lowest temperature: ", min_day)

# Find the day with the highest temperature.
max_temp = None
max_day = None
for day, temperature in enumerate(daily_temperatures, start=1):
    if max_temp is None or temperature > max_temp:
        hax_temp = temperature
        max_day = day
print("Day with the highest temperature: ", max_day)

# Find the days where the temperature rises above 20°C.
above_20 = []
for day, temperature in enumerate(daily_temperatures, start=1):
    if temperature > 20:
        above_20.append(day)
print("Days where the temperature rises above 20°C:", above_20)

# Find the days where the temperature drops below 10°C.
below_10 = []
for day, temperature in enumerate(daily_temperatures, start=1):
    if temperature < 10:
        below_10.append(day)
print("Days where the temperature drops below 10°C: ", below_10)

# Find the days where the temperature was hotter than any of the days in the month.
hotter_days = []
for day, temperature in enumerate(daily_temperatures[1:], start=2):
    if temperature > max(daily_temperatures[:day - 1]):
        hotter_days.append(day)
print("Days where the temperature was hotter than any of the day: ", hotter_days)


# PARTE 02 - RAINFALL
daily_rainfall = [random.randint(0, 10) for _ in range(30)]
print("Daily Rainfall: ", daily_rainfall)

# Record the amount of ‘bad weather’ days, the number of days that the rainfall is above 3mm and the temperature is below 10°C.
bad_days = 0
for temperature, rainfall in zip(daily_temperatures, daily_rainfall):
    if temperature < 10 and rainfall > 3:
        bad_days += 1
print("Numer of bad weather days: ", bad_days)

# Record the amount of ‘average weather’ days, the number of days that the rainfall is between 1mm and 5mm and the temperature is between 10°C and 18°C.
avarage_days = 0
for temperature, rainfall in zip(daily_temperatures, daily_rainfall):
    if 10 <= temperature <= 18 and 1 <= rainfall <= 5:
        avarage_days += 1
print("Number of avarage weather days: ", avarage_days)

# Record the amount ‘good weather’ days, the number of days that the rainfall is below 2mm, and the temperature is above 18°C.
good_days = 0
for temperature, rainfall in zip(daily_temperatures, daily_rainfall):
    if temperature > 18 and rainfall < 2:
        avarage_days += 1
print("Number of good weather days: ", avarage_days)
