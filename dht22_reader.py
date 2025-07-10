import time
import board
import adafruit_dht


class DHT22Reader:
    """Helper class to read DHT22 sensor data."""

    def __init__(self, pin: int = 4):
        board_pin = getattr(board, f"D{pin}")
        self.sensor = adafruit_dht.DHT22(board_pin)

    def read(self):
        """Return a tuple ``(humidity, temperature)`` from the sensor."""
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity
            if temperature is None or humidity is None:
                raise RuntimeError("Sensor returned None")
            return humidity, temperature
        except RuntimeError:
            return None, None

    def loop(self, interval: float = 2.0):
        """Yield sensor readings continuously every ``interval`` seconds."""
        while True:
            yield self.read()
            time.sleep(interval)

    def exit(self):
        """Release sensor resources."""
        try:
            self.sensor.exit()
        except AttributeError:
            pass

