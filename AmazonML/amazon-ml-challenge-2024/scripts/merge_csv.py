import pandas as pd

voltage = "voltage_regex.csv"
wattage = "wattage_regex.csv"
depth = "depth_regex.csv"
height = "height_regex.csv"
width = "width_regex.csv"
weight = "weight_regex.csv"
max_weight = "max_weight_regex.csv"
volume ="volume_regex.csv"

df_voltage = pd.read_csv(voltage)
df_wattage = pd.read_csv(wattage)
df_depth = pd.read_csv(depth)
df_height = pd.read_csv(height)
df_width = pd.read_csv(width)
df_weight = pd.read_csv(weight)
df_max_weight = pd.read_csv(max_weight)
df_volume = pd.read_csv(volume)


merged_df = pd.concat([df_depth, df_height, df_width, df_weight,
                       df_max_weight, df_volume, df_voltage, df_wattage],
                      axis=0, ignore_index=True)


# print(merged_df)
sorted_df = merged_df.sort_values(by='index')

new_df = sorted_df[['index', 'regex_1']]

new_df = new_df.rename(columns={'regex_1': 'prediction'})
# print(new_df)

# new_df.to_csv('final_merged.csv', index=False)

final_df = new_df
# test_df = pd.read_csv('test.csv')

# Check if the DataFrames have the same number of rows
# if final_df.shape[0] != test_df.shape[0]:
#     print("DataFrames have different numbers of rows. Final:", final_df.shape[0], "Test:", test_df.shape[0])

# print("Final DataFrame:")
# print(final_df)

duplicated_indices = final_df[final_df['index'].duplicated(keep=False)]

print("Rows with duplicated index values:")
print(duplicated_indices)

final_df = final_df.drop(96514)
print(final_df)
final_df.to_csv('try1.csv', index=False)