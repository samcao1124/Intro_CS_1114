"""
DEFINE YOUR FUNCTIONS BELOW
"""



"""
DEFINE YOUR FUNCTIONS ABOVE
"""


def main():
    """
    Just some sample behavior.
    """
    print_earth_age()
def print_earth_age():
    staturn_str = input("How old is the Saturnian you are talking to?")
    staturn_float = float(staturn_str)
    staturn_float = int(10759)
    staturn_str = int(staturn_float * 10)
    age_Earth_years = staturn_str //365

    staturn_str=staturn_str%365
    age_Earth_months = staturn_str //30

    staturn_str=staturn_str%30
    age_Earth_days = staturn_str //1

    print("This Saturnian is",age_Earth_years,"Earth-years,",age_Earth_months,"Earth-months,", "and",age_Earth_days,"Earth-days","old.")







# DO NOT WRITE CODE BEYOND THIS LINE ###


if __name__ == '__main__':
    main()
