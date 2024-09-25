import pandas as pd
import regex as re

# Load data
df1 = pd.read_csv('height_1_predictions.csv')
df2 = pd.read_csv('height_2_predictions.csv')
df3 = pd.read_csv('height_3_predictions.csv')
df4 = pd.read_csv('height_4_predictions.csv')
df5 = pd.read_csv('height_5_predictions.csv')


df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

df['regex_1'] = ''
predictions = df['prediction'].tolist()

# Length unit mapping (full forms and their abbreviations)
length_units = {
  'centimetre': ['cm', 'centimeter', 'centimetre'],
  'foot': ['ft', 'foot', 'feet'],
  'inch': ['in', 'inch', 'inches'],
  'metre': ['m', 'meter', 'metre'],
  'millimetre': ['mm', 'millimeter', 'millimetre'],
  'yard': ['yd', 'yard']
}

# Map to standard unit names
length_unit_map = {
  'cm': 'centimetre', 'centimeter': 'centimetre', 'centimetre': 'centimetre',
  'ft': 'foot', 'foot': 'foot', 'feet': 'foot',
  'in': 'inch', 'inch': 'inch', 'inches': 'inch',
  'm': 'metre', 'meter': 'metre', 'metre': 'metre',
  'mm': 'millimetre', 'millimeter': 'millimetre', 'millimetre': 'millimetre',
  'yd': 'yard', 'yard': 'yard'
}

# Regular expression to match all length units
length_units_pattern = r'(?i)(cm|centimeter|centimetre|ft|foot|feet|in|inch|inches|m|meter|metre|mm|millimeter|millimetre|yd|yard)'

def split_by_numbers(predic):
  # Regular expression to match integers, floats, and fractions
  try:
    split_list = re.split(r'(\d+(?:\.\d+)?(?:/\d+)?)', predic)
  except:
    temp_predic = str(predic)
    split_list = re.split(r'(\d+(?:\.\d+)?(?:/\d+)?)', temp_predic)

  result = []
  # Iterate over the split list, combining number and non-numeric part
  for i in range(1, len(split_list), 2):
    if i+1 < len(split_list):
      result.append(split_list[i] + split_list[i+1])
    else:
      # If there's no following non-numeric part, just append the number
      result.append(split_list[i])

  return result

def extract_magnitude_and_unit(split_str):
  poss_val = []
  for element in split_str:
    # Match numeric values and length units in the string
    match = re.search(r'(\d+(?:\.\d+)?(?:/\d+)?)\s*' + length_units_pattern, element)
    if match:
      magnitude = match.group(1)
      unit = match.group(2).lower()

      # Normalize the unit to the standard form using the map
      normalized_unit = length_unit_map.get(unit, None)
      if normalized_unit:
        poss_val.append(f"{magnitude} {normalized_unit}")

  return poss_val

non_empty = 0
empty = 0
for i, predic in enumerate(predictions):
  split_str = split_by_numbers(predic)
  split_str = [ele.strip() for ele in split_str if ele.strip()]

  poss_val = extract_magnitude_and_unit(split_str)

  if poss_val:
    df.at[i, 'regex_1'] = poss_val[0]
    non_empty += 1
  else:
    df.at[i, 'regex_1'] = ""
    empty += 1

print(df)

print(f"Non-empty: {non_empty}, Empty: {empty}")
df.to_csv('height_regex.csv', index=False)
