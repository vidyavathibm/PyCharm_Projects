class Temperature:
    def convertFahrenheit(self,celsius):
        fah=(celsius*1.8)+32
        print('%0.1f degree celsius is equal to %0.1f degree fahrenheit' %(celsius,fah))

    def convertCelsius(self,fahreinheit):
        cels=(fahreinheit-32)/1.8
        print('%0.1f degree fahreinheit is equal to %0.1f degree celsius' %(fahreinheit,cels))

t=Temperature()
t.convertCelsius(71.6)
t.convertFahrenheit(22)