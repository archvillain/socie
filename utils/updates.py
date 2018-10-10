def check_for_updates():
    from utils.globals import gc
    from os import path
    
    if not path.exists(".git"):
        print(gc.term.red("INVALID:\nERROR:クライアントはそのディレクトリから起動していません！ もう一度お試しください。\nE̸̗͚̰̜͎̫̿̐̊̔͆̾̉̊̅̚͝RRƠ̸̳̙̙̯̌͒̓̽͒̒̄̓͒̽͒͊̅̍̐̇̋̽̅̎̿͒̈́̈͒̈́͝͝͠͝͝R: client not started from its directory! Cancelling..."))
        print(gc.term.yellow("Please start the client from its folder to get automatic updates. \n自動アップデートを取得するには、そのフォルダからクライアントを起動する必要があります。"))
        return

    try:# git pull at start as to automatically update to master repo
        from subprocess import Popen,PIPE
        print(gc.term.green + "ダウンロード中お待ちください。\n"+"\n"+"C̸̡̠̘̺͉̹̹͇͉̹̞̼̜̜͍̘̘̤̊́̍̒hecking fo̸̡̨͉͊̒͜r u̵̙͈̓̓́pdates for S̷̨̻͗̋͒ocieţ̵̛̩̰̬̒̓͝ţ̸̧̍̽̅̑̿e  🗲 「 ソシエット 」..." + gc.term.normal)
        process = Popen(["git", "pull", "--force"], stdout=PIPE)
        output = process.communicate()[0].decode('utf-8').strip()

        #if "Already up to date" not in output:
        if "Already up to date. 更新は必要ありません。  S̷̨̻͗̋͒ocieţ̵̛̩̰̬̒̓͝ţ̸̧̍̽̅̑̿e  🗲 「 ソシエット 」は最新です。" not in output:
            # print(gc.term.yellow("Updates downloaded! Please restart."))
            print("\n \n")
            # This quit() call is breaking the client on MacOS and Linux Mint
            # The if statement above is being triggered, even when the output IS
            # "Already up to date". Why is this happening?
            # quit()
        else:
            print("It is on the latest build. No update needed \n更新は必要ありません。  S̷̨̻͗̋͒ocieţ̵̛̩̰̬̒̓͝ţ̸̧̍̽̅̑̿e  🗲 「 ソシエット 」は最新です。" + "\n")
    except KeyboardInterrupt: print("Cancel update input received, skipping..." +"\n" +"更新がキャンセルされました。")
    except SystemExit: pass
    except OSError: # (file not found)
        # They must not have git installed, no automatic updates for them!
        print(gc.term.red +"ERROR: GITが必要です。" + "E̸̗͚̰̜͎̫̿̐̊̔͆̾̉̊̅̚͝RRƠ̸̳̙̙̯̌͒̓̽͒̒̄̓͒̽͒͊̅̍̐̇̋̽̅̎̿͒̈́̈͒̈́͝͝͠͝͝R: Could not get updates. Is \
               git installed?" + gc.term.normal)
    except:
        print(gc.term.red + "Unknown E̸̗͚̰̜͎̫̿̐̊̔͆̾̉̊̅̚͝RRƠ̸̳̙̙̯̌͒̓̽͒̒̄̓͒̽͒͊̅̍̐̇̋̽̅̎̿͒̈́̈͒̈́͝͝͠͝͝R (error) occurred during \
               updates." + gc.term.normal)
