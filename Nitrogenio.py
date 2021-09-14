import RPi.GPIO as gpio

class Nitrogenio():
    def LigaGas(self):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        gpio.setup(5, gpio.OUT)
        gpio.output(5, gpio.LOW)
        status = "LIGADO"
        return status

    def DesligaGas(self):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        gpio.setup(5, gpio.OUT)
        gpio.output(5, gpio.HIGH)
        status = "DESLIGADO"
        return status

    def VerificaStatus(self, temp, temp_ant):
        if int(float(temp)) < 50:
            status = "DESLIGADO"
        else:
            status = "LIGADO"
        # if temp > temp_ant and temp > 150:
        if int(float(temp)) > int(float(temp_ant)) and int(float(temp)) > 50:
            status = Nitrogenio().LigaGas()
        #if temp < temp_ant and temp < 350:
        if int(float(temp)) < int(float(temp_ant)) and int(float(temp)) < 100:
            status = Nitrogenio().DesligaGas()
        return status