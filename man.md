### Current Features
--------------------------

* : /channel "channel name" --> change channel
* : /server "server name" --> change server
* : /nick "nick name" --> to change nickname (per server)
* : @member expansion/mentions
* : /status "status" --> to change online presence
* typing without a leading prefix will submit to current chat
* "<USER> is typing..." support
* private channels
* colored output, with user definable colors and custom roles
* Channel logs update when users edit messages
* /channels, /servers, /users to view information
* /game to update the "Now playing: " status
* use /help to see more commands
* unicode emoji displayal support
* sending emojis in messages (unicode *and* custom)
* File uploading via path (ex: /file /path/to/file)
* italic, bold, and underline font support
* inline \`code\` and \`\`\`code\`\`\` block support
* URL detection, highlighting in blue + italics
* automatic updating, fetching the latest master branch's commit
* channel logs blink red upon unread messages
* line scrolling
* dikcord "Nitro" emojis
* Externalized configs via YAML ~/.config/socie/config

### Legal Disclaimer
--------------------------------

Discord boys has not annouced any official statement if using their
API for 3rd party clients is allowed, therefore be careful. It is against Discord's ToS of using their API for "self bots." This software does not any sort do anything automated related.

So far, there has not been someone who got banned for using this type of software before, again
it is up to Discord to decide. This product is as-is and if you get banned, we do not take no responsiblity so use this at your own risk. We don't give a fuck.

## Launching
------------------------
It is recommended to be within the "socie"
directory upon starting. Manually you can launch via `python3.6 ./socie.py`, 
however it is advised to create a helper script to do this for you.

Example script is located in the /res/scripts folder, for you to
edit that fits for your system.

## Dependencies
------------------------

* git (for automatic updates)
* [Python 3.5+](https://www.python.org/downloads/)
* [discord.py](https://github.com/Rapptz/discord.py)
* [blessings.py](https://pypi.python.org/pypi/blessings/)
* [PyYAML](https://pypi.python.org/pypi/PyYAML/)
* asyncio

**To install dependencies**:

1. Download Python 3.5/3.6
2. Install `pip3`, it is also called `python3-pip` in package manager
3. Download the dependencies using pip3 with the following command:

    `sudo pip3 install asyncio discord blessings pyyaml`

### Color Customization
------------------------

You can edit your client with these set of colors from  `~/.config/socie/config`

Note: If you have colors already defined in your ~/.Xresources or similar, this will 
be very confusing. Assuming you are using your terminal stock colors.


## How to install step by step (no notes version)
------------------------

1. On your CLI, install the dependencies (recommended pip3):

    `sudo pip3 install asyncio discord blessings pyyaml`

2. Clone the repo

    `git clone https://github.com/archvillain/socie`


3. Find your dikord "token"

    * Use your Dikord app or go to http://discordapp.com/channels/@me

    * Open your internet browser's developer console. (Normally `F12` or `CTRL-SHIFT-I`) (works on Dikord application as well)

    * Click `Network` tab, the `Console` tab is not needed.

    * Type `"/api"` on text box that has `'Filter'` in it, Refresh Dikord by `F5`, 

    * Click on the "application" box under "Names" tab, clicking this will show you a list of variables on the bottom right of the console page. 
    
    * Scroll down for a line that looks like:

        `"authorization: your.token123456fuckyoueatass6969420"`

    * Copy your token and paste it somewhere safe

4. On CLI type `python3 socie.py --store-token your.token123456fuckyoueatass6969420` to store your token

5. On CLI Type `python3 socie.py --copy-skeleton` to get a template config

6. On CLI Edit `~/.config/socie/config` to your choosing. (I recommend increasing some space and another CLI window)

7. Launch <b>socie</b> with `python3`

    `python3 socie.py`

    *(if you have `python3.6` you can simply use `./socie.py`)*