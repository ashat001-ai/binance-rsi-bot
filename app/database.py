import aiosqlite


class Database:

    def __init__(self, path="signals.db"):
        self.path = path

    async def init(self):
        async with aiosqlite.connect(self.path) as db:

            await db.execute("""
                CREATE TABLE IF NOT EXISTS signals(
                    symbol TEXT PRIMARY KEY,
                    rsi REAL,
                    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            await db.commit()

    async def exists(self, symbol):

        async with aiosqlite.connect(self.path) as db:

            cursor = await db.execute(
                "SELECT 1 FROM signals WHERE symbol=?",
                (symbol,)
            )

            return await cursor.fetchone() is not None

    async def save(self, symbol, rsi):

        async with aiosqlite.connect(self.path) as db:

            await db.execute(
                "INSERT OR REPLACE INTO signals(symbol,rsi) VALUES(?,?)",
                (symbol, rsi)
            )

            await db.commit()

    async def delete(self, symbol):

        async with aiosqlite.connect(self.path) as db:

            await db.execute(
                "DELETE FROM signals WHERE symbol=?",
                (symbol,)
            )

            await db.commit()
