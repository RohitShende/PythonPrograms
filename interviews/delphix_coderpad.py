# Your previous Plain Text content is preserved below:
#
# This is just a simple shared plaintext pad, with no execution capabilities.
#
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
#
# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings
#
# Enjoy your interview!
#
# ===== Preface =====
#
# This question is very difficult in C and C++, where there is
# insufficient library support to answer it in an hour. If you
# prefer to program in one of those languages, please ask us to
# provide you with a question designed for those languages instead!
#
# ===== Intro =====
#
# The Delphix Boston office is located in Boston’s financial district.
# MBTA (Massachusetts Bay Transportation Authority) is a public
# transportation system serving the Massachusetts Bay area.  Many
# engineers in the Boston office use the Park Street Station to get to/from
# the office.
#
# As engineers in the office will tell you, the MBTA system is
# infamously off schedule. Luckily, the MBTA public API
# (https://www.mbta.com/developers/v3-api) has a real-time information
# feed containing information about real-time estimated departures for
# specific stations. Your goal is to write a small program that utilizes
# the MBTA API that will quickly tell :
# - The current time
# - The next 10 trains leaving Park Street Station
# - Where they are going (destination town/city)
# - Minutes until scheduled departure
#
#
# Rules/constraints:
#
# - Print the trains grouped by which line they are using, and in the
#   order that they are leaving the station
# - Limit the number of trains printed to the 10 trains next leaving
#   the station. Do not print trains that have already left the station (negative departure time).
# - Print the number of minutes until the scheduled departure time.
# - Print the destination town/city of each train
# - You can use any standard or third party libraries available in coderpad.
#
# Example output:
#
# ```
# <Current Time>
# ----Red Line----
# Ashmont/Braintree: Departing in 3 minutes
# Alewife: Departing in 5 minutes
# Ashmont/Braintree: Departing in 9 minutes
#
# ----Green Line C----
# North Station: Departing in 4 minutes
# Cleveland Circle: Departing in 6 minutes
#
# ----Green Line E----
# North Station: Departing in 4 minutes
# Heath Street: Departing in 5 minutes
#
# ----Green Line D----
# Riverside: Departing in 5 minutes
# Government Center: Departing in 7 minutes
#
# ----Green Line B----
# Park Street: Departing in 6 minutes
#
# ```
#
# Your output does not need to match this, this is just an example.
# If you have better ideas of how to display the data, please do!
# Just include the required information.
#
# You should implement this in whatever language you're most
# comfortable with. Consider this to be production level code and
# should include, but not limited to, exception handling, error
# checking, and diagnostic/logging information. You should consider
# execution performance, memory consumption, and general efficiency
# in your design.
#
# Finally, please help us by keeping this question and your
# answer secret so that every candidate has a fair chance in
# future Delphix interviews.
#
#
# ===== Steps =====
#
# 1.  Choose the language you want to code in from the menu
#     labeled "Plain Text" in the top right corner of the
#     screen. You will see a "Run" button appear on the top
#     left -- clicking this will send your code to a Linux
#     server and compile / run it. Output will appear on the
#     right side of the screen.
#
#     For information about what libraries are available for
#     your chosen language, see:
#
#       https://coderpad.io/languages
#
# 2.  Pull up the documentation for the API you'll be using:
#
#       https://api-v3.mbta.com/docs/swagger/index.html#/Prediction/ApiWeb_PredictionController_index
#
#       https://www.mbta.com/developers/v3-api
#
# 3.  Since the above API doesn’t have the name of the routes,
#     or the destination name we are interested in, you’ll want
#     to include Route Relationships in the query. To help you save
#     time figuring out the stop to filter over, use "place-pktrm".
#     This is the MBTA's id for the Park Street Station.
#
#     Suggested parameters for the API call:
#
#     include=route -- Used to get additional route information
#
#     filter[stop]=place-pktrm -- Used to filter the data to Park
#       Street Station
#
#     sort=departure_time -- Used to sort by 'departure_time' instead
#       of the default 'arrival_time'
#
# 4.  Implement the functionality described above, using data
#     fetched dynamically from the MBTA API endpoint here:
#
#       https://api-v3.mbta.com/predictions
#
# 5.  Writing tests for your code is optional. If you do write tests for your code,
#     add them to the main() method of your program so that we can easily run them.
#
#
# ====== FAQs =====
#
# Q:  What if the API doesn't return any trains? How do I test my code?
# A:  You can use the attached file with a sample response. You'll need
#     to use a timestamp of 2021_05_11 17:15:00 UTC-4 as the current time
#     in order to get 'realistic' arrival times. It's path is:
#     /home/coderpad/data/MBTA_Departures_2021_05_11T5_15_00.txt
#
# Q:  How do I turn in my solution?
# A:  Anything you've typed into this document will be saved.
#     If you were given a Takehome question, there should be a Submit
#     Button in the bottom right of the coderpad page. If you do not
#     see such a button, feel free to email us when you are done with
#     your solution. We will respond confirming we've received the
#     solution within 24 hours.
#
# Q:  What timezone does the MBTA API use?
# A:  They use UTC-4. For your solution, it would make the most sense
#     to compare arrival times in the same time zone.
#
# Q:  What does a direction_id of 0 or 1 mean?
# A:  This is used as a key to identify which direction (0 or 1) the
#     train is headed in. You can use this key with the
#     direction_destinations in the included route data to find the
#     destination of the train.
#
# Q:  How do I know if my solution is correct?
# A:  Make sure you've read the assignment carefully and you're
#     convinced your program does what you think it should
#     in the common case. If your program does what the assignment
#     dictates, you will get full credit. We do not use an
#     auto-grader, so we do not have any values for you to
#     check correctness against.
#
# Q:  What is Delphix looking for in a solution?
# A:  After submitting your code, we'll have a pair of engineers
#     evaluate it and determine next steps in the interview process.
#     We are looking for correct, easy-to-read, robust code.
#     Specifically, ensure your code is idiomatic and laid out
#     logically. Ensure it is correct. Ensure it handles all edge
#     cases and error cases elegantly.
#
# Q:  If I need a clarification, who should I ask?
# A:  Send all questions to the email address that sent you
#     this document, and an engineer at Delphix will get
#     back to you ASAP (we're pretty quick during normal
#     business hours).
#
# Q:  How long should this question take me?
# A:  Approximately 1 hour, but it could take more or less
#     depending on your experience with web APIs and the
#     language you choose.
#
# Q:  When is this due?
# A:  We will begin grading your answer 24 hours after it is
#     sent to you, so that is the deadline.
#
# Q:  Can I use any external resources to help me?
# A:  Absolutely! Feel free to use any online resources you
#     like, but please don't collaborate with anyone else.
#
# Q:  Can I use my favorite library in my program?
# A:  Unfortunately, there is no way to load external
#     libraries into CoderPad, so you must stick to what
#     they provide out of the box for your language (although
#     they do support for many popular general-use libraries):
#
#       https://coderpad.io/languages
#
#     If you really want to use something that's not
#     available, email the person who sent you this link
#     and we will work with you to find a solution.
#
# Q: Can I code this up in a different IDE?
# A: Of course! However, we do not have your environment
#    to run your code in. We ask that you submit your final
#    code via CoderPad (and make sure it can run). This gives
#    our graders the ability to run your code rather than guessing.
#
# Q:  Why does my program terminate unexpectedly in
#     CoderPad, and why can't I read from stdin or pass
#     arguments on the command line?
# A:  CoderPad places a limit on the runtime and amount of
#     output your code can use, but you should be able to
#     make your code fit within those limits. You can hard
#     code any arguments or inputs to the program in your
#     main() method or in your tests.
#
# Q:  I'm a Vim/Emacs fan -- is there any way to use those
#     keybindings? What about changing the tab width? Font
#     size?
# A:  Yes! Hit the button at the bottom of the screen that
#     looks like a keyboard.
#
#

import logging
import requests
import traceback
import time
import pandas as pd
from datetime import timedelta, datetime, timezone
from dateutil.parser import isoparse

logging.basicConfig(
    format='%(asctime)s,%(msecs)d %(name)s [%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)
logger = logging.getLogger(__name__)
pd.options.display.max_columns = None


class Display:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print_green(text):
        logger.info(f"{Display.OKGREEN}{text}{Display.ENDC}")

    @staticmethod
    def print_red(text):
        logger.info(f"{Display.FAIL}{text}{Display.ENDC}")

    @staticmethod
    def print_blue(text):
        logger.info(f"{Display.OKBLUE}{text}{Display.ENDC}")


class MBTATransitSchedulesForStation:
    """
    Displays the Transit Schedules from the supplied base station at current time.

    As a division of the Massachusetts Department of Transportation (MassDOT),
    the MBTA provides Subway, Bus, Commuter Rail, Ferry, and Paratransit service
    to eastern Massachusetts and parts of Rhode Island.

    """

    def __init__(self, base_station_id="place-pktrm", api_endpoint='/predictions', sort='departure_time',
                 include='route'):
        """
        Default base station id is taken as Park Street Station

        """
        logger.debug("* " * 5 + "MBTA Transit Schedules For Station" + " *" * 5)
        self.base_station_id = base_station_id
        self.base_api_url = 'https://api-v3.mbta.com'
        self.current_time = None
        self.api_endpoint = api_endpoint
        self.sort = sort
        self.include = include

    def get_route_name_and_destination(self, route_id):
        response = requests.get(self.base_api_url + f'/routes/{route_id}')
        response_data = response.json()
        route_name = response_data['data']['attributes']['long_name']
        destinations = response_data['data']['attributes']['direction_destinations']
        return route_name, destinations

    def display_schedule(self, display=True):
        self.current_time = self.get_current_time_for_timezone_offset(-4)
        logger.debug(f"CURRENT TIME : {self.current_time}")
        if display:
            print('# ' * 40)
            print('#' * 15 + f" Current Time : {self.current_time} " + '#' * 15)
            print('# ' * 40)
        predicted_schedules_response = self.get_all_predicted_schedules()
        if predicted_schedules_response is not None:
            logger.debug(f"Predicted schedules API returned HTTP {predicted_schedules_response.status_code}")
            if predicted_schedules_response.status_code == 200:
                predicted_schedules = predicted_schedules_response.json()
                if predicted_schedules and predicted_schedules.get('data') and len(
                        predicted_schedules['data']) > 0:
                    # there are schedules present
                    data = predicted_schedules.get('data')
                    list_of_schedules = []
                    for d in data:
                        obj = dict()
                        obj['departure_time'] = d['attributes']['departure_time']
                        obj['direction_id'] = d['attributes']['direction_id']
                        obj['route-id'] = d['relationships']['route']['data']['id']
                        obj['vehicle-id'] = d['relationships']['vehicle']['data']['id']
                        list_of_schedules.append(obj)

                    df = pd.DataFrame.from_records(list_of_schedules)

                    # remove elements where departure time is null since these vehicles have not arrived
                    # at Park Street Station Yet
                    df = df[~df.departure_time.isna()]
                    # print(df.head(10))

                    # check for rows where the vehicle has already departed from Park Street and remove those
                    df['time_diff'] = df['departure_time'].apply(self.get_difference_with_current_in_minutes)
                    # print(df.head(10))
                    df = df[~df.time_diff.isna()]

                    # get the upcoming top 10 predictions for each route
                    sorted_by_time_df = df.groupby('route-id').min().sort_values(by='time_diff')
                    # print(sorted_by_time_df)
                    for route_id in sorted_by_time_df.index:
                        top_10_pred_for_route = df[df['route-id'] == route_id].head(10)
                        # print(top_10_pred_for_route)
                        # print('\n' + '-' * 20 + '\n')
                        route_name, destinations = self.get_route_name_and_destination(route_id)
                        if display:
                            print('\n' + '-' * 30 + route_name + '-' * 30)
                        for ind in top_10_pred_for_route.index:
                            row = df.loc[ind]
                            if display:
                                print(f'\n{destinations[row.direction_id]} : Departs in {row.time_diff} minutes '
                                      f'at {str(row.departure_time)}')
                        if display:
                            print()
                    return 200, "Successful"
                else:
                    # there is no data returned by the API
                    logger.error('No schedules present...')
                    return 200, 'No schedules present...'
            else:
                logger.error('Failed to get the API result correctly. Please verify your API url and parameters')
                logger.error(f'HTTP status code - {predicted_schedules_response.status_code}')
                logger.error(predicted_schedules_response.json())
                return predicted_schedules_response.status_code, predicted_schedules_response.json()
        else:
            logger.error("Not able to fetch all the schedules")
            return None, "Not able to fetch all the schedules"

    @staticmethod
    def get_current_time_for_timezone_offset(offset):
        return datetime.now(timezone(timedelta(hours=offset)))

    def get_vehicle(self, vehicle_id):
        response = requests.get(self.base_api_url + f'/vehicles/{vehicle_id}')
        response_data = response.json()
        vehicle_number = response_data['data']['attributes']['label']
        return vehicle_number

    def get_difference_with_current_in_minutes(self, departure_time):
        departure_time_obj = isoparse(departure_time)
        if departure_time_obj >= self.current_time:
            return round((departure_time_obj.timestamp() - self.current_time.timestamp()) / 60, 2)
        return None

    def get_all_predicted_schedules(self):
        url_params = {
            'sort': self.sort,
            'include': self.include,
            'filter[stop]': self.base_station_id
        }
        response = None
        try:
            response = requests.get(self.base_api_url + self.api_endpoint, params=url_params)
        except Exception as e:
            logger.error('Error while getting all predicted schedules')
            logger.error(traceback.format_stack())
        finally:
            return response


class MBTATransitSchedulesForStationTest:
    """
    Test the class class MBTATransitSchedulesForStation with different scenarios
    """

    def __init__(self):
        Display.print_blue('STARTING TO TEST THE APP..')
        self.positive_tests()
        self.negative_tests()
        self.performance_tests()
        Display.print_green('# ' * 20 + 'TEST FINISHED SUCCESSFULLY !!' + '#' * 20)

    def positive_tests(self):
        Display.print_green('> ' * 10 + 'Starting Positive tests..')
        self.all_correct_default_arguments()
        Display.print_green('< ' * 10 + 'All Positive tests PASSED !')

    def negative_tests(self):
        Display.print_green('> ' * 10 + 'Starting Negative tests..')
        self.wrong_base_station_id()
        self.wrong_sort_key()
        self.wrong_api_endpoint()
        Display.print_green('< ' * 10 + 'All Negative tests PASSED !')

    def performance_tests(self):
        Display.print_green('> ' * 10 + 'Starting Performance tests..')
        self.test_performance_good_scenario()
        self.test_performance_bad_scenario()
        Display.print_green('> ' * 10 + 'All Performance tests PASSED !')

    # All tests go below this
    @staticmethod
    def wrong_base_station_id():
        status_code, response = MBTATransitSchedulesForStation(base_station_id="my_wrong_id").display_schedule()
        assert status_code == 200
        assert 'No schedules present' in response

    @staticmethod
    def wrong_sort_key():
        status_code, response = MBTATransitSchedulesForStation(sort="my_wrong_sort_key").display_schedule()
        assert status_code == 400
        assert response['errors'][0]['detail'] == "Invalid sort key."

    @staticmethod
    def wrong_api_endpoint():
        status_code, response = MBTATransitSchedulesForStation(api_endpoint="/wrong").display_schedule()
        assert status_code == 404
        assert response['errors'][0]['title'] == "Resource Not Found"

    @staticmethod
    def wrong_include_key():
        status_code, response = MBTATransitSchedulesForStation(include="wrong_include").display_schedule()
        assert status_code == 404
        assert response['errors'][0]['title'] == "Resource Not Found"

    @staticmethod
    def all_correct_default_arguments():
        status_code, response = MBTATransitSchedulesForStation().display_schedule()
        assert status_code == 200
        assert response == "Successful"

    @staticmethod
    def test_performance_good_scenario():
        start_time = time.time()
        MBTATransitSchedulesForStation().display_schedule(display=False)
        diff = time.time() - start_time
        assert diff < 3, "The method took more than 3 seconds"

    @staticmethod
    def test_performance_bad_scenario():
        start_time = time.time()
        MBTATransitSchedulesForStation(sort="my_wrong_sort_key").display_schedule(display=False)
        diff = time.time() - start_time
        assert diff < 3, "The method took more than 3 seconds"


if __name__ == '__main__':
    MBTATransitSchedulesForStation().display_schedule()

    # // For testing uncomment the below line
    MBTATransitSchedulesForStationTest()
