import settings

def height_prct(percentage: int | float):
    return int((settings.HEIGHT / 100) * percentage)

def width_prct(percentage: int | float):
    return int((settings.WIDTH / 100) * percentage)


# print(height_prct(25))