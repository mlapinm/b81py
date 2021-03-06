import csv
import re

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.car_type = None
        self.get_photo_file_ext()
        pass

    def get_photo_file_ext(self):
        ext = re.sub(r'.+(\..+)$', r'\1', self.photo_file_name)
        return ext


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)
        pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl = body_whl
        whl = self.body_whl.split('x')
        self.body_width = 0.0
        self.body_height = 0.0
        self.body_length = 0.0
        try:
            if len(whl) != 3:
                raise ValueError()
            whl = [float(e) for e in whl]
            self.body_length = whl[0]
            self.body_width = whl[1]
            self.body_height = whl[2]
        except Exception as ex:
            pass

    def get_body_volume(self):
        v = 1
        for a in (self.body_width, self.body_height, self.body_length):
            v *= a
        return v

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra
        pass

def get_photo_file_ext(name):
    ext = re.sub(r'\w+(\..+)$', r'\1', name)
    if ext == name:
        ext = ''
    return ext


def get_car_list(csv_filename):
    car_list = []
    autos = []

    reader = []

    try:
        f = open(csv_filename)
        reader = csv.reader(f, delimiter=';')
        headers = next(reader)
            
    except Exception as exc:
        return []
        pass

    for row in reader:
        vehicle = None

        try:
            if ''.join(row).strip() == '':
                raise ValueError
            auto = dict(zip(headers, row))
            autos.append(auto)
            if not 'car_type' in auto:
                raise ValueError
            if auto['car_type'].strip() == '' or auto['brand'].strip() == '' or auto['photo_file_name'].strip() == '' or auto['carrying'].strip() == '':
                raise ValueError
            exts = ['.jpg', '.jpeg', '.png', '.gif']    
            if not get_photo_file_ext(auto['photo_file_name']) in exts:
                raise ValueError

            if auto['car_type'] == 'car' and auto['passenger_seats_count'].strip() != '':
                vehicle = Car( auto['brand'], auto['photo_file_name'], auto['carrying'], auto['passenger_seats_count'] )
            if auto['car_type'] == 'truck':
                vehicle = Truck( auto['brand'], auto['photo_file_name'], auto['carrying'], auto['body_whl'] )
            if auto['car_type'] == 'spec_machine'and auto['extra'].strip() != '':
                vehicle = SpecMachine( auto['brand'], auto['photo_file_name'], auto['carrying'], auto['extra'] )

            vehicle and car_list.append(vehicle)

        except Exception as exc:
            continue
    return car_list



if __name__ == "__main__":

    car = Truck('Nissan', '1.jpg', '2.5', '0x0x0x0')
    print(car, car.body_width,
    car.get_photo_file_ext())

    file_path = "./b81py/b11032deep/"

    spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
    print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
    ext = spec_machine.get_photo_file_ext()
    print(ext)

    cars = get_car_list(file_path + "cars_week3.csv")
    for car in cars:
        car and print(type(car), car.brand)

    print(cars, len(cars))
    v = cars[1].get_body_volume()
    print(v, len(cars))
    print(get_photo_file_ext('.jpg'))



