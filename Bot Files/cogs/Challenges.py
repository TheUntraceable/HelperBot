import discord
from discord.ext import commands

class Challenges(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.group(case_insensitve=True,invoke_without_command=True)
    async def challenge(self,ctx):
        embed = discord.Embed(title="Subcommands!",color=ctx.author.color)
        embed.add_field(name="List Indexing: ",value="This command will be all about list's and indexing them.")
    @challenge.group(case_insensitve=True,invoke_without_command=True)
    async def one(self,ctx):
        embed = discord.Embed(title="Subcommands!",color=ctx.author.color,description="These are the available subcommands for the list indexing challenge.")
        embed.add_field(name="Info: ",value="This will get all the information about list's. This is not the help command.",inline=True)
        embed.add_field(name="Submit: ",value="Submit your answer",inline=True)
        embed.add_field(name="Question: ",value="Sends the question for you to answer.",inline=True)
        await ctx.send(embed=embed)
    @challenge.group(case_insensitve=True,invoke_without_command=True)
    async def submit(self,ctx):
        embed = discord.Embed(color=ctx.author.color,title="Submit your answers!",description="Below are a list of questions you can answer, please use `.challenge <ChallengeNumber> submit <QuestionNumber>` to answer a question!")
        embed.set_footer(text="Use `.challenge <ChallengeNumber> question for a list of questions!`")
        await ctx.send(embed=embed)
    @one.group(case_insensitve=True,invoke_without_command=True)
    async def question(self,ctx):
        embed = discord.Embed(color=ctx.author.color,title="The question!",description="Answer these series of questions to put your list knowledge to use!")
        embed.add_field(name="\u200b",value="Use `.challenge one submit <question>  <your code/answer>`, and the bot will decide if it's correct or not!")
        embed.add_field(name="Question 1: ",value="What error will be raised with this code? \n```py\nalist = [1,2,3,4,5,6,7,8,9,0]\nprint (alist[10])")
        await ctx.send(embed=embed)
    @submit.command(case_insensitve=True,invoke_without_command=True)
    async def one(self,ctx,*,answer):
        pass # I still need to get some shit done
    @one.group(case_insensitve=True,invoke_without_command=True)
    async def info(self,ctx):
        embed = discord.Embed(title="List's",color=ctx.author.color,description="This paragraph will contain useful information concerning lists.")
        embed.add_field(name="Lists as a whole: ",value="Lists/arrays,also a type of iterable, are represented in python as `[]`, you can put whatever you want to inside of these `[]`, you can seperate items with a `,`. For example ```py\nl = [1,2,3]\nprint (l)```You can store whatever datatypes here, really, try it yourself!",inline=False)
        embed.add_field(name="Lists rules: ",value="The rules a list has are simple, each seperate item must be splitted by a `,`. You can't have a trailing comma at the end. Pretty sure that's just it. Well.",inline=False)
        embed.add_field(name="List indexes: ",value="Indexes are the order each item comes in. Indexes start at `0` at all times. No exceptions. An example of this is\n```py\nl = [0,1,2,3,4,5,6,7,8,9]\nprint (l[0]) # This will output 0.\nprint (l[1]) # This will output 1\n``` If a list has 12 items and you index the list at 12, such as\n```py\nl = [1,2,3,4,5,6,7,8,9,10,11,12]\n print (l[12]) # This will raised a IndexError because there are 12 items in the list and indexes start at 0```",inline=False)
        embed.add_field(name="Bultins revolving lists: ",value="```py\nlist.append(LiterallyAnything`)\nlist.insert(LiterallyAnything,WhatIndexToAddItAt)\nlist.extend(ListYouWantToAddToTheEndOfThisList)\nlist.del(IndexYouWantToDelete)\nlist.pop(IndexYouWantToRemove)\nlist.copy() # Creates a copy of the list, takes in to args\nlist.clear() # Clears the contents of a list, takes in no args\nlist.reverse() # This reverses the items' order in a list\nlist.sort() # Sorts the items in ascending order, takes no args\nlist.index(ItemYouWantToGetTheIndexFor)```",inline=False)
        embed.add_field(
            name="Examples of List usages: ",
            value="""
***Below are a list of __examples__ of list usages. These may be really useful.***
```py
# An example for getting a list of favourite music
FaveSongs = []
def func():
    Tracker = False
    print("What are a list of your favourite songs? Enter '123STOP' to end the list.")
    while Tracker == False:
        item = input("Favourite Song: ")
        FaveSongs.append(item)
        if item == "123STOP":
            Tracker = True
    return print (f"I see your fave songs are {song for song in FaveSongs}")
func()
``` 
            """,
            inline=False
            )
        embed.add_field(name="Extended example: ",value="""
        ```py

# An example of lists being used as a selection of choice
foods = ["pear","apple","banana"]
def get_food():
    Tracker = True
    while Tracker:
        print (f"Which food would you select from {food for food in foods}")
        selected = input ("Food: ")
        if selected not in foods:
            print ("That's not a valid option!")
        return print (f"I see your favourite food is {selected}"
```
            """)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(Challenges(client))
