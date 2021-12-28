import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
start_time = time.time()
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Chooce a city: Chicago, New York City or Washington').lower()
        if city not in CITY_DATA.keys():
            print('Invalid input!')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("Chooce your search month: january, february, march, april, may, june or 'all' ").lower()
        months=['january','february','march','april','may','june']
        if month !='all' and month not in months:
            print('Enter a valid month')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Chooce your search day or "all" ').lower()
        days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        if day !='all' and day not in days:
            print('Enter a valid day')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])

    df['month']=df['Start Time'].dt.month

    df['day_of_week']=df['Start Time'].dt.day_name()

    if month !='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
    
        df=df[df['month']==month]
    
    if day !='all':
        df=df[df['day_of_week']==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month']=df['Start Time'].dt.month
    common_month=df['month'].mode()[0]
    print(common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print(common_start_station)

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print(common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print(total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender information in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)
    else:
        print("There is no birth year information in this city.")

# Asking 5 lines of the raw data and more, if they want
def display_data(df):
    raw_data = 0
    while True:
        answer = input("Do you want to see 5 rows of data?").lower()
        if answer not in ['yes', 'no']:
            answer = input("Please type Yes or No.").lower()
        elif answer == 'yes':
            raw_data += 0
            print(df.iloc[raw_data : raw_data + 5])
            break
    while True:
        again = input("Do you want to see the next 5 rows of data?: ").lower()
        if again == 'no':
                    break
        elif again == 'yes':
                raw_data += 5
                print(df.iloc[raw_data : raw_data + 5])
        elif answer == 'no':
            return
        
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
