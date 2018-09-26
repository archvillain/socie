import os
from utils.globals import gc

def get_token():
    if os.path.exists(os.getenv("HOME") + "/.config/socie/token"):
        token = ""
        try:
            f = open(os.getenv("HOME") + "/.config/socie/token", "r")
            token = f.read()
            f.close()
        except: pass

        if token != "":
            return token
    
    from blessings import Terminal
    gc.term = Terminal()
    print("\n" + gc.term.red("Error reading token."))
    print("\n" + gc.term.yellow("Are you sure you stored your token? Double check"))
    print(gc.term.yellow("Use --store-token to store your token."))
    quit()

def store_token():
    import sys
    from blessings import Terminal
    
    token = ""
    try: 
        token=sys.argv[2]
    except IndexError:
        print(Terminal().red("Error: You did not specify a token! probably incorrect input"))
        quit()

    if not os.path.exists(os.getenv("HOME") + "/.config/socie"):
        os.mkdir(os.getenv("HOME") + "/.config/socie")

    if token is not None and token != "":
        # trim off quotes if user added them
        token = token.strip('"')
        token = token.strip("'")

    # ------- Token format seems to vary, disabling this check for now -------- #
    # if token is None or len(token) < 59 or len(token) > 88:
        # print(Terminal().red("Error: Bad token. Did you paste it correctly?"))
        # quit()
    # ------------------------------------------------------------------------- #
    
    try:
        f = open(os.getenv("HOME") + "/.config/socie/token", "w")
        f.write(token)
        f.close()
        print(Terminal().green("a Token is fucking stored!"))
    except:
        print(Terminal().red("Error: Could not write token to file."))
        quit()
