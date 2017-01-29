import time
import sensor_api
import yeelink_config
import yeelink_api

_DEBUG_ = False

MYID = 1
yeelink_config.init(MYID)

serial_name_0 = "/dev/ttyS0"
sensor_api.init(serial_name_0)

while True:
    value_pm25 = sensor_api.read_pm25()
    if Ud > 0:
        print "pm2.5 :", Ud
        if not _DEBUG_:
            yeelink_api.send_value(yeelink_config.device_id(), yeelink_config.sensor_pm25_id(), value_pm25)

    value_CO = sensor_api.read_CO()
    if value_CO > 0:
        print "CO :", value_CO
        if not _DEBUG_:
            yeelink_api.send_value(yeelink_config.device_id(), yeelink_config.sensor_CO_id(), value_CO)

    value_SO2 = sensor_api.read_SO2()
    if value_SO2 > 0:
        print "SO2 :", value_SO2
        if not _DEBUG_:
            yeelink_api.send_value(yeelink_config.device_id(), yeelink_config.sensor_SO2_id(), value_SO2)



            # print "sleep"
time.sleep(15)
