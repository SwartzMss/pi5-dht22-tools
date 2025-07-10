import argparse
from dht22_reader import DHT22Reader


def main():
    parser = argparse.ArgumentParser(description="Read DHT22 sensor on Raspberry Pi 5")
    parser.add_argument('--pin', type=int, default=4, help='GPIO pin connected to DHT22 data')
    parser.add_argument('--interval', type=float, default=2.0,
                        help='Interval between reads (seconds)')
    args = parser.parse_args()

    reader = DHT22Reader(pin=args.pin)

    for humidity, temperature in reader.loop(interval=args.interval):
        if humidity is not None and temperature is not None:
            print(f"Temp={temperature:.1f}°C  Humidity={humidity:.1f}%")
        else:
            print("Failed to retrieve data from sensor")


if __name__ == '__main__':
    main()
