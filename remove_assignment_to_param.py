"""Remove assignment to method parameter."""
# By Kami Bigdely

class Distance:
    """distance units and value"""
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_light(self):
        """convert from light-year to km unit"""
        if self.unit != 'km':
            # [ly] stands for light-year (measure of distance in astronomy)
            if self.unit == "ly":
                in_km = self.value * 9.461e12
            self.value = in_km
            self.unit = "km"
        else:
            print ("unit is Unknown")
            return


class Mass:
    """mass units and value"""
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def time_density(self, distance, time):
        """convert from solar mass to kg"""
        speed = distance.value/time # [km per sec]
        if mass.unit != 'kg':
            if mass.unit == "solar-mass":
                self.value = mass.value * 1.98892e30 # [kg]
                self.unit = 'kg'
        else:
            print ("unit is Unknown")
            return


def calculate_kinetic_energy(mass, distance, time):
    """astronomy equation that returns int"""
    distance.to_light()
    mass.time_density(distance, time)

    kinetic_energy = 0.5 * mass.value * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))
