from discord.ext import commands
import discord
from datetime import datetime
import cogs.commands.closeticket as closeticket
from config_loader import get_config


class HelpForm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command("test")
    async def test(self, ctx: commands.Context):
        await ctx.send()

class HelpFormModalType1(discord.ui.Modal):
    reason = discord.ui.TextInput(label=f"Explain the reason of the ticket", 
                                placeholder="")
    
    problem = discord.ui.TextInput(
        label='Explain your problem here',
        style=discord.TextStyle.long,
        placeholder='My problem is...',
        required=True,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        #TO DO : protect the server from massive creation of rooms by a single user
        ticket_category_id = int(get_config()["TICKET_CATEGROY_ID"])
        ticket_category = discord.utils.get(interaction.guild.categories, id=ticket_category_id)
        tc = await interaction.guild.create_text_channel(category=ticket_category, name=str(self.id))
        await tc.set_permissions(target=interaction.user, read_messages=True, view_channel=True)
        close_button = closeticket.CloseButton(timeout = None, channel=tc)

        embed = discord.Embed(title=f"Ticket of {interaction.user.display_name}",
                      description=f"**Reason :**\n{self.reason}\n\n**Description :**\n{self.problem}\n\n*A moderator will help you. Please wait before sending a new request !*\n||ID : {self.id}||",
                      colour=0x00b0f4,
                      timestamp=datetime.now())

        embed.set_author(name="Ticket")

        embed.set_footer(text="OpenTicket",
                        icon_url="https://github.com/simonchanay/OpenTicket/blob/main/statics/images/logo2.png")

        await tc.send(embed=embed, view=close_button)
        await interaction.response.send_message(f'Thanks for your feedback, {interaction.user.display_name}! A mod is going to help you', 
                                                ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        await interaction.response.send_message('Something went wrong.', ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(HelpForm(bot=bot))
