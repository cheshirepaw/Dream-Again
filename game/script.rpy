# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define v = Character("Vix", color="#d2125c")
define himeko = Character("Himeko", who_color="#ec4a88", what_color="#f0aac5")


# The game starts here.
init: #метка для кода который должен выполняться до начала игры

    $ left2 = Position(xalign=0.3) #задаем дополнительные лево и право
    $ right2 = Position(xalign=0.7)
    
    # variables DEFINE ДЛЯ КОНСТАНТ DEFAULT ДЛЯ ПЕРЕМЕННЫХ

# блок статов, точнее их стейджей (как с силой в gina's gym)
    default strength_level = 0
    default dexterity_level = 0
    default vitality_level = 0
    default intelligence_level = 0
    default wisdom_level = 0
    default charisma_level = 0

# блок опыта характеристик. по идее только его должно хватить так как на простейшую математику у renpy есть возможности без импорта math
    default strength_xp = 0
    default dexterity_xp = 0
    default vitality_xp = 0
    default intelligence_xp = 0
    default wisdom_xp = 0
    default charisma_xp = 0

#define background

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "Hello? Is anybody here?"
    "Ah, there you are."

    show himeko main:
        xalign 0.5 yalign 1.2
    with dissolve

    himeko "Hello! My name is Himeko. I'm author's representative here."
    himeko "Maybe one day I'll appear in a plot! Well, at least he promised me that."
    himeko "Anyway. As you can see, illustrations for this novel were made by AI."
    himeko "If you're not fine with it, I understand. You can leave. No grudge. No questions asked."
    himeko "For those who are still here, I really hope you like my style."
    himeko "I guess that's all for now! Let's proceed with actual plot."

    hide himeko main
    with dissolve

    scene room beginning
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    "Our story begins in not so distant future. Many wish that this future would be bright and shiny, but let's be real"

    "Pandemics. Endless economic disasters. Big countries attacking small countries just to show everyone that they have biggest balls in th block. When nobody wanted to look at these balls."

    "Oh, and let's not forget about AI taking over more and more jobs. Recruitment centers became battlegrounds because big wallets in governments fear spending budget on citizen's needs more than death"

    "So yeah. \"Bright and shiny.\" Fuck my arse."

    "And if you think that this is enough, you're wrong. On one day archeologists decided to open few very old canopies to see what's inside."

    "There was Lambda-Virus inside."

    "Lambda-Virus, or L-Vi, after incubation period starts attacks on all types of body cells, causing their continuous mutations and therefore organ degradation." 
    
    "Severe organ degradation syndrome as result of L-Vi infection is main cause of deaths in our story."

    "No cure developed yet. There are survivors of L-Vi, lucky 50\%, but they still need to deal with consequences of illness"

    "So here we are, in small cheap apartment, looking at the our protagonist, sitting at their PC with grim face."

    show vix test at right2
    with dissolve

    v "Alright, according to lab results I have L-Vi. To receive \"last wish\" package i need to fill this form."

    "\"Last wish\" is a pack of medicine that can be used by L-Vi patients to help with symptoms. Or ease last pain."

    "Because hospitals are overcrowded with patients, there is no way to get help if you don't have necessary contacts or can't pay."

    "So if you got L-Vi, you're all by yourself. The only thing that you can get is \"last wish\""

    v "Let's see... Name, sex, age... Occupation... I hope there is no wrong answer, knowing that they might actually limit \"last wish\" to certain jobs"

label job_choice:

    menu:
        "Please select your occupation"
        "Physical labor (construction worker, trainer, etc.)":
            jump physical_job
        "Intellectual job (IT, science, tutoring)":
            jump smart_job
        "Arts (artist, writer, musician)":
            jump arts_job
        
label physical_job:
    v "Good old physical labor. At least I got in some half descent shape before lockdown started."

    v "Should I really tell them that earn my living with moving heavy stuff?"

    menu:
        "Vix will receive bonus  to strength (STR) and vitality (VIT). Choose this occupation?"
        "Yes":
            #$ strength = strength + 3
            #$ vitality = vitality + 3
            jump after_job_choice
        "No":
            jump job_choice

label smart_job:
    v "Used my brains all my life. Maybe they will give me some bonus medicine."

    v "Should I tell them that my job requires brains?"

    menu:
        "Vix will receive bonus  to intelligence (INT) and wisdom (WIS). Choose this occupation?"
        "Yes":
            #$ intelligence = strength + 3
            #$ wisdom = vitality + 3
            jump after_job_choice
        "No":
            jump job_choice

label arts_job:
    v "At least others love what I do. Also can try to write about L-Vi in my blog."

    v "Should I tell them that I'm just an artist?"

    menu:
        "Vix will receive bonus  to dexterity (DEX) and charisma (CHA). Choose this occupation?"
        "Yes":
            #$ charisma = charisma + 3
            #$ dexterity = dexterity + 3
            jump after_job_choice
        "No":
            jump job_choice
        

label after_job_choice: #я не очень хорошо умею кодить, поэтому это лейбл для подтверждения после того как выбрана профессия
    v "I guess I'm fucked."

    #"They looked through message once again."

    #v "Immunoreaction percentage... Blood cells degradation approximate..."

    #v "{i}*Loud sigh*{/i}"

    #v "Can't understand much, except final statement. Guess I'll deal with what I have now."




    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
