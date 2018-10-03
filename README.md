<img src="res/logo/logo_small.png" alt="socie" width="50"/> socie 
<p align="center">
    <a href="https://raw.githubusercontent.com/archvillain/socie/master/LICENSE" alt="WTFPL License">
        <img src="https://img.shields.io/badge/license-WTFPL-ff69b4.svg"/></a>
    <a href="#version">
        <img src="https://img.shields.io/badge/version-1.0-lightblue.svg"
            alt="version"></a>
    <a href="https://discord.gg/HjJCwm5">
        <img src="https://img.shields.io/discord/494990656603815950.svg?logo=discord"
            alt="chat on Discord"></a>
</p>

__**Warning**__: Currently Linux/BSD/Mac only.

**NOTE**: For educational purposes and personal use none other. AS-IS product. This will repository is temporary. `CLI` means `command language interpreter` if you are illiterate computer user.

### Legal Disclaimer
--------------------------------

Discord boys has not annouced any official statement if using their
API for 3rd party clients is allowed, therefore be careful. It is against Discord's ToS of using their API for "self bots." This software does not any sort do anything automated related.

So far, there has not been someone who got banned for using this type of software before, again
it is up to Discord to decide. This product is as-is and if you get banned, we do not take no responsiblity so use this at your own risk. `We don't give a fuck.`


## Launching
------------------------
It is recommended to be within the `socie`
directory upon starting. Manually you can launch via `python3.6 ./socie.py`, 
We recommend to create a helper script to do this for you.

There's an example script is in the `/res/scripts` folder, for you to
edit fit for your system.


## How to get "socie" running:
-------------------------

1. On your CLI, install the dependencies (recommended `pip3`):

    `sudo pip3 install asyncio discord blessings pyyaml`

2. Clone the repo

    `git clone https://github.com/archvillain/socie`

### Token Warning
-------------------------------
PLEASE DO *NOT* share your token with anybody, if someone else gets obtains your token, you are a victim of getting hacked. Your account will be in a hands of someone you may not know and you are retarded. Please do not leave your token for the public and it should only be seen by you.

If your that person
who keeps their ~/.config on github, **add your token to your .gitignore**.
Otherwise it will become public. Just don't put it anywhere in this repository otherwise `bad things will happen.` 


3. Find your dikord "token"

    * Use your Dikord app or go to http://discordapp.com/channels/@me

    * Open your internet browser's developer console. (Normally `F12` or `CTRL-SHIFT-I`) (works on Dikord application as well)

    * Click `Network` tab, the `Console` tab is not needed.

    * Type `"/api"` on text box that has `'Filter'` in it, Refresh Dikord by `F5`, 

    * Click on the `applications` box under `Headers` tab (bottom right of the console screen), clicking this will show you a list of variables on the bottom right of the console page. 
    
    * Scroll down for a line that looks like:

        `"authorization: your.token123456fuckyoueatass6969420"`

    * Copy your token and paste it somewhere safe

4. On CLI type `python3 socie.py --store-token your.token123456fuckyoueatass6969420` to store your token

5. On CLI Type `python3 socie.py --copy-skeleton` to get a template config

6. On CLI Edit `~/.config/socie/config` to your choosing. (I recommend increasing some space and another CLI window)

7. Launch <b>socie</b> with `python3`

    `python3 socie.py`

    *(if you have `python3.6` you can simply use `./socie.py`)*


### License
-------------------------------

Licensed under `WTFPL` <br/>
For education, and have fun.

### Information
-------------------------------
You can find more in `man.md` and
how to use.
