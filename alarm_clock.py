
'''
As a developer, I want to use Python’s proper snake_case for variable names.
As a developer, I want to create an AlarmClock class (alarm_clock.py).

As a developer, I want the AlarmClock class to have class variables to keep track of the AlarmClock’s current time, whether the alarm is on or off, and the time the alarm is set to. 
NOTE: You can use arbitrary strings to represent the time, it does not need to be accurate or change over time

As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.
As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off. 
As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.

As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

Print the clock’s time to the terminal
Call the alarm clock’s change time method to change the time
Toggle the alarm clock’s on off switch

'''



class AlarmClock:
    def __init__(self):
        self.current_time = "" # current time
        self.alarm_time = "" # Set time for alarm
        self.alarm_status = "" # on or off

    def set_current_time(self, time):
        self.current_time = time

    def toggle_alarm(self, alarm_on_or_off):
        self.alarm_status = alarm_on_or_off

    def set_alarm_time(self, alarm_time):
        self.alarm_time = alarm_time

    def display_alarm_clock(self):
        display = f'''
        Current time: {self.current_time}
        Alarm set to: {self.alarm_time}
        Alarm is currently turned {self.alarm_status}
        '''
        return display