import warnings
...
ledGPIO = 47
...
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    led = LED(ledGPIO)
