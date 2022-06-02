# pylint: disable=E1111

from faker import Faker

from src.infra.entities import Pet as PetModel
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.pet import AnimalTypes
from .pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection_handle = DBConnectionHandler()


def test_insert_pet():
    """Should Insert pet"""

    name = faker.name()
    species = "dog"
    age = faker.random_number(digits=2)
    user_id = faker.random_number()

    engine = db_connection_handle.get_engine()

    # SQL Commands
    new_pet = pet_repository.insert_pet(name, species, age, user_id)
    query_pet = engine.execute(f"SELECT * FROM pets WHERE id='{new_pet.id}'").fetchone()

    engine.execute(f"DELETE FROM pets WHERE id='{new_pet.id}'")

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.species == query_pet.species
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id


def test_select_pet():
    """Should Select a pet in pets table and comapare it"""

    pet_id = faker.random_number(digits=5)
    name = faker.name()
    species = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    species_mock = AnimalTypes("fish")
    data = PetModel(
        id=pet_id, name=name, species=species_mock, age=age, user_id=user_id
    )

    engine = db_connection_handle.get_engine()
    engine.execute(
        "INSERT INTO pets (id, name, species, age, user_id) "
        + f"VALUES ('{pet_id}', '{name}', '{species}', '{age}', '{user_id}')"
    )

    query_pet1 = pet_repository.select_pet(pet_id=pet_id)
    query_pet2 = pet_repository.select_pet(user_id=user_id)
    query_pet3 = pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

    assert data in query_pet1
    assert data in query_pet2
    assert data in query_pet3

    engine.execute(f"DELETE FROM pets WHERE id='{pet_id}'")
