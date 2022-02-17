import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        pass


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        pass


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        pass


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as f:
        reader = csv.reader(f, delimiter=';')
        headers = next(reader)
        count = len(headers)
        vals = ["" for i in range(10)]
        auto_dict = dict(zip(headers, vals))

        print(auto_dict)
        for row in reader:
            if row and row[0]:
                auto_dict = dict(zip(headers, row))
            print(auto_dict)
            pass
        


    return car_list



if __name__ == "__main__":
    file_path = "d:/programs/b81py/b11032deep/"

    get_car_list(file_path + "cars_week3.csv")

    print(5555)

