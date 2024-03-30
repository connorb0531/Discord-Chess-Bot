from discord.ext import commands

from components.quit_button import QuitButton
from utils.puzzle_logic import PuzzleLogic


# Decorator to check if a message author is the active player for a puzzle
def is_active_player():
    async def predicate(ctx):
        # Check if the author's ID is in the list of active puzzles
        return ctx.author.id in ctx.cog.active_puzzle

    return commands.check(predicate)


class Training(commands.Cog, name="Training"):
    def __init__(self, bot):
        self.bot = bot
        self.active_puzzle = {}  # Dictionary to keep track of active puzzles by user ID

    @commands.command()
    async def puzzle(self, ctx):
        # Start a new puzzle for the user if they don't already have one active
        if ctx.author.id not in self.active_puzzle:
            puzzle_logic = PuzzleLogic()  # Initialize the puzzle logic
            self.active_puzzle[ctx.author.id] = puzzle_logic  # Assign the puzzle logic to the user
            puzzle_logic.setup()  # Setup the puzzle
            # Send the initial board to the user
            await ctx.send(f"\n```\n{puzzle_logic.print_board()}\n```", view=QuitButton(ctx.author.id, self))
        else:
            await ctx.send("You already have an active puzzle.")

    @commands.command()
    @is_active_player()
    async def check(self, ctx, move: str):
        # Process a move made by the user in their active puzzle
        puzzle_logic = self.active_puzzle[ctx.author.id]
        check, engine_move = puzzle_logic.check_move(move)
        if check:
            if puzzle_logic.current_move is None:  # Puzzle solved condition
                await ctx.send(f"Puzzle solved! Congratulations! 🎉\n```{puzzle_logic.print_board()}```")
                # Remove the puzzle from active puzzles, allowing a new one to start
                del self.active_puzzle[ctx.author.id]
            elif engine_move:
                # Inform the user of the correct move and show the engine's response
                await ctx.send(f"Correct. Engine plays {engine_move}\n```{puzzle_logic.print_board()}```",
                               view=QuitButton(ctx.author.id, self))
            else:
                # Acknowledge the correct move and prompt for the next move
                await ctx.send(f"Correct move. Awaiting your next move.\n```{puzzle_logic.print_board()}```")
        else:
            # Inform the user the move was incorrect and prompt again
            await ctx.send("Incorrect move. Try again.", view=QuitButton(ctx.author.id, self))

    # Method to handle a user quitting their puzzle
    async def handle_quit(self, user_id, interaction):
        if user_id in self.active_puzzle:
            del self.active_puzzle[user_id]
            await interaction.response.send_message("Your puzzle has been quit.", ephemeral=True)
        else:
            await interaction.response.send_message("You don't have an active puzzle to quit.", ephemeral=True)

    # Listener to handle command errors within this cog
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            # Handle unauthorized attempts to use puzzle commands based on the cog's context
            if ctx.command.cog_name == 'Training':
                await ctx.send("You don't have an active puzzle.")
            elif ctx.command.cog_name == 'Chess Engine Game':
                await ctx.send("You don't have an active game.")
        else:
            # Generic error handler for all other types of errors
            await ctx.send(f"An error occurred: {error}")


async def setup(bot):
    await bot.add_cog(Training(bot))