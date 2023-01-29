from device_models.services import DeviceModelsService
from device_models.models.schemas import DeviceModelSchema
from beverages.services import BeverageServices
from fastapi import HTTPException


class DeviceModelsController:

    @staticmethod
    def get_all_device_models():
        all_device_models = DeviceModelsService.get_all_device_models()
        all_device_schemas = []
        for device in all_device_models:
            all_device_schemas.append(DeviceModelSchema(**device.__dict__))
        return all_device_schemas

    @staticmethod
    def get_device_model_by_id(device_model_id: int):
        return DeviceModelsService.get_device_model_by_id(device_model_id)

    @staticmethod
    def create_device_model(model_name: str, model_number: str, water_capacity_liters: float,
                            coffee_capacity_kgs: float, milk_capacity_kgs: float, sugar_capacity_kgs: float,
                            sweetener_capacity_count: int, cups_capacity_count: int):

        return DeviceModelsService.create_device_model(model_name, model_number, water_capacity_liters,
                                                       coffee_capacity_kgs, milk_capacity_kgs, sugar_capacity_kgs,
                                                       sweetener_capacity_count, cups_capacity_count)

    @staticmethod
    def delete_device_model(device_model_id: int):
        try:
            DeviceModelsService.delete_device_model(device_model_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_device_model(attributes_dict: dict, device_model_id: int):
        return DeviceModelsService.update_device_model(attributes_dict, device_model_id)

    @staticmethod
    def add_new_beverage_to_device_model(device_model_id: int, beverage_id: int):
        try:
            device_model = DeviceModelsService.get_device_model_by_id(device_model_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Device model with this id does not exist")

        try:
            beverage = BeverageServices.get_beverage_by_id(beverage_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Beverage with this id does not exist")

        try:
            beverage_ids = DeviceModelsService.get_all_beverages_ids_for_device_model(device_model_id)
            for bev_id in beverage_ids:
                if bev_id.beverage_id == beverage_id:
                    raise HTTPException(status_code=400, detail="Device already has that beverage")
            flag = DeviceModelsService.add_new_beverage_to_device_model(device_model_id, beverage_id)
            if flag:
                return True
            else:
                raise HTTPException(status_code=500, detail="Database error")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Unknown error")


    @staticmethod
    def device_model_with_list_of_beverages(device_model_id: int):
        try:
            device_model = DeviceModelsService.get_device_model_by_id(device_model_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Device model with this id does not exist")

        try:
            beverage_ids = DeviceModelsService.get_all_beverages_ids_for_device_model(device_model_id)
            # print(beverage_ids)
            beverages = []
            for beverage in beverage_ids:
                beverages.append(BeverageServices.get_beverage_by_id(beverage.beverage_id))
                # print(beverage.beverage_id)
            device_model.beverages = beverages
            return device_model
        except Exception as e:
            raise HTTPException(status_code=500, detail="Unknown error")


    @staticmethod
    def delete_beverage_from_device_model(device_model_id: int, beverage_id: int):
        try:
            device_model = DeviceModelsService.get_device_model_by_id(device_model_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Device model with this id does not exist")

        try:
            beverage = BeverageServices.get_beverage_by_id(beverage_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Beverage with this id does not exist")
        try:
            device_model_beverages = DeviceModelsService.get_all_beverages_ids_for_device_model(device_model_id)
            device_model_beverages_ids = []
            for device_model_beverage in device_model_beverages:
                device_model_beverages_ids.append(device_model_beverage.beverage_id)
            if beverage_id not in device_model_beverages_ids:
                raise HTTPException(status_code=400, detail="Device model doesn't have this beverage")

            print(device_model_beverages_ids)
            DeviceModelsService.delete_beverage_from_device_model(device_model_id, beverage_id)
        except Exception as e:
            raise e
