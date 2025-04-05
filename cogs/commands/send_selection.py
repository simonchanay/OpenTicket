from discord.ext import commands
import discord
from datetime import datetime
import cogs.commands.help_form as help_form
import cogs.user_list as user_list

class SendSelectionCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="sendselection")
    async def sendselection(self, ctx: commands.Context, channel : discord.TextChannel):
        embed = discord.Embed(title="Tickets",
                      description="To open a ticket for support, please select the category from the ones offered.\n```\n1 - Option 1\n2 - Option 2\n3 - Option 3\n```\n**A moderator will come and help you**",
                      colour=0xe66100,
                      timestamp=datetime.now())
        embed.set_author(name="OpenTicket",
                        url="https://github.com/simonchanay/OpenTicket/blob/main/statics/images/logo2.png?raw=true")
        embed.add_field(name="⚠️ - Abuse",
                        value="Please do not abuse tickets.",
                        inline=True)
        embed.set_footer(text="OpenTicket", icon_url="https://github.com/simonchanay/OpenTicket/blob/main/statics/images/logo2.png?raw=true")

        await channel.send(embed=embed, view=DropdownView())
        await ctx.reply("The selection section has been created successfully.", ephemeral=True)    


class TicketSelectionMenu(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Option 1",emoji="👌",description="Here the description for the first option"),
            discord.SelectOption(label="Option 2",emoji="✨",description="Here the description for the second option"),
            discord.SelectOption(label="Option 3",emoji="🎭",description="Here the description for the third option")
        ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        if user_list.UserList().is_user_in_user_list(interaction.user) and user_list.UserList().get_counter_value() <= 50:
            await interaction.response.send_message("You have already opened a ticket.", ephemeral=True)
            return
        user_list.UserList().append_user(interaction.user)
        user_list.UserList().increment_counter()
        hf = help_form.HelpFormModalType1(title="Ticket", timeout=None)
        await interaction.response.send_modal(hf)

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.timeout = None
        self.add_item(TicketSelectionMenu())

async def setup(bot: commands.Bot):
    await bot.add_cog(SendSelectionCommand(bot=bot))