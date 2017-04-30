import discord
from discord.ext import commands
from PyDictionary import PyDictionary

# !meaning #meaning of a word
# !synonym #synonyms of a word
# !antonym #antonyms of a word
# !translate #translation of a word

class Dictionary:
    """Makes wordart from strings or someshizz"""
    
    def __init__(self, bot):
        self.bot = bot
        self.dictionary = PyDictionary('lxml')
        
    
    def unjson(self, msg):
        print("huh")
       
    @commands.command()
    async def meaning(self, word:str):
        ret = self.dictionary.meaning(word)
        if ret is None:
            await self.bot.say("```Meaning for "+word+" not found.```")
        else:
            def_str = ""
            for k in ret.keys():
                def_str +=k + ":\n"
                for i in ret[k][:3]:
                     def_str += i + "\n"
                def_str += "\n"
            await self.bot.say("```"+def_str+"```")
        
        
    @commands.command()
    async def synonym(self, word:str):
        ret = self.dictionary.synonym(word)
        if ret is None:
            await self.bot.say("```Synonym for "+word+" not found.```")
        else:
            def_str = "Synonyms for "+word+": "
            for j in ret:
                def_str += j + ", "
            await self.bot.say("```"+def_str+"```")
    
    @commands.command()
    async def antonym(self, word:str):
        ret = self.dictionary.antonym(word)
        if ret is None:
            await self.bot.say("```Antonym for "+word+" not found.```")
        else:
            def_str = "Antonyms for "+word+": "
            for j in ret:
                def_str += j + ", "
            await self.bot.say("```"+def_str+"```")
    
    #google translate broke this function
    @commands.command()
    async def translate(self, word:str, lang:str):
        ret = self.dictionary.translate(word, lang)
        print(word)
        print(lang)
        if ret is None:
            await self.bot.say(word+" not found.")
        else:
            await self.bot.say("```"+ret+"```")
        
def setup(bot):
    bot.add_cog(Dictionary(bot))
