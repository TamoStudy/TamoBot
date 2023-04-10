import discord

class Rules:

    @staticmethod
    def get_rules_embed(rules_channel):
        """
        Creates rules embed.
        """

        embed = discord.Embed(title='Server Rules', color=0xff3a40)
        embed.set_thumbnail(url='https://avatars.githubusercontent.com/u/59890724?v=4')
        embed.add_field(name='\u200b', value='**1** → Always follow [Discord\'s official Terms of Service](https://discord.com/terms)', inline = False)
        embed.add_field(name='\u200b', value='**2** → Be respectful to other users; any form of discrimination will not be tolerated.', inline = False)
        embed.add_field(name='\u200b', value='**3** → Initiating in fights/controversial discussion will not be tolerated.', inline = False)
        embed.add_field(name='\u200b', value='**4** → Do not send harmful material such as viruses, IP-grabbers, or harm-ware.', inline = False)
        embed.add_field(name='\u200b', value='**5** → Advertising of other servers/websites will not be tolerated.', inline = False)
        embed.add_field(name='\u200b', value='**6** → Use common sense. If you think it\'s going to get you in trouble, odds are it will.', inline = False)
        embed.add_field(name='\u200b', value='**7** → English only in text channels. You may speak in other languages in <#1030510653003276318>.', inline = False)
        embed.add_field(name='\u200b', value='**8** → Impersonating other users will not be tolerated.', inline = False)
        embed.add_field(name='\u200b', value=f'**Refer to {rules_channel.mention} for more information**.', inline = False)

        return embed