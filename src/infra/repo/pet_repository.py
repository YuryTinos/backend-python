from typing import List
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pet
from src.infra.entities import Pet as PetModel
from src.infra.config import DBConnectionHandler


class PetRepository(PetRepositoryInterface):
    """Class to manage Pet Repository"""

    @classmethod
    def insert_pet(cls, name: str, species: str, age: int, user_id: int) -> Pet:
        """Insert data in pets Entity
        :param  - name: name of the pet
                - species: Enum with species accepted
                - age: pet age
                - user_id: id of the owner
        :return - tuple with new pet inserted
        """

        try:

            with DBConnectionHandler() as db_connection:
                new_pet = PetModel(name=name, species=species, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pet(
                    id=new_pet.id,
                    name=new_pet.name,
                    species=new_pet.species.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pet]:
        """Select data in Pet entity by id and/or user_id
        :param  - pet_id: Id of the pet
                - user_id: Id pf the Owner
        :return - List of selected Pets
        """

        try:
            query_data = None

            if pet_id and not user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetModel).filter_by(id=pet_id).one()
                    )
                    query_data = [data]

            elif not pet_id and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetModel).filter_by(user_id=user_id)
                    ).all()
                    query_data = data

            elif pet_id and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetModel)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
