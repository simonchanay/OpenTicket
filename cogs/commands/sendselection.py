from discord.ext import commands
import discord
from datetime import datetime

class SendSelectionCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="sendselection")
    async def sendcommand(self, ctx: commands.Context, channel : discord.TextChannel):
        #TO DO : Add a link to the logo
        embed = discord.Embed(title="Tickets",
                      description="Pour ouvrir un ticket afin d'obtenir de l'aide, veuillez sélectionner la catégorie parmis celle qui sont proposées.\n```\n1 - Aide 1\n2 - Aide 2\n3 - Aide 3\n```\n**Un modérateur viendra vous aider..**",
                      colour=0xe66100,
                      timestamp=datetime.now())
        embed.set_author(name="OpenTicket",
                        url="https://google.com")
        embed.add_field(name="⚠️ - Abus",
                        value="Merci de ne pas abuser des tickets",
                        inline=True)
        embed.set_footer(text="OpenTicket")

        await channel.send(embed=embed, view=DropdownView())
        await ctx.reply("La commande a bien été générée", ephemeral=True)    

class TicketSelectionMenu(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Option 1",emoji="👌",description="This is option 1!"),
            discord.SelectOption(label="Option 2",emoji="✨",description="This is option 2!"),
            discord.SelectOption(label="Option 3",emoji="🎭",description="This is option 3!")
        ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Your favourite colour is {self.values[0]}')

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(TicketSelectionMenu())

async def setup(bot: commands.Bot):
    await bot.add_cog(SendSelectionCommand(bot=bot))