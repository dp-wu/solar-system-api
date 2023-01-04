from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    size = db.Column(db.Integer)
    distance_from_earth = db.Column(db.Integer)
    
    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["size"] = self.size
        planet_as_dict["distance_from_earth"] = self.distance_from_earth

        return planet_as_dict
    
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                        description=planet_data["description"],
                        size=planet_data["size"],
                        distance_from_earth=["distance_from_earth"]
                    )
        return planet_data