def point_counter(amount_of_points_width, amount_of_points_height, pixel_density=1):
    return amount_of_points_width*amount_of_points_height*pixel_density


print(point_counter(800, 600, 1))
