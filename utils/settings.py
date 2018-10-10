import os
import sys
from yaml import safe_load
from blessings import Terminal

settings = ""

def copy_skeleton():
    term = Terminal()
    try:
        from shutil import copyfile
        if not os.path.exists(os.getenv("HOME") + "/.config/socie"):
            os.mkdir(os.getenv("HOME") + "/.config/socie")
        
        if os.path.exists(os.getenv("HOME") + "/.config/socie/config"):
            try: 
                os.remove(os.getenv("HOME") + "/.config/socie/config")
            except: 
                pass

        copyfile("res/settings-skeleton.yaml", os.getenv("HOME") + "/.config/socie/config", follow_symlinks=True) 
        print(term.green("PASSED:\nsettings-skeleton.yamlがコピーされました！\nsettings-skeleton.yaml has been copied!" + term.normal))
        print(term.cyan("\nNOTE:\n設定ファイルは 「 ~/.config/socie 」にあります。\nYour configuration file can be found at $[~/.config/socie]\n"))

    except KeyboardInterrupt: 
        print("キャンセルしている...\nCancelling...")
        quit()
    except SystemExit: 
        quit()
    except:
        print(term.red("スケルトンファイルの作成中にエラーが発生しました。\nError creating skeleton file."))
        quit()

def load_config(path):
    global settings
    with open(path) as f:
        settings = safe_load(f)
 
arg = ""
try: 
    arg = sys.argv[1]
except IndexError: 
    pass

if arg == "--store-token" or arg == "--token":
    pass
elif arg == "--skeleton" or arg == "--copy-skeleton":
    copy_skeleton()
    quit()
elif arg == "--config":
    try:
        load_config(sys.argv[2])
    except IndexError:
        print("提供されるパスはありませんか？\nNo path provided?")
        quit()
    except:
        print("入力された設定へのパスが無効です。\nInvalid path to config entered.")
        quit()
else:
    try:
        load_config(os.getenv("HOME") + "/.config/socie/config")
    except:
        try:
            load_config(os.getenv("HOME") + "/.socie")
        except:
            print(term.red("INVALID:\nERROR:設定が見つかりません。\nsettings are not found."))
            quit()
