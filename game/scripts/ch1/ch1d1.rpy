label ch1d1:
    scene bg school hallway with dissolve
    "I step into the school grounds, taking a deep inhale of the fresh late-Summer air."
    "It's finally the new school year..."
    "I'm gonna make it the best one yet!"

    scene bg classroom day with dissolve
    "I enter my new classroom. I'm really early, there's only one other person here."
    "This could be my chance to make a new friend!"
    "I head over to the person."
    show m3gin school normal
    mc "Hello!"
    "???" "Hello. How can I help you?"
    "How polite."
    mc "Well, I thought I'd introduce myself to you."
    "???" "Go right ahead."
    mc "Okay!"
    mc "My name is..."
    python:
        mcname = renpy.input("What is your name?", length=32)
        mcname = mcname.strip()
        if not mcname:
            povname = "Ellie"
    "???" "Oh, nice to meet you, [mcname]."
    m3gin "My name is M3GIN."
    mc "M3GIN?"
    m3gin "Yes."
    mc "Oh... Nice to meet you, M3GIN."
    "She must be one of those Androids that are everywhere nowadays."
    "Why is one in my school though...? Wearing our uniform too..."