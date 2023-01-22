from device_model import DeviceModel

if __name__ == "__main__":
    # Zadatak 1
    device_models = DeviceModel.read_all_device_models_from_database()
    for device_model in device_models:
        print(device_model)

    # Zadatak 2
    try:
        device_model = DeviceModel.get_device_model_by_id(2)
        print(device_model)
    except Exception as e:
        print(e)

    # Zadatak 3
    try:
        device_model = DeviceModel.create_new_device_model("New model name", "new model number", 4, 6, 5.5, 7, 600, 700)
        print(device_model)
    except Exception as e:
        print(e)

    # Zadatak 4
    try:
        if DeviceModel.delete_device_model_by_id(14):
            print("Device model deleted")
    except Exception as e:
        print(e)

    # Zadatak 5
    try:
        device_model = DeviceModel.get_device_model_by_id(2)
        print(device_model)
        device_model = device_model.update_device_model({"water_capacity_liters": 7, "coffee_capacity_kgs": 12})
        print(device_model)
    except Exception as e:
        print(e)
