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
    print(gc.term.red("INVALID:"))
    print("\n" + gc.term.red("ERROR: 無効なトークン。 \nE̸̗͚̰̜͎̫̿̐̊̔͆̾̉̊̅̚͝RRƠ̸̳̙̙̯̌͒̓̽͒̒̄̓͒̽͒͊̅̍̐̇̋̽̅̎̿͒̈́̈͒̈́͝͝͠͝͝R: token i̷n̸v̴a̵l̴i̶d̶."))
    print("\n" + gc.term.yellow("Incorrect token input. Please check if you input a token. \n不正なトークン入力。 トークンを入力したかどうかを確認してください。"))
    print(gc.term.yellow("Use --store-token to store your token."))
    quit()

def store_token():
    import sys
    from blessings import Terminal
    
    token = ""
    try: 
        token=sys.argv[2]
    except IndexError:
        print(Terminal().yellow("INVALID:")) #some reason its bright blue?
        print(Terminal().red("ERROR: お前はトークンを指定していません！ おそらく誤った入力。\nE̸̗͚̰̜͎̫̿̐̊̔͆̾̉̊̅̚͝RRƠ̸̳̙̙̯̌͒̓̽͒̒̄̓͒̽͒͊̅̍̐̇̋̽̅̎̿͒̈́̈͒̈́͝͝͠͝͝R: You did not specify a token! probably incorrect input"))
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
        print(Terminal().green("PASSED:"))
        print(Terminal().green("トークンは入力され保存されています。S̷̨̻͗̋͒ocieţ̵̛̩̰̬̒̓͝ţ̸̧̍̽̅̑̿e  🗲 「 ソシエット 」をしてください。\n\nT̸̡̻̺͍̝͈͚͈̘̥̣̮̥͎̅̿̑͋͊̅͌͂̀̄̅͒̚͘͘̚͝͝ͅoken stored! Please run socie."))
        print(Terminal().green("\nrun: python3 socie.py   -or-    ./socie.py \n"))
    except:
        print(Terminal().red("ERROR: ファイルにトークンを書き込めませんでした。\nE̸̗͚̰̜͎̫̿̐̊̔͆̾̉̊̅̚͝RRƠ̸̳̙̙̯̌͒̓̽͒̒̄̓͒̽͒͊̅̍̐̇̋̽̅̎̿͒̈́̈͒̈́͝͝͠͝͝R: Could not write token to file."))
        quit()
