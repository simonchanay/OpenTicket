from discord.ext import commands
import discord
from config_loader import get_config
import cogs.user_list as user_list

class CloseTicket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_guild = True)
    @commands.hybrid_command(name="closeticket")
    async def close_ticket(self, ctx : commands.Context, channel : discord.TextChannel, reason : str = ""):
        ticket_category_id = int(get_config()["TICKET_CATEGROY_ID"])
        archived_ticket_category_id = int(get_config()["ARCHIVED_TICKET_CATEGORY_ID"])
        if channel.category_id != ticket_category_id:
            await ctx.send("You can't delete a non-ticket text channel")
        else:
            try :
                category_archived = discord.utils.get(ctx.guild.categories, id=archived_ticket_category_id)
                archived_channel = await channel.clone(name=channel.name, category = category_archived)
                await archived_channel.send(f"Ticket {channel.name} closed by {ctx.author.display_name} for {reason}")
            except:
                ctx.send("Something went wrong.")
                return
            await channel.delete()

class CloseButton(discord.ui.View):
    def __init__(self, *, timeout=None, channel: discord.TextChannel, member : discord.Member):
        self.channel = channel
        self.member = member
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Close Ticket",style=discord.ButtonStyle.red ,emoji="🎁")
    async def button_callback(self, interaction:discord.Interaction, button:discord.ui.Button):
        if not interaction.user.guild_permissions.manage_guild:
            await interaction.response.send_message("You can't close a ticket.", ephemeral=True)
            return
        archived_ticket_category_id = int(get_config()["ARCHIVED_TICKET_CATEGORY_ID"])
        try :
            category_archived = discord.utils.get(interaction.guild.categories, id=archived_ticket_category_id)
            archived_channel = await self.channel.clone(name=self.channel.name, category = category_archived)
            await archived_channel.send(f"Ticket {self.channel.name} closed by {interaction.user.display_name}")
        except Exception as e:
            await interaction.response.send_message("Something went wrong !", ephemeral=True)
            return
        await self.channel.delete()
        user_list.UserList().remove_user_from_user_list(user=self.member)
        user_list.UserList().decrement_counter()

            
async def setup(bot: commands.Bot):
    await bot.add_cog(CloseTicket(bot=bot))