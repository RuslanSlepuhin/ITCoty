import asyncio
import logging
import psycopg2
import asyncpg
from psycopg2.extras import DictCursor


class AsyncPGDatabase:
    def __init__(self, url):
        self.database_url = url
        self.connection = None
        self.connection_sync = None
        self.lock = asyncio.Lock()
        self.logger = logging.getLogger(__name__)

    async def connect(self):
        try:
            self.connection = await asyncpg.connect(self.database_url)
            self.logger.info("Connected to database")
            return self.connection
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error connecting to database: {e}")

    def connect_sync(self):
        try:

            self.connection_sync = psycopg2.connect(self.database_url)
            self.logger.info("Connected to database synchronously")
            return self.connection_sync
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error connecting to database synchronously: {e}")

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
                    keywords VARCHAR(500),
                    selected_notification VARCHAR(500)
                ) """
            )
            self.logger.info("Table created")
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error creating table: {e}")

    async def insert_into_data(
        self, user_id, direction, specialization, level, location, work_format, keyword, selected_notification
    ):
        if not self.connection:
            await self.connect()

        try:
            await self.connection.execute(
                "INSERT INTO user_requests (user_id, direction, specialization, level, location, work_format, keywords, selected_notification)"
                " VALUES ($1, $2, $3, $4, $5, $6, $7, $8)",
                user_id,
                direction,
                specialization,
                level,
                location,
                work_format,
                keyword,
                selected_notification
            )
            self.logger.info("Data inserted successfully")
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error inserting data: {e}")

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
                        AND (body iLIKE $4 OR body iLIKE $5) ;
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
            self.logger.error(f"Error select data: {e}")

    async def vacancy(self):
        if not self.connection:
            await self.connect()

        try:
            result = await self.connection.execute("SELECT * FROM  vacancies LIMIT 1")
            return await result.fetchall()
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error inserting data: {e}")

    async def delete_user_request(self, user_id):
        if not self.connection:
            await self.connect()

        try:
            await self.connection.execute(
                "DELETE FROM user_requests WHERE user_id = $1", user_id
            )
            self.logger.info("Data deleted successfully")
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error deleting data: {e}")

    async def get_user_request(self, user_id=None, selected_notification=None):
        if not self.connection:
            await self.connect()
        try:
            async with self.lock:
                if selected_notification is not None:
                    get_user = "SELECT * FROM user_requests WHERE selected_notification = $1;"
                    result_user_requests = await self.connection.fetch(get_user, selected_notification)
                elif user_id is not None:
                    get_user = "SELECT * FROM user_requests WHERE user_id = $1 LIMIT 1;"
                    result_user_requests = await self.connection.fetch(get_user, user_id)
                else:
                    get_user = "SELECT * FROM user_requests;"
                    result_user_requests = await self.connection.fetch(get_user)
            user_requests = [dict(row) for row in result_user_requests]
            return user_requests
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error inserting data: {e}")

    def get_periodical_task_vacancies(
        self,
        direction: str,
        specialization: str,
        level: str,
        location: str,
        work_format: str,
        keyword: str,
        interval: str,
    ):
        if not self.connection_sync:
            self.connect_sync()
        try:
            cursor = self.connection_sync.cursor(cursor_factory=DictCursor)
            query = """
                        SELECT * FROM vacancies
                        WHERE level iLIKE %s
                        AND sub iLIKE %s
                        AND job_type iLIKE %s
                        AND (body iLIKE %s OR body iLIKE %s)
                        AND created_at >= %s
                        ORDER BY created_at DESC 
                        ;
                    """

            cursor.execute(
                query,
                (level, f'%{direction}%', f'%{work_format}%', f'%{specialization}%', f'%{keyword}%', interval)
            )
            vacancies = cursor.fetchall()
            result = [dict(row) for row in vacancies]
            cursor.close()
            return result
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error inserting data: {e}")


    async def change_user_notification(self,notification, user_id):
        if not self.connection:
            await self.connect()

        try:
            await self.connection.execute(
                "UPDATE user_requests SET selected_notification = $1 WHERE user_id = $2", notification, user_id
            )
            self.logger.info("Data updated successfully")
        except asyncpg.PostgresError as e:
            self.logger.error(f"Error updating data: {e}")

