from nextcord import *
from nextcord.ext import commands
import time

from ext.util import *

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @slash_command(description="Checks whether you are admin or not", guild_ids=mains)
    async def checkadmin(self, interaction: Interaction):
        if interaction.user.id in bot_admins:
            await interaction.response.send_message(":white_check_mark: You are a CASbot admin!")

        else:
            await interaction.response.send_message(":x: You are not a CASbot admin.")

    @slash_command(description="Spams a message. ADMIN ONLY", guild_ids=mains)
    async def spam(
        self, 
        interaction: Interaction,
        times: int = SlashOption(name="times", description="How many times to repeat the message 1 10000", required=True),
        delay: float = SlashOption(name="delay", description="How long to wait between each message 0 60 secs", required=True),
        content: str = SlashOption(name="content", description="Text to send", required=True)
    ):
        if interaction.user.id in bot_admins:
            await interaction.response.send_message(":white_check_mark: Sending your message(s)!")
            for i in range(times):
                await interaction.channel.send(content)
                time.sleep(delay)

        else:
            await interaction.response.send_message(":x: Sorry, you do not have permission to use this command.")

    @slash_command(description="CASbot Admin commands", guild_ids=admin_guilds)
    async def admin(self, interaction: Interaction):
        await interaction.response.send_message("Hi")

    @admin.subcommand(description="Change the bot's prescence. ADMIN ONLY")
    async def presence(
        self, 
        interaction: Interaction,
        status_type: str = SlashOption(name="statustype", description="Choose the status type for the bot", required=True, choices=["online", "dnd", "idle", "invisible"]),
        activity_type: str = SlashOption(name="activitytype", description="Choose the activity type for the bot", required=True, choices=["playing", "streaming", "listening to", "watching", "competing in"]),
        activity_name: str = SlashOption(name="activityname", description="Specify the custom activity name", required=True)
    ):
        if interaction.user.id in bot_admins:
            status_types = {"online": Status.online, "dnd": Status.dnd, "idle": Status.idle, "invisible": Status.invisible}
            activity_types = {"playing": ActivityType.playing, "streaming": ActivityType.streaming, "listening to": ActivityType.listening, "watching": ActivityType.watching, "competing in": ActivityType.competing}
        
            await self.client.change_presence(status=status_types[status_type], activity=Activity(name=activity_name, type=activity_types[activity_type]))
            await interaction.response.send_message(f":white_check_mark: Activity successfully set to **{activity_type} {activity_name}** ({status_type}).")

        else:
            await interaction.response.send_message(":x: Sorry, you do not have permission to use this command.")

    @admin.subcommand(description="Shuts down the bot. ADMIN ONLY")
    async def shutdown(self, interaction: Interaction):
        if interaction.user.id in bot_admins:
            await interaction.response.send_message(":white_check_mark: Shutting down...")
            await self.client.close()

        else:
            await interaction.response.send_message(":x: You are not a CASbot admin.")