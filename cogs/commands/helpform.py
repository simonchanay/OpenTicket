from discord.ext import commands
import discord

class HelpForm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command("test")
    async def test(self, ctx: commands.Context):
        await ctx.send()

class HelpFormModal(discord.ui.Modal):
    name = discord.ui.TextInput(label=f"Here the subtitle you want", 
                                placeholder="Short placeholder")
    
    feedback = discord.ui.TextInput(
        label='What do you think of this new feature?',
        style=discord.TextStyle.long,
        placeholder='Type your feedback here...',
        required=False,
        max_length=300,
    )
    async def on_submit(self, interaction: discord.Interaction):
        #TO DO : protect the server from massive creation of rooms by a single user
        category = discord.utils.get(interaction.guild.categories, id=1356718971331547268)
        interaction.guild.create_text_channel(category=category, name=str(self.id))
        tc = discord.utils.get(interaction.guild.text_channels, name=self.id)
        await tc.send(content=f"{self.name.value}")
        await interaction.response.send_message(f'Thanks for your feedback, {self.name.value}! A mod is going to help you', 
                                                ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        print(error)


async def setup(bot: commands.Bot):
    await bot.add_cog(HelpForm(bot=bot))
