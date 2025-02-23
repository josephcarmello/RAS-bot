import discord

RESPONSE_MAP = {
    "mobile": """📱 **Mobile AIM Clients**
    Mobile AIM clients are currently unsupported, but are on the roadmap!
    More details to come.""",

    "android": """🤖 **Android Info**
    Here’s some information about Android AIM clients.
    - They arent supported yet!
    - More details to come.""",

    "ios": """🍏 **iOS Info**
    Here’s some information about iOS AIM clients.
    - They arent supported yet!
    - More details to come.""",

    "setup": discord.Embed(
        title="🔧 Setup Instructions",
        description="Follow these steps to get set up:",
        color=discord.Color.blue()
    ).add_field(name="Self-Hosted", value="Visit the RAS github for configuration steps to host your own server.", inline=False)
     .add_field(name="Join Chivanet", value="Visit the ChivaNet web portal to create an account and join in!", inline=False)
     .set_footer(text="Need more help? Use !help"),

    "help": discord.Embed(
        title="❓ Help Section",
        description="Here are available commands:",
        color=discord.Color.green()
    ).add_field(name="!mobile", value="Information about mobile AIM clients", inline=False)
     .add_field(name="!setup", value="Setup instructions", inline=False)
     .add_field(name="!chivanet", value="ChivaNet details", inline=False),

    "chivanet": """🌐 **ChivaNet Info**
    ChivaNet is a publically accessible AIM network that uses RAS as its server backend.
    - Something something
    - Some more somethings"""
}

# Function to retrieve a response
def get_response(command):
    return RESPONSE_MAP.get(command, "Unknown command.")

# Function to get all available commands
def get_all_commands():
    return RESPONSE_MAP.keys()

