def get_long(data, min_length=5):
    new_data = data.copy()[data >= min_length]
    return new_data
