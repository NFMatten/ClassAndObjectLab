from alarm_clock import AlarmClock

# String for times

alarm_one = AlarmClock()
alarm_one.set_current_time("12:00")
alarm_one.set_alarm_time("12:30")
alarm_one.toggle_alarm("on")
print(alarm_one.display_alarm_clock())

alarm_two = AlarmClock()
alarm_two.set_current_time("1:48 pm")
alarm_two.set_alarm_time("3:00 am")
alarm_two.toggle_alarm("off")
print(alarm_two.display_alarm_clock())