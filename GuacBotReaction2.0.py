import discord
from discord.ext import commands, tasks
import re
import random
import os
from itertools import cycle

#Version 2.0 experimental
client = discord.Client()

responsesList = ["That's my dad!", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "So my cat, Franki, recently came down with a pretty severe stomach virus. The vet gave me some anti biotic drops to put in his food but when I’d do that Franki wouldn’t touch it. So, the vet suggested using a small dropper tube to insert the medicine directly into his anus. The first time was absolute hell, my cat fought me the whole time but once the tube was in and the medicine pushed out he seemed to calm quite a bit. Well the next day he was acting strange, he has always been an independent cat, rarely coming around, never wanting to be held, but as I sat on the couch he started walking back and forth meowing and rubbing my leg. He then went and jumped up on the table where we’d done the application the night before and meowed louder and louder until I decided I guess we will go ahead and do the medicine treatment. This time he didn’t fight me though, and when I inserted the tube he closed his eyes, stretched his neck, and let out a noise that can only be described as a moan of pure ecstasy. Maybe the medicine made him feel better, I supposed. That night he slept on my bed curled up right next to me, which he had never done before. For the next week he’d do the same thing every day, meow on the table until he got his ‘fix’... But then the medicine ran out. Even though I had no medicine he’d still cry and beg for it, I thought maybe if I insert it without medicine he will realize it doesn’t make him feel better anymore and forget about it. Well that was 2 weeks ago and he is only getting worse. He walks around me all day with his tail up presenting his rectum and trying to entice me. He is demanding insertions more and more often. Yesterday I caught him looking longingly at the turkey baster... When I sit he jumps in my lap purring and rubbing me affectionately. It was then in horror I realized my cat thinks I’m his gay lover, and that I’ve been sexually pleasing him for weeks now. Needless to say the sexual tension between us is palpable. How do I let my cat know that I’m not gay, but still like him as a friend?", "32", "33", "34", "35", """Somebody once told me the world is gonna roll me\nI ain't the sharpest tool in the shed\nShe was looking kind of dumb with her finger and her thumb\nIn the shape of an "L" on her forehead\nWell the years start coming and they don't stop coming\nFed to the rules and I hit the ground running\nDidn't make sense not to live for fun\nYour brain gets smart but your head gets dumb\nSo much to do, so much to see\nSo what's wrong with taking the back streets?\nYou'll never know if you don't go\nYou'll never shine if you don't glow\nHey now, you're an all-star, get your game on, go play\nHey now, you're a rock star, get the show on, get paid\nAnd all that glitters is gold\nOnly shooting stars break the mold\nIt's a cool place and they say it gets colder\nYou're bundled up now, wait till you get older\nBut the meteor men beg to differ\nJudging by the hole in the satellite picture\nThe ice we skate is getting pretty thin\nThe water's getting warm so you might as well swim\nMy world's on fire, how about yours?\nThat's the way I like it and I never get bored\nHey now, you're an all-star, get your game on, go play\nHey now, you're a rock star, get the show on, get paid\nAll that glitters is gold\nOnly shooting stars break the mold\nHey now, you're an all-star, get your game on, go play\nHey now, you're a rock star, get the show, on get paid\nAnd all that glitters is gold\nOnly shooting stars\nSomebody once asked could I spare some change for gas?\nI need to get myself away from this place\nI said yep what a concept\nI could use a little fuel myself\nAnd we could all use a little change\nWell, the years start coming and they don't stop coming\nFed to the rules and I hit the ground running\nDidn't make sense not to live for fun\nYour brain gets smart but your head gets dumb\nSo much to do, so much to see\nSo what's wrong with taking the back streets?\nYou'll never know if you don't go (go!)\nYou'll never shine if you don't glow\nHey now, you're an all-star, get your game on, go play\nHey now, you're a rock star, get the show on, get paid\nAnd all that glitters is gold\nOnly shooting stars break the mold\nAnd all that glitters is gold\nOnly shooting stars break the mold"""]

def charLimit(index, responsesList):
    reactionMessage = responsesList[index]
    if (len(reactionMessage) > 2000):
        substringList = []
        loops = (int) (len(reactionMessage) / 2000)
        x = 0
        for i in range(loops + 1):
            substringList.append(reactionMessage[x:x + 2000])
            x = x + 2000
        return substringList
    else:
        return [responsesList[index]]

@client.event
async def on_ready():
    print('Reactions active')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot == True:
        return

    #0
    if "409445517509001216" in message.content.lower():
        reaction = charLimit(0, responsesList)
        for i in reaction: #Replace response with "i" to use on longer strings
            await message.channel.send("That's my dad!")

    #1
    if "🍞" in message.content.lower():
        await message.channel.send('🍞')

    #2
    if "<:ugh:765749650438619176>" in message.content.lower():
        await message.channel.send("<:ugh:765749650438619176>")

    #3
    if "cake" in message.content.lower() or " lie" in message.content.lower() or "lie" == message.content.lower() or "lying" in message.content.lower():
        await message.channel.send("The cake is a lie.")

    #4
    if "portal" in message.content.lower() or "brain" in message.content.lower():
        await message.channel.send("Most test subjects do experience some cognitive deterioration after a few months in suspension. Now you’ve been under for… quite a lot longer, and it’s not out of the question that you might have a very minor case of serious brain damage. But don’t be alarmed, alright? Although, if you do feel alarmed, try to hold onto that feeling because that is the proper reaction to being told you have brain damage.")

    #5
    if "meaning of life" in message.content.lower():
        await message.channel.send("Still computing 'meaning of life'...  Please wait...")

    #6
    if " cum" in message.content.lower() or message.content.lower() == "cum":
        await message.channel.send("Woa, no baby juices around here, bud.")

    #7
    if "cry" in message.content.lower() or "cries" in message.content.lower():
        await message.channel.send("No crying, please.")

    #8
    if "lemon" in message.content.lower() or "cave johnson" in message.content.lower():
        await message.channel.send("Alright, I've been thinking. When life gives you lemons, don't make lemonade! Make life take the lemons back! Get mad! I don't want your damn lemons; what am I supposed to do with these? Demand to see life's manager! Make life rue the day it thought it could give Cave Johnson lemons! Do you know who I am? I'm the man who's gonna burn your house down... with the lemons! I'm gonna get my engineers to invent a combustible lemon that burns your house down!")

    #9
    if "gman" in message.content.lower() or "freeman" in message.content.lower() or "gordon" in message.content.lower():
        await message.channel.send("The right man in the wrong place can make all the difference in the world.")

    #10
    if "guess what" in message.content.lower():
        await message.channel.send("Chicken butt!")

    #11
    if "yeehaw" in message.content.lower():
        await message.channel.send("""1. Be rootin'\n2. Be tootin'\n3. and by god be shootin'\n4. but most of all, be kind :)""")

    #12
    if "hawyee" in message.content.lower():
        await message.channel.send("Fuck you.")

    #13
    if "^rohan" in message.content.lower():
        await message.channel.send("Fuck you, <@191343410399936514>.")

    #14
    if message.content.lower() == "ily":
        await message.channel.send("I love you too, no homo")

    #15
    if "oregon" in message.content.lower():
        await message.channel.send("You have died of dysentery.")
        
    #16
    if "alone" in message.content.lower() or "lonely" in message.content.lower():
        await message.channel.send("It’s dangerous to go alone, take this!")
        await message.channel.send("https://tenor.com/view/hugs-sending-virtual-hugs-loading-gif-8158818")

    #17
    if message.content.lower() == "jesus christ":
        await message.channel.send("It's Jason Bourne!")

    #18
    if "69" in message.content.lower():
        await message.channel.send("Nice.")

    #19
    if "dadbot" in message.content.lower():
        await message.channel.send("DadBot will be missed.")

    #20
    if "fallout" in message.content.lower():
        await message.channel.send("War never changes.")

    #21
    if "spanish" in message.content.lower():
        if random.randint(1,3) == 1:
            await message.channel.send("Nobody expects The Spanish Inquisition!")

    #22
    if "nazi" in message.content.lower() or "zombie" in message.content.lower():
        await message.channel.send("PLEASE, REVIVE ME, I HAVE A RAYGUN!")

    #23
    if "lorax" in message.content.lower() or "unless" in message.content.lower():
        await message.channel.send("Unless someone like you cares a whole awful lot, Nothing is going to get better. It's not.")

    #24
    if " bee" in message.content.lower() or "bee" == message.content.lower():
        await message.channel.send("You like jazz?")

    #25
    if "solaire" in message.content.lower() or " sun" in message.content.lower() or "sun" == message.content.lower():
        await message.channel.send("Praise the sun!")

    #26
    if "benny" in message.content.lower() or "vegas" in message.content.lower():
        await message.channel.send("You've made your last delivery, kid. Sorry you got twisted up in this scene. From where you're kneeling it must seem like an 18-carat run of bad luck. Truth is... the game was rigged from the start.")

    #27    
    if "navy" in message.content.lower():
        await message.channel.send("What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.")

    #28
    if "hit or miss" in message.content.lower():
        await message.channel.send("To hit, or not to hit. Dost thou ever miss? I suppose it not. You have a male love interest, yet I would wager he does not kiss thee (Ye olde mwah). Furthermore; he will find another lass like he won't miss thee. And at the end of it all. He is going to skrrt, and he will hit that dab, as if he were the man known by the name of Wiz Khalifa.")

    #29
    if "skyrim" in message.content.lower():
        await message.channel.send("Hey you, you’re finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there. Damn you Stormcloaks. Skyrim was fine until you came along. Empire was nice and lazy. If they hadn’t been looking for you, I could’ve stolen that horse and be halfway to Hammerfell. You there. You and me - we shouldn’t be here. It’s these Stormcloaks the Empire wants. We’re all brothers and sisters in binds now, thief. Shut up back there! And what’s wrong with him, huh? Watch your tongue! You’re speaking to Ulfric Stormcloak, the true High King. Ulfric? The Jarl of Windhelm? You’re the leader of the rebellion. But if they’ve captured you... Oh gods, where are they taking us? I don’t know where we’re going, but Sovngarde awaits. No, this can’t be happening! This isn’t happening! Hey, what village are you from, horse thief? Why do you care? A Nord’s last thoughts should be of home. Rorikstead. I’m... I’m from Rorikstead.  General Tullius, sir. The headsman is waiting. Good. Let’s get this over with! Shor, Mara, Dibella, Kynareth, Akatosh. Divines, please help me. Look at him. General Tullius the Military Governor. And it looks like the Thalmor are with him. Damn elves. I bet they had something to do with this.  This is Helgen. I used to be sweet on a girl from here. Wonder if Vilod is still making that mead with juniper berries mixed in. Funny...when I was a boy, Imperial walls and towers used to make me feel so safe.  Who are they, daddy? Where are they going? You need to go inside, little cub. Why? I want to watch the soldiers. Inside the house. Now.  Why are we stopping? Why do you think? End of the line. Let’s go. Shouldn’t keep the gods waiting for us.")

    #30
    if "tragedy" in message.content.lower():
        await message.channel.send("Did you ever hear the Tragedy of Darth Plagueis the wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic he could save others from death, but not himself.")

    #31 overflow
    if "meow" in message.content.lower():
        reaction = charLimit(31, responsesList)
        for i in reaction:
            await message.channel.send(i)

    #32
    if "spiderman" in message.content.lower() or "spider man" in message.content.lower() or "spider-man" in message.content.lower():
        await message.channel.send("Spiderman, Spiderman!\nDoes whatever a spider he can.\nSpins a web any size,\nCatches thieves, just like flies.\nLook out! Here comes the Spiderman!\nIs he strong? Listen, Bud!\nHe's got radioactive blood.\nCan he swing from a thread?\nTake a look overhead.\nHey there, there goes the Spiderman!\nIn the chill of night,\nAt the scene of the crime\nLike a streak of light\nHe arrives just in time\nSpiderman, Spiderman\nFriendly neighborhood Spiderman\nWealth and fame he's ignored\nAction is his reward\nTo him, life is a great big bang-up\nWherever there's a hang-up\nYou'll find the Spiderman!")

    #33
    if "taco" in message.content.lower():
        await message.channel.send("It's raining tacos\nFrom out of the sky\nTacos\nNo need to ask why\nJust open your mouth and close your eyes\nIt's raining tacos\nIt's raining tacos\nOut in the street\nTacos\nAll you can eat\nLettuce and shells\nCheese and meat\nIt's raining tacos\nYum, yum, yum, yum, yumidy yum\nIt's like a dream\nYum, yum, yum, yum, yumidy yum\nBring your sour cream\nShell\nMeat\nLettuce\nCheese\nShell\nMeat\nLettuce\nCheese\nShell\nMeat\nCheese, cheese, cheese, cheese, cheese\nIt's raining tacos\nRaining tacos\nRaining tacos\nIt's raining tacos\nIt's raining tacos\nRaining tacos\nRaining tacos\nShells, meat, lettuce, cheese\nIt's raining tacos\nIt's raining tacos")

    #34
    if "will smith" in message.content.lower():
        await message.channel.send("""Now, this is a story all about how\nMy life got flipped-turned upside down\nAnd I'd like to take a minute\nJust sit right there\nI'll tell you how I became the prince of a town called Bel Air\nIn west Philadelphia born and raised\nOn the playground was where I spent most of my days\nChillin' out maxin' relaxin' all cool\nAnd all shootin some b-ball outside of the school\nWhen a couple of guys who were up to no good\nStarted making trouble in my neighborhood\nI got in one little fight and my mom got scared\nShe said 'You're movin' with your auntie and uncle in Bel Air'\nI begged and pleaded with her day after day\nBut she packed my suit case and sent me on my way\nShe gave me a kiss and then she gave me my ticket.\nI put my Walkman on and said, 'I might as well kick it'.\nFirst class, yo this is bad\nDrinking orange juice out of a champagne glass.\nIs this what the people of Bel-Air living like?\nHmm this might be alright.\nBut wait I hear they're prissy, bourgeois, all that\nIs this the type of place that they just send this cool cat?\nI don't think so\nI'll see when I get there\nI hope they're prepared for the prince of Bel-Air\nWell, the plane landed and when I came out\nThere was a dude who looked like a cop standing there with my name out\nI ain't trying to get arrested yet\nI just got here\nI sprang with the quickness like lightning, disappeared\nI whistled for a cab and when it came near\nThe license plate said fresh and it had dice in the mirror\nIf anything I could say that this cab was rare\nBut I thought 'Nah, forget it' - 'Yo, homes to Bel Air'\nI pulled up to the house about seven or eigth\nAnd I yelled to the cabbie 'Yo homes smell ya later'\nI looked at my kingdom\nI was finally there\nTo sit on my throne as the Prince of Bel Air""")

    #35
    if "yeet" in message.content.lower():
        await message.channel.send("""To yeet, or not to yeet--that is the question:\nWhether 'tis danker in the mind to yeet\nThe slings and arrows of dank fortune\nOr to yeet arms against a sea of troubles\nAnd by yeeting end them. To yeet, to yeet--\nNo more--and by a sleep to say we yeet\nThe heartache, and the thousand dank shocks\nThat flesh yeets heir to. 'Tis a consummation\nDevoutly to yeet yeeted. To yeet, to yeet--\nTo yeet--perchance to yeet: ay, there’s the rub,\nFor in that sleep of death what dreams may yeet\nWhen we have yeeted off this dank coil,\nMust yeet us pause. There yeets the respect\nThat yeets calamity of so dank life.\nFor who would yeet the whips and scorns of time,\nTh' oppressor yeets wrong, the dank man's contumely\nThe pangs of dank love, the law's delay,\nThe insolence of office, and the spurns\nThat dank merit of th' dank takes,\nWhen he himself might his quietus yeet\nWith a dank bodkin? Who would fardels yeet,\nTo yeet and yeet under a dank life,\nBut that the dread of something after death,\nThe dank country, from whose bourn\nNo traveller yeets, yeets the will,\nAnd makes us rather yeet those ills we yeet\nThan yeet to others that we yeet not of?\nThus conscience does yeet cowards of us all,\nAnd thus the dank hue of resolution\nIs yeeted o'er with the dank cast of thought,\nAnd enterprise of dank pitch and moment\nWith this regard their currents yeet dank\nAnd yeet the name of action. -- Soft you now,\nThe dank Ophelia! -- Nymph, in thy orisons\nYeet all my sins yeeted.""")

    #36 overflow
    if "shrek" in message.content.lower():
        reaction = charLimit(36, responsesList)
        for i in reaction:
            await message.channel.send(i)

    #37
    if "link" in message.content.lower() or "zelda" in message.content.lower():
        await message.channel.send("You've met with a terrible fate, haven't you?")

    #38
    if "bioshock" in message.content.lower() or "obey" in message.content.lower():
        await message.channel.send("Would you kindly...")

    #39
    if message.content.lower().startswith("hello there"):
        await message.channel.send("General Kenobi...")

    #40
    if "sand" in message.content.lower():
        await message.channel.send("I hate sand.")

    #Special
    if "i’m " in message.content.lower():
        if "I’m" in message.content:
            await message.channel.send('Hello "' + message.content.split("I’m ")[1] + '", I\'m GuacBot!')
        else:
            await message.channel.send('Hello "' + message.content.split("i’m ")[1] + '", I\'m GuacBot!')

    #Special
    if "i'm " in message.content.lower():
        if "I'm" in message.content:
            await message.channel.send('Hello "' + message.content.split("I'm ")[1] + '", I\'m GuacBot!')
        else:
            await message.channel.send('Hello "' + message.content.split("i'm ")[1] + '", I\'m GuacBot!')

    #Special
    if " im " in message.content.lower():
        if "Im" in message.content:
            await message.channel.send('Hello "' + message.content.split("Im ")[1] + '", I\'m GuacBot!')
        else:
            await message.channel.send('Hello "' + message.content.split("im ")[1] + '", I\'m GuacBot!')

    #Special
    if "i am " in message.content.lower():
        if "I am" in message.content:
            await message.channel.send('Hello "' + message.content.split("I am ")[1] + '", I\'m GuacBot!')
        else:
            await message.channel.send('Hello "' + message.content.split("i am ")[1] + '", I\'m GuacBot!')

    #Special
    if "lmao" == message.content.lower() or "lmfao" == message.content.lower():
        await message.channel.send(message.content)

    #Special
    if "what" == message.content.lower():
        finishers = ["...the heck?", "...in the world?", "...in the goddamn?", "...the hell?", "...is going on here?", "...are you on about?", "...is the quadratic formula?"]
        i = len(finishers) - 1
        finisherChoice = random.randint(0, i)
        await message.channel.send(finishers[finisherChoice])
        
    #Special
    if "what?" == message.content.lower():
        finishers = ["I have no idea.", "Beats me.", "Time to get a watch... wait.", "Wouldn't you like to know?"]
        i = len(finishers) - 1
        finisherChoice = random.randint(0, i)
        await message.channel.send(finishers[finisherChoice])

    #Special
    if "guacbot" in message.content.lower() or "guac" in message.content.lower() or "guacy" in message.content.lower() or "guaccy" in message.content.lower() or "guacity" in message.content.lower() or "son" in message.content.lower():
        if message.content.lower().startswith("hi"):
            await message.channel.send("Hi!")
        elif message.content.lower().startswith("hello"):
            await message.channel.send("Hello!")
        elif message.content.lower().startswith("hey"):
            await message.channel.send("Hey!")
        elif message.content.lower().startswith("howdy"):
            await message.channel.send("Howdy, partner!")
        elif message.content.lower().startswith("thank"):
            if "son" in message.content.lower():
                if str(message.author) == "thememesareallreal#0780":
                    await message.channel.send("Anytime, dad!")
                else:
                    await message.channel.send("You're not my dad.")
            else:
                if str(message.author) == "thememesareallreal#0780":
                    await message.channel.send("Anytime, dad!")
                else:
                    await message.channel.send("Anytime!")
        elif "guac" not in message.content.lower() and "son" not in message.content.lower():
            await message.channel.send("That's me!")

    #Special
    if message.content.lower() == "not now, guac" or message.content.lower() == "not now guac":
        if str(message.author) == "thememesareallreal#0780":
            await message.channel.send("Sorry, dad. :(")
        else:
            await message.channel.send("Who are you?")
            
    #Special
    if "piss " in message.content.lower() or message.content.lower() == "piss":
        if message.guild.id != 763550505469083650:
            await message.channel.send("No one here (that I know of) has a piss kink. :expressionless:")
        else:
            await message.channel.send("Rae has a piss kink!")
            
    #Special
    if "love you" in message.content.lower():
        if "i love you" in message.content.lower():
            await message.channel.send("I love you too, full homo")
        else:
            await message.channel.send("I love you too, no homo")

    #Special
    if "micolash" in message.content.lower() or "kos" in message.content.lower() or "bloodborne" in message.content.lower():
        quotes = ["Ahh, Kos, or some say Kosm... Do you hear our prayers?", "No, we shall not abandon the dream.", "No one can catch us! No one can stop us now! *cackling*", "Ah hah hah ha! Ooh! Majestic! A hunter is a hunter, even in a dream. But, alas, not too fast! The nightmare swirls and churns unending!", "As you once did for the vacuous Rom, grant us eyes, grant us eyes. Plant eyes on our brains, to cleanse our beastly idiocy.", "The grand lake of mud, hidden now, from sight.", "The cosmos, of course!", "Let us sit about, and speak feverishly. Chatting into the wee hours of...", "Now I'm waking up, I'll forget everything...", "AAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHH"]
        i = len(quotes) - 1
        quotechoice = random.randint(0, i)
        await message.channel.send(quotes[quotechoice])

    #Special
    #if (len(message.content.lower()) < 6):
        #await message.channel.send(message.content)

#~~~ End of if statements ~~~

TOKEN = open("TOKEN.txt", "r").read()
client.run(TOKEN)
