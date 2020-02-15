def kms_ran_input(message):
    while True:
        try:
            get_kms_ran = float(input(message))
        except ValueError:
            print("Sorry, Could you please enter Numerical digits only. ")
            continue
        if get_kms_ran <= 0:
            print("Sorry, Can you please Enter a Positive number greater then 0. ")
            continue
        else:
            return get_kms_ran


def minutes_ran_input(message):
    while True:
        try:
            get_minutes_ran = float(input(message))
        except ValueError:
            print("Sorry, Could you please enter Numerical digits only. ")
            continue
        if get_minutes_ran <= 0:
            print("Sorry, Can you please Enter a Positive number greater then 0. ")
            continue
        else:
            return get_minutes_ran


kms_ran = kms_ran_input("How many kilometres did you run? ")
minutes_ran = minutes_ran_input("how many Minutes did you run for? ")
miles_to_kms = 1.61
seconds_per_minute = 60
minutes_per_km = minutes_ran / kms_ran
minutes_per_mile = minutes_per_km * miles_to_kms
minutes_integer = int(minutes_per_mile)
seconds_float = minutes_per_mile - minutes_integer
seconds_multiplied = seconds_float * seconds_per_minute
seconds_integer = int(seconds_multiplied)
milliseconds_per_second = 100
milliseconds_float = seconds_multiplied - seconds_integer
milliseconds_mutiplied = milliseconds_float * milliseconds_per_second
milliseconds_integer = int(milliseconds_mutiplied)

print(
    "You ran an average of",
    minutes_integer,
    "minutes",
    seconds_integer,
    "seconds",
    "and",
    milliseconds_integer,
    "milliseconds",
    "per mile.",
)
