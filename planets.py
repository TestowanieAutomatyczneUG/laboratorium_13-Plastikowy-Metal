class Planets:
    def new_age(self, age, planet):
        earth = 31557600
        all_planets = {
            "Ziemia": 1,
            "Merkury": 0.2408467,
            "Wenus": 0.61519726,
            "Mars": 1.8808158,
            "Jowisz": 11.862615,
            "Saturn": 29.447498,
            "Uran": 84.016846,
            "Neptun": 164.79132
        }

        if type(age) == int and type(planet) == str:
            if age > 0 and (planet in all_planets):
                x = age / (all_planets[planet] * earth)
                return round(x, 2)
            else:
                raise Exception("Error in program")
        else:
            raise Exception("Error in program")

x = Planets()
print(x.new_age(662256000, "Wenus"))