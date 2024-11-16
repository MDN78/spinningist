import dataclasses


@dataclasses.dataclass
class User:
    name: str
    email: str
    phone: str
    street: str
    house: str
    additional_information: str


alex = User(
    name='Evlampy',
    email='test@yandex.ru',
    phone='9253343434',
    street='Lermontova',
    house='12',
    additional_information="Delivery after 12 o'clock",
)
