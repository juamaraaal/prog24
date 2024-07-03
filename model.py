from config import *

class Cabelo(db.Entity):
    tipo = Required(str)
    corte = Required(str)
    cor = Required(str)
    idade = Required(str)
    comprimento = Required(str)
    def __str__(self):
        return f'{self.tipo}, {self.corte}, {self.cor}, {self.idade}, {self.comprimento}'

db.bind(provider='sqlite', filename='cabelo.db', create_db=True)
db.generate_mapping(create_tables=True)