area = 2000
thickness = 150
porosity = 0.15
water_saturation = 0.3
formation_vol_factor = 1.65

oip = 7758 * area * thickness * porosity * (1 - water_saturation)

print('Oil originally in place = {:.2f} MMbbl'.format(oip/1e6))
