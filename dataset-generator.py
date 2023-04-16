import random
import csv

# Создаем список возможных значений для некоторых столбцов
os_values = [12, 11, 10, 9]
display_matrix_values = ['AMOLED','IPS', 'TFT']
body_material_values = ['glass','aluminium','plastic']
processor_values = ['Snapdragon 888', 'Snapdragon 855', 'Snapdragon 845', 'Exynos 990', 'Kirin 990', 'Kirin 980', 'Helio G90T', 'Helio P90', 'Snapdragon 750G', 'Helio G80', 'Snapdragon 730', 'Snapdragon 675', 'Helio P70', 'Helio G70', 'Snapdragon 660']
camera_quality_values = ['IMX766', 'IMX723', 'IMX708', 'IMX689', 'IMX686', 'IMX682', 'IMX616', 'IMX586', 'IMX582', 'IMX555', 'IMX363']
power_connector_type = ['TYPE-C', 'Micro-USB']
OTG_support_ = ['yes', 'no']
nfc_module_ = ['yes', 'no']
separate_slot_for_second_SIM_card_ = ['yes','no']
security_standard = ['IP68','IP67','IP00']
# Функция для генерации случайного значения для каждого столбца
def generate_row(id):
    model_name = f"Phone{id}"
    os = random.choice(os_values)
    compactness_level = round(random.uniform(50, 300), 2)
    screen_diagonal = round(random.uniform(4.2, 6.8), 2)
    display_matrix = random.choice(display_matrix_values)
    screen_resolution = random.randint(500000, 3000000)
    body_material = random.choice(body_material_values)
    battery_capacity = random.randint(1900, 8000)
    processor = random.choice(processor_values)
    ram = random.choice([2, 3, 4, 6, 8])
    ram_speed = random.randint(1200, 3600)
    storage_capacity = 2 ** random.randint(4, 9)
    storage_speed = random.randint(200, 1000)
    camera_quality = random.choice(camera_quality_values)
    nfc_module = random.choice(nfc_module_)
    bluetooth_version = round(random.uniform(4.0, 5.3), 1)
    power_connector_type = random.choice(['TYPE-C', 'Micro-USB'])
    selfie_camera_resolution = random.randint(5, 32)
    otg_support = random.choice(OTG_support_)
    separate_slot_for_second_sim_card = random.choice(separate_slot_for_second_SIM_card_)
    security_standard = random.choice(['IP00','IP00','IP00','IP00','IP00','IP00','IP00','IP67', 'IP68'])

    # Возвращаем сгенерированные значения для каждого столбца в виде списка
    return [id, model_name, os, compactness_level, screen_diagonal, display_matrix, screen_resolution,
            body_material, battery_capacity, processor, ram, ram_speed, storage_capacity, storage_speed,
            camera_quality, nfc_module, bluetooth_version, power_connector_type, selfie_camera_resolution,
            otg_support, separate_slot_for_second_sim_card, security_standard]

# Создаем CSV-файл и записываем в него данные
with open('phone_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'model name', 'operating system', 'compactness level', 'screen diagonal',
                     'type of display matrix', 'screen resolution', 'body material', 'battery capacity',
                     'processor', 'amount of RAM', 'RAM speed', 'storage capacity', 'storage speed',
                     'camera quality', 'NFC module', 'bluethooth version', 'power connector type',
                     'selfie camera resolution', 'OTG support', 'separate slot for second SIM card',
                     'security standard'])

    for i in range(100):
        row = generate_row(i)
        writer.writerow(row)

print("Генерация данных для таблицы завершена!")
