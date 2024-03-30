import discord


class QuitButton(discord.ui.View):
    def __init__(self, user_id, quit_action):
        super().__init__()
        self.user_id = user_id
        self.quit_action = quit_action

    @discord.ui.button(label="Quit", style=discord.ButtonStyle.secondary, custom_id="quit_puzzle")
    async def quit_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == self.user_id:
            await self.quit_action.handle_quit(self.user_id, interaction)
        else:
            await interaction.response.send_message("You cannot quit this action.", ephemeral=True)
