from discord.ext import commands
from utils.board_img_handler import delete_png
from utils.engine_logic import ChessGameWithEngine


def is_active_player():
    async def predicate(ctx):
        return ctx.author.id in ctx.cog.active_games

    return commands.check(predicate)


class ChessEngineGame(commands.Cog, name="Chess Engine Game"):
    def __init__(self, bot):
        self.bot = bot
        self.active_games = {}  # Dictionary to track active chess games by user ID

    @commands.command()
    async def chess(self, ctx):
        # Command to start a new chess game
        if ctx.author.id not in self.active_games:
            self.active_games[ctx.author.id] = ChessGameWithEngine(10, ctx.author.id)
            self.active_games[ctx.author.id].start_game()
            await ctx.send("Started a new game!")
            await ctx.send(file=self.active_games[ctx.author.id].print_board_png())
        else:
            await ctx.send("You already have an active game!")

    @commands.command()
    @is_active_player()
    async def move(self, ctx, move: str):
        # Command to make a move in the chess game
        game = self.active_games[ctx.author.id]
        valid_move, message, engine_move = game.make_move(move)
        if valid_move:
            # If the move is valid, show the engine's countermove and the updated board
            await ctx.send(f"Engine plays {engine_move}\n", file=game.print_board_png())
            if game.board.is_game_over():
                # Checks if the game is over and sends the outcome
                outcome_message = game.game_outcome()
                await ctx.send(outcome_message)
                del self.active_games[ctx.author.id]
        else:
            # If the move is invalid, notify the user
            await ctx.send(message)

    @commands.command()
    @is_active_player()
    async def resign(self, ctx):
        delete_png(ctx.author.id, 'engine')  # Deletes board png file
        del self.active_games[ctx.author.id]  # Removes the game from active games
        await ctx.send(f"{ctx.author.name} resigned.")

    @commands.command()
    @is_active_player()
    async def board(self, ctx):
        game = self.active_games[ctx.author.id]
        await ctx.send(file=game.print_board_png())


async def setup(bot):
    await bot.add_cog(ChessEngineGame(bot))
