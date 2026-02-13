class GeospatialInjector:
    def __init__(self):
        self.region_db = {
            "Erode": "High textile dye concentration in local water due to textile industries.",
            "Tuticorin": "Port activities and industrial discharge affect marine ecosystems."
        }

    def get_context(self, location):
        return self.region_db.get(
            location,
            "No specific regional environmental risk identified."
        )
