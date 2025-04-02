from discord.ext import commands
import discord
from datetime import datetime
import cogs.commands.helpform as helpform

class SendSelectionCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    "Send the message that allows the user to select the category of help they need"
    @commands.hybrid_command(name="sendselection")
    async def sendcommand(self, ctx: commands.Context, channel : discord.TextChannel):
        #TO DO : Add a link to the logo
        embed = discord.Embed(title="Tickets",
                      description="To open a ticket for support, please select the category from the ones offered.\n```\n1 - Option 1\n2 - Option 2\n3 - Option 3\n```\n**A moderator will come and help you**",
                      colour=0xe66100,
                      timestamp=datetime.now())
        embed.set_author(name="OpenTicket",
                        url="https://google.com")
        embed.add_field(name="⚠️ - Abuse",
                        value="Please do not abuse tickets.",
                        inline=True)
        embed.set_footer(text="OpenTicket", icon_url="https://github.com/simonchanay/OpenTicket/blob/main/statics/images/logo2.png?raw=true")

        await channel.send(embed=embed, view=DropdownView())
        await ctx.reply("La commande a bien été générée", ephemeral=True)    

class TicketSelectionMenu(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Option 1",emoji="👌",description="Here the description for the first option"),
            discord.SelectOption(label="Option 2",emoji="✨",description="Here the description for the second option"),
            discord.SelectOption(label="Option 3",emoji="🎭",description="Here the description for the third option")
        ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        hf = helpform.HelpFormModal(title="Modal", timeout=None)
        await interaction.response.send_modal(hf)
        await interaction.channel.send(f'The id of the modal is {hf.id}')

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.timeout = None
        self.add_item(TicketSelectionMenu())

async def setup(bot: commands.Bot):
    await bot.add_cog(SendSelectionCommand(bot=bot))