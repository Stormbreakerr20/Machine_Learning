entity_unit_map = {
    "width": {"centimetre", "foot", "millimetre", "metre", "inch", "yard"},
    "depth": {"centimetre", "foot", "millimetre", "metre", "inch", "yard"},
    "height": {"centimetre", "foot", "millimetre", "metre", "inch", "yard"},
    "item_weight": {
        "milligram",
        "kilogram",
        "microgram",
        "gram",
        "ounce",
        "ton",
        "pound",
    },
    "maximum_weight_recommendation": {
        "milligram",
        "kilogram",
        "microgram",
        "gram",
        "ounce",
        "ton",
        "pound",
    },
    "voltage": {"millivolt", "kilovolt", "volt"},
    "wattage": {"kilowatt", "watt"},
    "item_volume": {
        "cubic foot",
        "microlitre",
        "cup",
        "fluid ounce",
        "centilitre",
        "imperial gallon",
        "pint",
        "decilitre",
        "litre",
        "millilitre",
        "quart",
        "cubic inch",
        "gallon",
    },
}

all_entity_units = set()
for entity, units in entity_unit_map.items():
    all_entity_units.update(units)
all_entity_units = sorted(all_entity_units)
