from chevyvolt import ChevyVolt
from fordfusion import FordFusion
from jeepsahara import JeepSahara
from nullcar import NullCar

def getCar(carname):
    if carname == 'Chevy':
        return ChevyVolt()
    elif carname == 'Ford':
        return FordFusion()
    elif carname == 'Jeep':
        return JeepSahara()
    else:
        return NullCar(carname)

for carname in 'Chevy', 'Ford', 'Jeep', 'Tesla':
    car = getCar(carname)
    car.start()
    car.stop()