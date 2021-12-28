import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wh': 'washington.csv' }

def get_filters():

  print('Hello! Let\'s explore some US bikeshare data!')
  CITY_ARRAY = {'ch': 'chicago.csv','ny': 'new_york_city.csv','wh': 'washington.csv'}
  while True:
    try:
      city = str(input('select city name:\n(ch) for chicago\n(ny) for new_york_city\n(wh)washington\n')).lower()
      if city.lower() not in CITY_ARRAY:
          print('The data you have entered is incorrect, please try again.')
      else:
          break
    except Exception as e:
          print('Something Went wrong: {}.\n'.format(e))

  print('-'*80)

  months = ['jan','feb','mar','apr','may','jun','all']
  while True:
    try:
      month = str(input('select month or select all:\n-jan\n-feb,\n-mar\n-apr\n-may\n-jun\n-all.')).lower()
      if month.lower() not in months:
          print('The data you have entered is incorrect, please try again.')
      else:
          break
    except Exception as e:
          print('Something Went wrong: {}.\n'.format(e))
    
  print('-'*80)

  days = ['sat','sun','mon','tues','wed','thurs','fri','all']
  while True:
    try:
      day = str(input('select day from:\n-sat\n-sun\n-mon\n-tues\n-wed\n-thurs\n-fri\n-all.')).lower()
      if day.lower() not in days:
          print('The data you have entered is incorrect, please try again.')
      else:
          break
    except Exception as e:
          print('Something Went wrong: {}.\n'.format(e))        
  
  print('-'*80)

  return city,month,day
  
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month      #weekday_name
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
      months = ['jan','feb','mar','apr','may','jun','all']
      month = months.index(month) + 1          #start with 0
      df = df[df['month'] == month]
      
    if day != 'all':

      df = df[df['day_of_week'].str.startswith(day.title())]
    
    return df

def display_row_data(df):
    i = 0
    answer =str(input('do you need to view more than the frist 5 rows from data? yes /no : ')).lower()
    pd.set_option('display.max_columns',None)
    while True:
      if answer == 'no' :
          break 
      #df = [i:i+5]
      print(df[i:i+5])
      answer =str(input('do you need to view more than the frist 5 rows from data? yes /no : ')).lower()
      i += 5
        




def time_stats(df):
  
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Popular Start Month:',calendar.month_name[common_month])

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*80)

def station_stats(df):
  
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('most common Start Station:',common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('most common End Station:',common_end)

    # display most frequent combination of start station and end station trip
    common_start_end =(df['Start Station']+'  --  '  +df['End Station']).mode()[0]
    print('most frequent combination of start station and end station :',common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def trip_duration_stats(df):
    #"""Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time:',total_time,)
    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average Travel Time:', avg_time ,'S')
    #print('Average Travel Time:', avg_time ,'second, or', avg_time /3600,'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def user_stats(df):
    #"""Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of User Types:\n',user_types)

    # Display counts of gender
    if 'Gender' in df:
      gender = df['Gender'].value_counts()
      print('\n Counts of Gender:\n',gender)
    else:
      print("no gender found in data . ")
    # Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df:

      earliest_year =int(df ['Birth Year'].min())
      print('\n Earliest Year of Birth:\n',earliest_year)
      recent_year = int(df ['Birth Year'].max())
      print('\n Most Recent Year of Birth:\n',recent_year )
      common_year =int(df ['Birth Year'].mode())
      print('\n Most Common Year of Birth:\n',common_year  )
    else:
      print("no birth date found in data .")  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def main():
  while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print(df.head())
        display_row_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == '__main__':
    main()
