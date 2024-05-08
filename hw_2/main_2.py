class Patient:

    full_name: str
    age: int
    disease: str

    def __init__(self, full_name: str, age: int, disease: str):
        self.full_name = full_name
        self.age = age
        self.disease = disease

    def make_an_appointment(self):
        pass

    def print_info(self):
        pass