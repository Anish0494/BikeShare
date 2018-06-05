import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    print("which city you want to look for chicago, new york city, washington?")
    city=input()
    city=city.lower()
    if (city not in CITY_DATA):
        print("OOPS!!!wrong input please try again")
        get_filters()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    print("which month do you want for data to get filter ")
    month=input()
    month=month.lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if (month not in months):
        print("OOPS!!!wrong input please try again")
        get_filters()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("Which day of week you want to get data filter")
    day=input()
    day=day.lower()
    week=['monday', 'tuesday', 'wednesday','thrusday','friday','saturday','sunday']
    if(day not in week):
        print("OOPS!!!wrong input please try again")
        get_filters()
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
    df=pd.DataFrame(pd.read_csv(CITY_DATA[city]))
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    b=0
    b=input('How would want to filter the data? enter both, month or days\n')   
    if(b.lower() == 'both' or b.lower() == 'month'):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if (b.lower() == 'both' or b.lower() == 'days'):
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    m=df['month'].mode()[0]
    print("most common month(in numeric) is:-",m)
    # TO DO: display the most common day of week
    d=df['day_of_week'].mode()[0]
    print("most common day of week is:-",d)
    # TO DO: display the most common start hour
    sh=df['Start Time'].dt.hour.mode()[0]
    print("most popular start time:-",sh)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    print("Most commonly used start station:-",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most commonly used end station:-",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    l=df['Start Station']+df['End Station']
    print("Most frequent combination of the start station and end station:-",l.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:-",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean travel Time:-",df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)
    start_time = time.time()
    print("\nDisplaying more detail of subscriber and customer....\n")
    s=df[df['User Type']=='Subscriber']
    c=df[df['User Type']=='Customer']
    st=s['Trip Duration'].sum()
    ct=c['Trip Duration'].sum()
    print("Total time travel by subscriber---",st)
    print("Total time travel by customer---",ct)
    
    print("Mean travel time by subscriber---",s['Trip Duration'].mean())
    print("Mean travel time by customer--",c['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Displaying the type of the user-------\n")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print("\nDisplaying the counts of gender----\n")
    try:
        print(df['Gender'].value_counts())
    except KeyError:
        print("No Gender data to display")


    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nDisplaying the details about the birth year......\n")
    try:
        print("Most earliest year of birth:-",df['Birth Year'].min())
        print("Most recent year of birth:-",df['Birth Year'].max())
        print("Most common year of birth:-",df['Birth Year'].mode()[0])
    except KeyError:
        print("No birth data to display")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df):
    a=input('\ndo you want to know the data of individual? enter yes or no\n')
    if(a.lower() != 'no'):
        h=0
        while(True):
            print(df[0+h:5+h])
            cycle=input('do you want to stop displaying more data? enter yes or no\n')
            if(cycle.lower() == 'yes'):
                break
            h+=5
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
