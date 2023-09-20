import time
import re
import sys
import asyncio
from bleak import BleakScanner
from bleak import BleakClient

# This the stub created, by which host performs different operations on Device Under Test
# by selecting proper radio - Wifi or BLE
# As of now identified operations are
# 1. Scan and connect to DUT via Wifi or BLE
# 2. Close the connection with DUT
# 3. Change the operating radio mode of DUT
# 4. Get the configration parameter of Wifi Radio
# 5. Get the configuration parameter of BLE Radio
# 6. Set the configuration parameter of Wifi Radio
# 7. Set the configuration parameter of BLE Radio


async def read_temperature():
    address = "A8:42:E3:57:6D:22"
    async with BleakClient(address) as client:
        temp_value = await client.read_gatt_char("00002a6e-0000-1000-8000-00805f9b34fb")
        #print("Temparature: {0}".format("".join(map(chr, temp_value))))
        string_value = temp_value.decode('utf-8')
        #print(f"Temparature:{string_value}")
        number_match = float(string_value.split()[0])
        if number_match > 0 and number_match < 100:
            read_success = 1
        else:
            read_success = 0
        print(read_success)

async def read_humidity():
    address = "A8:42:E3:57:6D:22"
    async with BleakClient(address) as client:
        humid_value = await client.read_gatt_char("00002a6f-0000-1000-8000-00805f9b34fb")
        #print("Humidity: {0}".format("".join(map(chr, humid_value))))
        string_value = humid_value.decode('utf-8')
        #print(f"Humidity:{string_value}")
        number_match = float(string_value.split()[0])
        if number_match > 0 and number_match < 100:
            read_success = 1
        else:
            read_success = 0
        print(read_success)

async def read_pressure():
    address = "A8:42:E3:57:6D:22"
    async with BleakClient(address) as client:
        pres_value = await client.read_gatt_char("00002a6d-0000-1000-8000-00805f9b34fb")
        #print("Pressure: {0}".format("".join(map(chr, pres_value))))
        string_value = pres_value.decode('utf-8')
        #print(f"Pressure:{string_value}")
        number_match = float(string_value.split()[0])
        if number_match > 0 and number_match < 1000:
            read_success = 1
        else:
            read_success = 0
        print(read_success)


#if __name__ == '__main__':
#    actions = {'read_temperature': read_temperature,
#               'read_humidity': read_humidity,
#               'read_pressure': read_pressure}

#    action = sys.argv[1]
#    args = sys.argv[2:]
#    actions[action](*args)

async def main():
    await read_temperature()
    await read_humidity()
    await read_pressure()

if __name__ == '__main__':
    asyncio.run(main())

