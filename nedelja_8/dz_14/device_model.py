from database_connector import my_cursor


class DeviceModel:

    def __init__(self, device_model_id, model_name, model_number, water_capacity_liters, coffee_capacity_kgs,
                 milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count):
        self.device_model_id = device_model_id
        self.model_name = model_name
        self.model_number = model_number
        self.water_capacity_liters = water_capacity_liters
        self.coffee_capacity_kgs = coffee_capacity_kgs
        self.milk_capacity_kgs = milk_capacity_kgs
        self.sugar_capacity_kgs = sugar_capacity_kgs
        self.sweetener_capacity_count = sweetener_capacity_count
        self.cups_capacity_count = cups_capacity_count

    def __str__(self):
        return (f"{self.device_model_id}, {self.model_name}, {self.model_number}, {self.water_capacity_liters}, "
                f"{self.coffee_capacity_kgs}, {self.milk_capacity_kgs}, {self.sugar_capacity_kgs}, "
                f"{self.sweetener_capacity_count}, {self.cups_capacity_count}")

    @staticmethod
    def read_all_device_models_from_database():
        sql = """select device_model_id, model_name, model_number, water_capacity_liters, coffee_capacity_kgs,
                 milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count from device_model"""
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        device_models = []
        for row in result:
            device_models.append(DeviceModel(device_model_id=row[0], model_name=row[1], model_number=row[2],
                                             water_capacity_liters=row[3], coffee_capacity_kgs=row[4],
                                             milk_capacity_kgs=row[5], sugar_capacity_kgs=row[6],
                                             sweetener_capacity_count=row[7], cups_capacity_count=row[8]))
        return device_models

    @staticmethod
    def get_device_model_by_id(device_model_id):
        sql = """select device_model_id, model_name, model_number, water_capacity_liters, coffee_capacity_kgs,
                 milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count from device_model 
                 where device_model_id = (%s)"""
        val = (device_model_id,)
        my_cursor.execute(sql, val)
        result = my_cursor.fetchone()
        if result:
            return DeviceModel(device_model_id=result[0], model_name=result[1], model_number=result[2],
                               water_capacity_liters=result[3], coffee_capacity_kgs=result[4],
                               milk_capacity_kgs=result[5], sugar_capacity_kgs=result[6],
                               sweetener_capacity_count=result[7], cups_capacity_count=result[8])
        else:
            raise Exception(f"Device model with id:{device_model_id} doesn't exist in database!")

    @staticmethod
    def create_new_device_model(model_name, model_number, water_capacity_liters, coffee_capacity_kgs,
                                milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count):
        sql = """insert into device_model (model_name, model_number, water_capacity_liters, 
        coffee_capacity_kgs, milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count)
                 values ((%s), (%s), (%s), (%s), (%s), (%s), (%s), (%s))"""
        values = (model_name, model_number, water_capacity_liters, coffee_capacity_kgs,
                  milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count)
        my_cursor.execute(sql, values)

        device_model_id = my_cursor.lastrowid

        return DeviceModel(device_model_id, model_name, model_number, water_capacity_liters, coffee_capacity_kgs,
                           milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count)

    @staticmethod
    def delete_device_model_by_id(device_model_id):
        sql = "delete from device_model where device_model_id = (%s)"
        value = (device_model_id,)
        my_cursor.execute(sql, value)
        if my_cursor.rowcount == 0:
            raise Exception(f"Delete failed. Device model with provided id:{device_model_id} was not found.")
        else:
            return True

    def update_device_model(self, attributes_dict: dict):
        attribute_value_string = ""
        for attribute in attributes_dict:
            attribute_value_string += attribute + " = " + str(attributes_dict.get(attribute)) + ", "
        attribute_value_string = attribute_value_string[:-2]
        sql = "update device_model set " + attribute_value_string + f" where device_model_id = {self.device_model_id}"
        my_cursor.execute(sql)
        if my_cursor.rowcount == 0:
            raise Exception("Update failed!")
        else:
            return DeviceModel.get_device_model_by_id(self.device_model_id)
