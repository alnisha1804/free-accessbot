import discord
import time
from discord import app_commands
import random
import os


# Internal user data (NOT recommended for production)
# This is used for demonstration purposes only. You should use a proper database.
user_data = {}

def check_user_play_count(user_id):
  """Checks the user's internal play count (for demonstration)."""
  if user_id not in user_data:
    user_data[user_id] = {'play_count': 0}
  return user_data[user_id]['play_count']

def update_user_play_count(user_id):
  """Updates the user's internal play count (for demonstration)."""
  if user_id in user_data:
    user_data[user_id]['play_count'] += 1

class aclient(discord.Client):
  def __init__(self):
    super().__init__(intents=discord.Intents.default())
    self.synced = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:
      await tree.sync()
      self.synced = True
    print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name='mines', description='mines game mode')
async def mines(interaction: discord.Interaction, tile_amt: int, round_id: str):
  if len(round_id) >= 10:  # Check for minimum length instead of exact length
    user_id = str(interaction.user.id)
    play_count = check_user_play_count(user_id)

    # Daily Limit Logic (single play limit)
    if play_count == 0:
      start_time = time.time()
      grid = ['❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌']
      already_used = []

      count = 0
      while tile_amt > count:
        a = random.randint(0, 24)
        if a in already_used:
          continue
        already_used.append(a)
        grid[a] = '✅'
        count += 1

      chance = random.randint(85, 95)
      if tile_amt < 4:
        chance = chance - 15

      em = discord.Embed(color=0x0025ff)
      em.add_field(name='Grid', value="\n" + "`" + grid[0] + grid[1] + grid[2] + grid[3] + grid[4] + "\n" + grid[5] + grid[6] + grid[7] + grid[8] + grid[9] + "\n" + grid[10] + grid[11] + grid[12] + grid[13] + grid[14] + "\n" + grid[15] + grid[16] + grid[17] + grid[18] + grid[19] + "\n" + grid[20] + grid[21] + grid[22] + grid[23] + grid[24] + "`\n" + f"**Accuracy**\n`{chance}%`\n**Round ID**\n`{round_id}`\n**Response Time:**\n`{str(int(time.time() - int(start_time)))}`")
      em.set_footer(text='made by Amaan')
      await interaction.response.send_message(embed=em)
      update_user_play_count(user_id)  # Update play count (for demonstration)
    else:
      # Handle user reaching daily limit
      channel_id = 1256258500485713980  # Replace with the actual channel ID where purchase info is
      channel = client.get_channel(channel_id)
    
      await interaction.response.send_message("You've reached the daily limit. Consider purchasing the unlimited access version for more: <#1256258500485713980> ")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
