import aiosqlite
import logging

DB_NAME = "bot_database.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS broadcast_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                audience TEXT NOT NULL,
                media_file_id TEXT,
                media_type TEXT,
                caption TEXT,
                status TEXT DEFAULT 'running',
                offset INTEGER DEFAULT 0,
                total INTEGER DEFAULT 0,
                source TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.commit()

async def add_user(user_id: int, username: str):
    async with aiosqlite.connect(DB_NAME) as db:
        try:
            await db.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
            await db.commit()
        except Exception as e:
            logging.error(f"Error adding user: {e}")

async def get_users_count():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else 0

async def get_all_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT user_id FROM users ORDER BY user_id") as cursor:
            return await cursor.fetchall()

async def create_broadcast_job(audience: str, media_file_id: str | None, media_type: str | None, caption: str | None, total: int, source: str | None) -> int:
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("""
            INSERT INTO broadcast_jobs (audience, media_file_id, media_type, caption, status, offset, total, source)
            VALUES (?, ?, ?, ?, 'running', 0, ?, ?)
        """, (audience, media_file_id, media_type, caption, total, source))
        await db.commit()
        return cursor.lastrowid

async def get_running_job():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("""
            SELECT id, audience, media_file_id, media_type, caption, status, offset, total, source
            FROM broadcast_jobs
            WHERE status = 'running'
            ORDER BY id DESC
            LIMIT 1
        """) as cursor:
            return await cursor.fetchone()

async def get_job(job_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("""
            SELECT id, audience, media_file_id, media_type, caption, status, offset, total, source
            FROM broadcast_jobs WHERE id = ?
        """, (job_id,)) as cursor:
            return await cursor.fetchone()

async def update_job_progress(job_id: int, offset: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            UPDATE broadcast_jobs
            SET offset = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (offset, job_id))
        await db.commit()

async def set_job_status(job_id: int, status: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            UPDATE broadcast_jobs
            SET status = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (status, job_id))
        await db.commit()

async def get_job_status(job_id: int) -> str | None:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT status FROM broadcast_jobs WHERE id = ?", (job_id,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else None

async def stop_jobs_by_audience(audience: str) -> int:
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "UPDATE broadcast_jobs SET status = 'stopped', updated_at = CURRENT_TIMESTAMP WHERE status = 'running' AND audience = ?",
            (audience,)
        )
        await db.commit()
        return cursor.rowcount
