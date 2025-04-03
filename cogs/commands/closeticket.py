from discord.ext import commands
import discord


class CloseTicket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_guild = True)
    @commands.hybrid_command(name="closeticket")
    async def close_ticket(self, ctx : commands.Context, channel : discord.TextChannel, reason : str = ""):
        if channel.category_id != 1356718971331547268:
            await ctx.send("You can't delete a non-ticket text channel")
        else:
            try :
                categoryArchivved = discord.utils.get(ctx.guild.categories, id=899714498812858389)
                archivedChannel = await channel.clone(name=channel.name, category = categoryArchivved)
                await archivedChannel.send(f"Ticket {channel.name} closed by {ctx.author.display_name} for {reason}")
            except:
                ctx.send("Something went wrong.")
                return
            await channel.delete()

class CloseButton(discord.ui.View):
    def __init__(self, *, timeout=None, channel: discord.TextChannel):
        self.channel = channel
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Close Ticket",style=discord.ButtonStyle.red ,emoji="🎁")
    async def button_callback(self, interaction:discord.Interaction, button:discord.ui.Button):
        if not interaction.user.guild_permissions.manage_guild:
            await interaction.response.send_message("You can't close a ticket.", ephemeral=True)
        try :
            categoryArchivved = discord.utils.get(interaction.guild.categories, id=899714498812858389)
            archivedChannel = await self.channel.clone(name=self.channel.name, category = categoryArchivved)
            await archivedChannel.send(f"Ticket {self.channel.name} closed by {interaction.user.display_name}")
        except Exception as e:
            print(e)
            await interaction.response.send_message("Something went wrong !", ephemeral=True)
            return
        await self.channel.delete()

            
async def setup(bot: commands.Bot):
    await bot.add_cog(CloseTicket(bot=bot))