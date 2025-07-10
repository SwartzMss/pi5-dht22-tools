import time
import Adafruit_DHT


class DHT22Reader:
    """Helper class to read DHT22 sensor data."""

    def __init__(self, pin: int = 4):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = pin

    def read(self):
        """Return a tuple ``(humidity, temperature)`` from the sensor."""
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return humidity, temperature

    def loop(self, interval: float = 2.0):
        """Yield sensor readings continuously every ``interval`` seconds."""
        while True:
            yield self.read()
            time.sleep(interval)

