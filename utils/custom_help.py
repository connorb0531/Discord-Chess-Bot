from discord.ext import commands


class CustomHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        help_text = ""
        for cog, commands in mapping.items():
            command_list = [command.name for command in commands if command.name is not None]
            if command_list:
                cog_name = 'General' if cog is None else cog.qualified_name
                help_text += f"\n**{cog_name}**\n"
                help_text += ", ".join(command_list)

        # Get the author of the message (user who invoked the command)
        author = self.context.message.author
        # Send the help text as a direct message
        await author.send("Here's a list of commands you can use:\n" + help_text)

    async def send_command_help(self, command):
        help_text = f"**{command.name}**\n{command.help}"
        # Get the author of the message (user who invoked the command)
        author = self.context.message.author
        # Send the help text as a direct message
        await author.send(help_text)