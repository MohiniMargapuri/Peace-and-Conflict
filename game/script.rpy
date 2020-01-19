#these are the characters
define sm = Character ("Stepmom",color="#7630f0")
define ss = Character ("Cole",color="#5ad32c")
define su = Character ("Michael",color="#cca433")
define unknown = Character ("???",color="#dd22c2")

#the images and sprites used
image bg burning = "burninghousebackground.jpg"
image bg modern_house = "modernhouse.jpg"
image bg black = "blackbackground.jpg"
image bg bedroom = "bedroom.jpg"
image bg balcony = "balconyveiw.jpg"
image bg tunnel = "subway.jpg"
image bg fence = "fence.jpg"
image bg air = "airport.jpg"
image bg home = "home.jpg"

#the characters
image cole = "cole.png"
image stepmom = "stepmom_norm.png"
image stepdad = "stepdad_norm.png"
image michael = "michael.png"



label start:
    $points = 0
    
    #The game actually begins
    
    scene bg black
    
    $ mc = renpy.input("{b}What is your name?{/b}")

    $ mc = mc.strip()

    if mc == "":
        $ mc ="[Y/N]"

    "Pleased to meet you, %(mc)s!"
    
    scene bg burning
    
   
    "Soldier #1" "I HEAR SOMETHING OVER THERE!"
    "Soldier #2" "UNDERSTOOD, SIR!"
    
    scene bg black
    with fade
    
    "10 years later..."
    
    
    scene bg modern_house
    show stepmom_norm
    
    sm "-once your done with those, start with the dishes. "
    mc "{i}I already knew that.{/i}"
    sm "NO BACKTALKING, YOU PATHETIC BRAT!! "
    mc "Yes ma'am."
    sm "If you show that kind of behaviour again, it's down to the basement for you. Do I make myself clear, trash?"
    mc "Y-Yes ma'am."
    sm "*crash*"
    
    hide stepmom_norm
    
    scene bg black
    with fade
    
    "Late at night..."
    
    scene bg balcony
    
    mc "*sigh* I really should stop talking out loud, it'd get me in more trouble."
    mc "Isn't Sir on a buisness trip? At least he won't be here to yell at me, I get enough bruises with ma'am."
    
    show cole
    
    ss "hey,%(mc)s, are you alright?"
    mc "I'm fine, Cole." 
    mc "{i}I lied.{/i}"
    ss "Are you sure?"
    mc "Um, yeah, it's just a cut from a glass plate."
    ss "Why...Is it from mom?"

menu:
     
     "Tell him the truth":
         
        $points += 1
        jump truth
     
     "Tell him a lie":
         $points += 3
         jump lie
         
label truth:
    
    $scar = True
    
    mc "...yeah, I said something out loud and upset her. But it's fine! It's my fault for taking back in the first place."
    ss "..."
    ss "Maybe you should just escape from this place."
    mc "HUH?!"
    ss "Be quiet! And I really think you should, ya know, run away. Mom and dad treat you like filth beneath their shoes no matter how hard you work for them."
    mc "But where would I go? If I get caught then it'll be even worse! How would I even get enough supplies for the trip? I'll need money, clothes, and also- "     
    ss "I'll help you."
    mc "excuse me?"
    ss "I'll help you, and you'll leave soon. Perhaps when mom goes to the supermarket or something."
    mc "...I'll think about it."
    
    hide cole
    
    jump bedroom
    
     
                
label lie:    
    
    $scar = False
    
    mc "No...and you should be getting to bed now."
    ss "...Fine.*Goes to room*"
    
    hide cole
    
    mc "..."
    mc "*Goes to bed*"
    
    
    
    jump bedroom
    
label bedroom:
    
    scene bg bedroom
    
    mc "{i}Escaping, huh? Is it worth the risk? If I fail, then everything up till that point would be for nothing. I'd need to think of a plan.{/i}"
    mc "{i}Would the country even allow it, i mean it's illegal immigration. I'll have to sorta consider myself lucky, since most kids my age and younger than me would be on the streets. I'll need to escape once I get the chance. So I'll have to prepare beforehand.{/i}"
    mc "{i}I'll be homealone tomorrow since cole and ma'am are going to the movies. That could be my chance to rummage through for items.{/i}"
 
    scene bg black
    with fade
                                                                                                                                           
    "The next morning..."
                        
    scene bg modern_house
    show stepmom
     
     
    sm "%(mc)s, make sure you follow the instructions I gave you, or else you know what will happen."                                                                                                                                 
    mc "Understood."
    mc "{i}Alright, now to set my plan into action...{/i}"
    
    hide stepmom
    
    scene bg black
    "You've obtained a bag, food, waterbottle, money, clothes, and medicine."
    "That night..."
    
    scene bg bedroom
    
    mc "Alright, I've got everything. Cole and ma'am are asleep now, this is my chance. I'm worried about Cole, but he's strong. I need to leave Jenock, the laws of this land are too cruel!"
    "*You quietly go to the backyard*"      
    
    scene bg escape
    with fade
    
    mc "Now or never..."
   
    scene bg fence
    
    
    mc "{i}Should I really climb over the fence? Or should I look for another way?{/i}"
    
menu:
    
    "Climb over the fence":
        $points += 3
        jump climb
        
    "Look for another way":
        $points += 1
        jump way
        

label climb:
    
    $climb = True
    
    mc "Hmph!"
    "You land safely on the pavement"
    "You keep walking down a road"
   
    scene bg tunnel
    
    mc "{i}A tunnel to that abandoned subway! Maybe I can stay there for the night.{/i}"
    "You walk into the tunnel and find a decent spot to rest"
    
    scene bg black
    with fade
    jump supporter
    

label way:
    
    $climb = False
    
    mc "{i}I should check my options first{/i}"
    unknown "Is there someone there?"
    mc "{i}Oh no! The fence it is then.{/i}"
    "You hastly climb the fence but fall on the pavement."
    mc "*grunts* Ow!"
    "You have a gash on your knee from the fall."
    mc "{i}Just great. Now I'm bleeding, yay.{/i} -_-"
    "You limp your way to a subway tunnel."
    
    scene bg tunnel
    
    mc "I should rest here for the night and patch myself up."
    "You limp into the tunnel and find a decent spot to rest"
    mc "*sigh* Now to deal with my knee."
    "You use your medicine on your knee and rip a piece of cloth from your shirt to tie up the wound."
    mc "I'm so exhausted. *Yawn*"
    "You soon fall asleep"
    scene bg black
    with fade
    jump supporter
    
label supporter:
    
    unknown "So pale, you should eat more."
    
    
    scene bg tunnel
    show michael
    
    
    mc"Huh?!"
    
    scene bg tunnel
    with vpunch
    show michael
    
    mc "{i}What the-? who is-? why is he here? Please tell me he isn't going to take me back. I'm going to labour camp! Dear god, I knew this was a bad idea!{/i}"
    unknown "Don't worry, i'm not going to hurt you. My name is Michael. I work for P.F.C. coorporation."

menu:

    "P.F.C.?":
        $points += 3
        jump nameless
        
    "My name is...":
        $points += 2 
        jump name

label name:
    
    $name = True

    mc "Um...My name is %(mc)s. What does P.F.C. stand for?"
    su "You should be more careful with your name. P.T.S. stands for Protection till safe. We are similar to the CPS. Here's my Identification card."
    "You look at the card. It seems legit."
    mc "Alright, so why are you here?"
    su "I help people escape the borders of countries and support them until they are stable enough at their new location. We also educate them on things they need to know about the country."
    su "So, can you tell me why are you here?"
    jump reason
    
label nameless:
    
    $name = False
    
    mc "What does P.T.S. stand for?"
    su "P.T.S. stands for Protection tlll safe, we are similar to the CPS. Here's my Identification card."
    "You look at the card. It seems legit."
    mc "Alright, so why are you here?"
    su "I help people escape the borders of countries and support them until they are stable enough at their new location. We also educate them on things they need to know about the country."
    su "So, can you tell me your name and why you're here?" 
    mc "Um...%(mc)s..."
    jump reason
    
label reason:
    
    mc "I'm here because I ran away from home. When I was 4, There was a war between my previous home and this country. My parents died in a fire caused by a bomb."
    mc "I was found by soliders who were part of My stepfather's batallion. Two of their platoon soliders and taken to there base to find out what to do with me. I was taken into my stepfather's family and am a slave to them."
    mc "This country's rules are vicious and inhumane. People are suffering because of our leader and I want to leave."
    su "Would you like me to help you?"
    mc "{i}Should I let him? He seems nice, I feel like I can trust him...{/i}"
    
    scene bg black 
    with fade
    
menu:
    
    "Let Michael help you.":
        $points += 3
        jump help
    
    "Think about it":
        $points += 2
        jump maybe
    
    "...No":
        $points += 1
        jump no
    
label no:

    
    
    
    scene bg tunnel
    with fade

    mc "...Um, no."
    su "Are you sure?"
    mc "Yes."
    su "..."
    su "......"
    su "Very well then. But I will say, being cautious in this world is good, but too much could {i}get you killed.{/i}"
    su "*Stands up and walks away.*"
    
    hide michael
    
    mc "{i}That was ominous. I'm hungry anyway, so I'll eat some food then.{/i}"
    
    scene bg black
    with fade
    
    "You use up your last items for food and water. You try get closer to the border but not by much."
    "..."
    "......"
    "............."
    "..................."
    "Bad Ending" "...You die of starvation. You're body is found roughly 14 KM from your house."
    
    return
    
    
label help:
    
    scene bg tunnel
    with fade
    show michael
    mc "I...I would like that..."
    su "You should be more cautious about strangers, %(mc)s. But i'm glad you've decided to accept my help."
    su "First, You should eat something and drink some water."
    mc "I-I have some canned soup, and a water bottle."
    su "Fill up and meet me outside the tunnel."
    "You eat up but can't help wondering what's to come next."
    
    hide michael
    jump airport
    
label maybe:
    
    scene bg tunnel 
    with fade
    show michael
    mc "I'm not sure...what exactly is the plan?"
    su "We've decided that getting you to the neighboring continent by airport. It's going to be the 7:45 AM plane. I've booked the tickets and will be accompanying you until further notice."
    mc "{i}I'm going to another continent...kinda exciting. I'm finally going to be free.{/i}"
    mc "{i}If we're going to one of the neighboring countries, then it's either Rossius or Porton.{/i}"
label airport:    
    
    scene bg black
    with fade
    
    "Outside the tunnel..."
    
    scene bg balcony
    with fade
    show michael
    
    su "%(mc)s, I've spoken to my boss about the situation. We've decided that getting you to the neighboring continent by airport. It's going to be the 7:45 AM plane. I've booked the tickets and will be accompanying you until further notice."
    mc "{i}I'm going to another continent...kinda exciting. I'm finally going to be free.{/i}"
    mc "{i}If we're going to one of the neighboring countries, then it's either Rossius or Porton.{/i}"
    mc "Mr. Michael, where exactly are we going?"
    su "We'll be departing to Rossius, Harness to be more exact. Then, after things get sorted out, You'll be staying in Porton, in the beautiful state of Ezeldarm."
    mc "I see. Is what I have with me fine?"
    su "Yes, just make sure you are awake at 6 AM sharp."
    
    hide michael
    
    scene bg  black
    with fade
    
    "In the morning..."
    
    scene bg tunnel
    with fade
    
    su "Good morning,%(mc)s, are you ready?"
    mc "...I guess? I'm not entirely sure."
    su "That's alright. I don't really expect you to be."
    mc "{i}Rude.{/i}"
    su "Oh, im sorry if I sounded like that to you."
    mc "{i}I was talking out loud again, wasn't I?{/i}"
    
    scene bg black
    with fade
    
    "At the Airport..."
    
    scene bg air
    with fade
    
    unknown "Welcome to Arabista Airport!"
    mc "{i}Some computer-like voice of an Arabistian lady.{/i}"
    unknown "*Murmur murmur*  *Murmur murmur*"
    unknown "*Murmur murmur* *Murmur murmur*"
    mc "There're lots of people here. I'm starting to feel claustraphobic...It's like the basement."
    mc "...."
    mc "........."
    mc "................"
    su "-ey, kid? Hey, you're okay."
    mc "H-huh?"
    su "You had an anxiety/panic attack, They're relatively common for people dealing with trauma and stress."
    mc "..."
    su "I'm guessing it's a flashback. Happens to people suffering from PTSD. But you'll be fine, they come and they go."
    
    show soldier
    
    "Soldier" "Identify yourself."
    
    
    $ mcfn = renpy.input("{b}Enter your fake name?{/b}")

    $ mcfn = mcfn.strip()

    if mcfn == "":
        $ mcfn ="[F/N]"
        
    mc "{i}Don't get caught. Don't get caught. Don't get caught. Don't get caught. Don't get caught. Don't get caught. Don't get caught. Don't get caught.{/i}"
    "Solider" "Alright, we need to make sure you're not lying, so we'll need to clarify once again."
    mc "...okay."    



if $points==10:
    
    scene bg black 
    with fade
    
    "You made it safely past the border. P.T.S. has helped you escape and gain stability. You have been going to therapy for a few years now."
    
    scene bg home
    with fade
    
    "You have a nice apartment in Ezeldarm. Porton is a wonerful country, especially for refugees. The number of help organizations is amazing."
    "You have a stable job and are finally free, you are also a spokesperson at a few events and interviews. You still miss Cole and wonder how he is."
    "Good ending..."
    return
else:
    
    scene bg black
    with fade
    
    "You failed. The efforts of Cole, michael and yourself had gone to waste."
    "You were taken back to the Leiutenent, Sir was beyond furious with you. You were sent to labour camp for 2 years, you were rediculed relentlessly before being sent back to your stepfamily."
    "You dissapointed Cole. You were no longer the brave older sibling he cared about. You were pitiful."
    "Once you got back, the punishments you got were ruthless. Bruises and cuts on every inch of your body. Pure torture and agony"
    "The pain was too much to bare..."
    "You found your stepfather's Government 1911..."
    "You were found dead in the living room...Suicide, a bullet to the side of the head."
    "Bad ending..."
    return

    
    #This is the end of the game :)

