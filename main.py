def weather():
    """This module helps in geting current weather forcast from the USA: https://weather.gov
    You can search for the weather forcast of any particular State by providing the url for that state, after you search for it on the website

    For example, type: Texas into the search box on https://weather.gov and enter
    Copy the url for the Texas page that you are on.

    The function weather() can be called without any parameter.

    """
    try:
        import pandas as pd
        import requests
        from bs4 import BeautifulSoup

        try:
            weather_url = input("Enter the URL: ")
            usweather = requests.get(weather_url)
            print("Content copied successfully")
            
            weathersoup = BeautifulSoup(usweather.content, 'html.parser')

            """Get the items in the id: 'seven-day-forecast-list' This narrows down the search. """
            extended_weather_forecast = weathersoup.find(id='seven-day-forecast-list')
            print("Successfully copied the content in: id='seven-day-forecast-list'")

            """
            To locate the general container of all the items.
            See they are all in a div, with the class 'tombstone-container'
            """
            items = extended_weather_forecast.find_all(class_ = 'tombstone-container')
            #print(items[0]) #This is the first item on the list, with index [0]

            """
            print(items[0].find(class_ = 'period-name').get_text())
            print(items[0].find(class_ = 'short-desc').get_text())
            print(items[0].find(class_ = 'temp').get_text())
            """

            """It is easier to just use List comprehension to get all the items
            #We will do that one after the otxher,
            #starting with the period name, which is the days of the week

            #period_name = [item for item in items]
            #Making it get just the text and the particular period names
            """
            period_names = [item.find(class_ = 'period-name').get_text() for item in items]
            short_descr = [item.find(class_ = 'short-desc').get_text() for item in items]
            temperature = [item.find(class_ = 'temp').get_text() for item in items]

            """Let's use pandas to prepare the content for storage or display on the computer """
            clean_weather_info = pd.DataFrame(
                {
                    'Period': period_names,
                    'Short_Descriptions': short_descr,
                    'Temperatures': temperature,
                })
            
            try:
                import os
                import re
                
                ucwd = os.path.dirname(os.path.realpath(__file__))
                """To save it as a excel file in .csv format, use any extension of your choice"""
                try:
                    clean_weather_info_file_name = input("Enter the name you want the save the information with.\nIf you do not enter a valid name, \nwe will use a 'clean_weather_info.csv' for you.\n")
                    clean_weather_info_file_name = str(clean_weather_info_file_name)

                    alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                    if (len(clean_weather_info_file_name) > 0 and clean_weather_info_file_name != '.' and clean_weather_info_file_name != '@' and clean_weather_info_file_name != '#' and clean_weather_info_file_name != '%' and clean_weather_info_file_name != '^'):
                        clean_weather_info_file_name = clean_weather_info_file_name + ".csv"
                        clean_weather_info.to_csv(clean_weather_info_file_name)
                        print(f"Your clean weather forcast information has been saved in '{clean_weather_info_file_name}'\nYou can find the file in your current workng directory.\nYour current working directory is:\n{ucwd}")
                    else:
                        clean_weather_info_file_name = 'clean_weather_info.csv'
                        clean_weather_info.to_csv(clean_weather_info_file_name)
                    print(f"Your clean weather forcast information has been saved in '{clean_weather_info_file_name}'\nYou can find the file in your current workng directory.\nYour current working directory is:\n{ucwd}")
                    
                        
                except:
                    clean_weather_info_file_name = 'clean_weather_info.csv'
                    clean_weather_info.to_csv(clean_weather_info_file_name)
                    print(f"Your clean weather forcast information has been saved in '{clean_weather_info_file_name}'\nYou can find the file in your current workng directory.\nYour current working directory is:\n{ucwd}")
                    
            except:
                print("Oops! Could not save the clean weather information as a csv file...")
            finally:
                print("The following table shows a sample of the weather information that we just saved\n\n\n")
                print(clean_weather_info)
            
        except:
            print("There was a problem completing the data mining process...")

    except:
        print("Check that you have: pandas, requests and BeautifulSoup installed.")

if __name__ == '__main__':
    weather()
