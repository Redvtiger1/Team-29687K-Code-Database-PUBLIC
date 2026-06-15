def battery_alert():

    while True:
        # Check battery and alert driver
        if brain.battery.capacity() < 40:
            controller_1.rumble(". .")
            # 20 second delay so it doesn't distract the driver too often
            wait(20, SECONDS)



            wait(20, MSEC) # Prevent CPU hogging

battery_thread = Thread(battery_alert)
