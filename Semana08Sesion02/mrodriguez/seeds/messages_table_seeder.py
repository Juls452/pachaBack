from orator.seeds import Seeder


class MessagesTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        # identificando usuarios
        twittor = self.db.table("users").where("name", "twittor").first()
        john = self.db.table("users").where("name", "john").first()
        jane = self.db.table("users").where("name", "jane").first()

        # pasando mensaje a cada usuario por user_id
        self.db.table("messages").insert(
            {"content": "Twittor's message.", "user_id": twittor["id"]}
        )

        self.db.table("messages").insert(
            {"content": "John's message.", "user_id": john["id"]}
        )

        self.db.table("messages").insert(
            {"content": "Jane's message.", "user_id": jane["id"]}
        )
