from alarm_clock import AlarmClock

# String for times

alarm_one = AlarmClock()
alarm_one.set_current_time("12:00")
alarm_one.set_alarm_time("12:30")
alarm_one.toggle_alarm("On")
print(alarm_one.display_alarm_clock())