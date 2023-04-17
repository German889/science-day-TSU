import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from dtw import dtw
import json

# переменные (категориальные признаки) для Ordinal Encoding
os_values = [12, 11, 10, 9]
display_matrix_values = ['AMOLED','IPS', 'TFT']
body_material_values = ['glass','aluminium','plastic']
processor_values = ['Snapdragon 888', 'Snapdragon 855', 'Snapdragon 845', 'Exynos 990', 'Kirin 990', 'Kirin 980', 'Helio G90T', 'Helio P90', 'Snapdragon 750G', 'Helio G80', 'Snapdragon 730', 'Snapdragon 675', 'Helio P70', 'Helio G70', 'Snapdragon 660']
camera_quality_values = ['IMX766', 'IMX723', 'IMX708', 'IMX689', 'IMX686', 'IMX682', 'IMX616', 'IMX586', 'IMX582', 'IMX555', 'IMX363']
power_connector_type = ['TYPE-C', 'Micro-USB']
OTG_support = ['yes','no']
nfc_module = ['yes','no']
separate_slot_for_second_SIM_card = ['yes','no']
security_standard = ['IP68','IP67','IP00']
df = pd.read_csv('phone_data.csv')

#прочие переменные
distances = {1:11.6878}
distances.clear()
sorted_dict = {}

#dataframes
categorical_df = pd.DataFrame()
numeric_df = pd.DataFrame()
normalized_df = pd.DataFrame()
selected_device = pd.DataFrame()

def normalize_categorical_df(): #нормализация категориального dataframe
    standard_df = df[['operating system', 'type of display matrix', 'body material', 'processor', 'camera quality', 'power connector type', 'OTG support', 'NFC module', 'separate slot for second SIM card', 'security standard']]
    # Функция для сравнения значений с списком и получения индекса совпадения
    def get_index(value, values_list):
        if value in values_list:
            return values_list.index(value)
        else:
            return -1

    # Создание нового dataframe
    global categorical_df
    categorical_df = pd.DataFrame(columns=standard_df.columns)

    # Заполнение нового dataframe значениями из исходного dataframe, полученными путем сравнения с соответствующим списком
    for index, row in standard_df.iterrows():
        new_row = []
        for column in standard_df.columns:
            value = row[column]
            if column == 'operating system':
                new_row.append(get_index(value, os_values))
            elif column == 'type of display matrix':
                new_row.append(get_index(value, display_matrix_values))
            elif column == 'body material':
                new_row.append(get_index(value, body_material_values))
            elif column == 'processor':
                new_row.append(get_index(value, processor_values))
            elif column == 'camera quality':
                new_row.append(get_index(value, camera_quality_values))
            elif column == 'power connector type':
                new_row.append(get_index(value, power_connector_type))
            elif column == 'OTG support':
                new_row.append(get_index(value, OTG_support))
            elif column == 'NFC module':
                new_row.append(get_index(value, nfc_module))
            elif column == 'separate slot for second SIM card':
                new_row.append(get_index(value, separate_slot_for_second_SIM_card))
            elif column == 'security standard':
                new_row.append(get_index(value, security_standard))
            else:
                new_row.append(value)
        categorical_df.loc[len(categorical_df)] = new_row
    print("categorical_df started")

def normalize_numeric_df():
    global numeric_df
    # Определение числовых столбцов
    numeric_columns = ['screen diagonal', 'battery capacity', 'amount of RAM', 'RAM speed', 'storage capacity', 'storage speed', 'selfie camera resolution', 'bluethooth version']
    scaler = MinMaxScaler()
    # Нормализация числовых столбцов
    normalized = scaler.fit_transform(df[numeric_columns])
    # Создание нового dataframe с нормализованными значениями
    numeric_df = pd.DataFrame(normalized, columns=numeric_columns)
    print("numeric_df started")

def concat_df(): #объединение датафреймов
    # global numeric_df, categorical_df
    global normalized_df
    normalized_df = pd.concat([numeric_df,categorical_df],axis=1)
    print("dfs concatenated")

def select_device(): #желаемое пользователем устройство
    global selected_device
    selected_device = normalized_df.loc[67].values
    print("device selected")

def start_DTW():
    global sorted_dict
    i = 0
    for index, row in normalized_df.iterrows():
        device_feature = row.values
        # Вычисление DTW между y и z
        alignment = dtw(selected_device, device_feature)
        dist = alignment.distance
        distances[dist] = i
        i+=1
    print("DTW started")
    # сортировка расстояний по возрастанию
    sorted_dict = {k: distances[k] for k in sorted(distances)}


def get_devices(count):
    global sorted_dict
    detected_devices = []
    h = 0
    for key, value in sorted_dict.items():
        if(h==count): break
        detected_devices.append(value)
        h+=1
    row_dicts = []
    for i in detected_devices:
        row_dict = df.iloc[i].to_dict()
        row_dicts.append(row_dict)
    print("devices found")
    return row_dicts

def start():
    print("started")
    normalize_categorical_df()
    normalize_numeric_df()
    concat_df()
    select_device()
    start_DTW()
    devices = get_devices(4)
    return devices

start()