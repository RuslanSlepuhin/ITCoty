import logging

import asyncpg


class AsyncPGDatabase:
    def __init__(self, url):
        self.database_url = url
        self.connection = None
        self.logger = logging.getLogger(__name__)

    async def connect(self):
        try:
            self.connection = await asyncpg.connect(self.database_url)
            self.logger.info("Connected to database")
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error connecting to database: {e}")

    async def disconnect(self):
        if self.connection:
            await self.connection.close()
            self.logger.info("Disconnected from database")

    async def create_db(self) -> None:
        try:
            if not self.connection:
                await self.connect()
            await self.connection.execute("CREATE DATABASE IF NOT EXISTS user_request")
            self.logger.info("Database created")
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error creating database: {e}")

    async def create_table(self) -> None:
        try:
            if not self.connection:
                await self.connect()
            await self.connection.execute(
                """CREATE TABLE IF NOT EXISTS user_requests
                (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT,
                    direction VARCHAR(255),
                    specialization VARCHAR(500),
                    level VARCHAR(500),
                    location VARCHAR(500),
                    work_format VARCHAR(500),
                    keywords VARCHAR(500)
                ) """
            )
            self.logger.info("Table created")
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error creating table: {e}")

    async def insert_into_data(
        self, user_id, direction, specialization, level, location, work_format, keyword
    ):
        if not self.connection:
            await self.connect()

        try:
            await self.connection.execute(
                "INSERT INTO user_requests (user_id, direction, specialization, level, location, work_format, keywords)"
                " VALUES ($1, $2, $3, $4, $5, $6, $7)",
                user_id,
                direction,
                specialization,
                level,
                location,
                work_format,
                keyword,
            )
            logging.info("Data inserted successfully")
        except asyncpg.PostgresError as e:
            logging.error(f"Error inserting data: {e}")

    async def receive_vacancy(
        self,
        direction: str,
        specialization: str,
        level: str,
        location: str,
        work_format: str,
        keyword: str,
    ):
        if not self.connection:
            await self.connect()

        try:
            query = """
                        SELECT * FROM vacancies
                        WHERE profession iLIKE $1
                        AND profession iLIKE $2
                        AND job_type iLIKE $3
                        AND (body iLIKE $4 OR body iLIKE $5); 
                    """
            vacancies = await self.connection.fetch(
                query,
                f"%{level}%",
                f"%{direction}%",
                f"%{work_format}%",
                f"%{specialization}%",
                f"%{keyword}%",
            )
            result = [dict(row) for row in vacancies]
            return result
        except asyncpg.PostgresError as e:
            logging.error(f"Error select data: {e}")

    async def vacancy(self):
        if not self.connection:
            await self.connect()

        try:
            result = await self.connection.execute("SELECT * FROM  vacancies LIMIT 1")
            return await result.fetchall()
        except asyncpg.PostgresError as e:
            logging.error(f"Error inserting data: {e}")

    async def delete_user_request(self, user_id):
        if not self.connection:
            await self.connect()

        try:
            await self.connection.execute(
                f"DELETE FROM user_requests WHERE user_id = $1", user_id
            )
            logging.info("Data deleted successfully")
        except asyncpg.PostgresError as e:
            logging.error(f"Error deleting data: {e}")

    async def get_user_request(self):
        if not self.connection:
            await self.connect()
        try:
            get_user = """SELECT *
                FROM user_requests ;"""
            result_user_requests = await self.connection.fetch(get_user)
            user_requests = [dict(row) for row in result_user_requests]
            return user_requests
        except asyncpg.PostgresError as e:
            logging.error(f"Error inserting data: {e}")

    async def get_periodical_task_vacancies(self,
        direction: str,
        specialization: str,
        level: str,
        location: str,
        work_format: str,
        keyword: str,):
        if not self.connection:
            await self.connect()
        try:
            query = """
                                     SELECT * FROM vacancies
                                     WHERE level iLIKE $1
                                     AND sub iLIKE $2
                                     AND job_type iLIKE $3
                                     AND (body iLIKE $4 OR body iLIKE $5)
                                     AND created_at >= NOW() - interval '30 minute'
                                     ORDER BY created_at DESC;   
                                 """
            vacancies = await self.connection.fetch(
                query,
                f"%{level}%",
                f"%{direction}%",
                f"%{work_format}%",
                f"%{specialization}%",
                f"%{keyword}%",
            )

            if vacancies:
                result = [dict(row) for row in vacancies]
                return result
        except asyncpg.PostgresError as e:
            logging.error(f"Error inserting data: {e}")
