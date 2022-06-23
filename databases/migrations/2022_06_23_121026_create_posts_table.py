"""CreatePostsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("posts") as table:
            table.increments("id")
            table.unsigned_integer("user_id")
            table.string("body").comment("本文")
            table.tiny_integer("is_show").default(True).comment("表示/非表示")

            table.soft_deletes()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("posts")
