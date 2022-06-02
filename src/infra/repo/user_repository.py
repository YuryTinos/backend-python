from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """Insert data into user entity
        :param  - name: User name
        :       - password: User password
        :return - tuple with new user inserted
        """

        insert_data = namedtuple("Users", "id, name, password")

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return insert_data(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

        return None
