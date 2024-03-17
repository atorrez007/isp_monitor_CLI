import speedtest
import datetime
import time
import csv


def run_speed_test():
    try:
        s = speedtest.Speedtest()
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        return downspeed, upspeed
    except Exception as e:
        print("Error during speed test:", e)
        return None, None


with open("test.csv", mode="w", newline="") as speedcsv:
    csv_writer = csv.writer(speedcsv)
    csv_writer.writerow(["time", "downspeed", "upspeed"])

    while True:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed, upspeed = run_speed_test()

        if downspeed is not None and upspeed is not None:
            csv_writer.writerow([time_now, downspeed, upspeed])
            speedcsv.flush()
            print(
                f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s"
            )
        else:
            print("Speed test failed. Skipping writing to CSV.")

        time.sleep(60)
