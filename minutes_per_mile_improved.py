def kms_ran_input(message):
    while True:
        try:
            get_kms_ran = float(input(message))
        except ValueError:
            print("Sorry, could you please enter Numerical digits only.")
            continue
        if get_kms_ran <= 0:
            print("Sorry, can you please Enter a Positive number greater than 0.")
            continue
        else:
            return get_kms_ran


def minutes_ran_input(message):
    while True:
        try:
            get_minutes_ran = float(input(message))
        except ValueError:
            print("Sorry, could you please enter Numerical digits only. ")
            continue
        if get_minutes_ran <= 0:
            print("Sorry, can you please Enter a Positive number greater than 0.")
            continue
        else:
            return get_minutes_ran


kms_ran = kms_ran_input("How many kilometres did you run? ")
minutes_ran = minutes_ran_input("How many Minutes did you run for? ")
minutes_per_km = minutes_ran / kms_ran
miles_to_kms = 1.61
minutes_per_mile = minutes_per_km * miles_to_kms
minutes_integer = int(minutes_per_mile)
seconds_float = minutes_per_mile - minutes_integer
seconds_per_minute = 60
seconds_multiplied = seconds_float * seconds_per_minute
seconds_integer = int(seconds_multiplied)

print(
    "You ran an average of",
    minutes_integer,
    "minutes and",
    seconds_integer,
    "seconds",
    "per mile.",
)
