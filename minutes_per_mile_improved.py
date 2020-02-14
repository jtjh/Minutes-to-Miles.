def kms_ran_input(message):
    while True:
        try:
            kms_ran = float(input(message))
        except ValueError:
            print("Sorry, Could you please enter the number of kilometers you ran only. ")
            continue
        else:
            return kms_ran


def minutes_ran_input(message):
    while True:
        try:
            minutes_ran = float(input(message))
        except ValueError:
            print("Sorry, Could you please enter the number of minutes you ran only. ")
            continue
        else:
            return minutes_ran


def minutes_per_km_0():
    while True:
        try:
            minutes_per_km_0 = minutes_ran / kms_ran
        except ZeroDivisionError:
            print("Thats Illegal! Im calling the Police! ")
            return exit()
        else:
            return minutes_per_km_0


kms_ran = kms_ran_input("How many kilometers did you run? ")
minutes_ran = minutes_ran_input("how many Minutes did you run for? ")


miles_to_kms = 1.61
seconds_per_minute = 60
milliseconds_per_second = 100
minutes_per_km = minutes_per_km_0()
minutes_per_mile = minutes_per_km * miles_to_kms
minutes_integer = int(minutes_per_mile)
seconds_float = minutes_per_mile - minutes_integer
seconds_multiplied = seconds_float * seconds_per_minute
seconds_integer = int(seconds_multiplied)
milliseconds_float = seconds_multiplied - seconds_integer
milliseconds_mutiplied = milliseconds_float * milliseconds_per_second
milliseconds_integer = int(milliseconds_mutiplied)


print(
    "You ran an average of",
    minutes_integer,
    "minutes",
    seconds_integer,
    "seconds",
    #    "and",
    #    milliseconds_integer,
    #    "milliseconds",
    "per mile.",
)
