class script(object):
    START_TXT = """š·š“Lš»š¾ {},
š¼š š½š°š¼š“ šøš <a href=https://t.me/{}>{}</a> Iam a powerful autofilter bot with some more featues.. ā”š«š«š«"""
    HELP_TXT = """š·š“š {}
š·š“šš“ šøš šš·š“ š·š“š»šæ šµš¾š š¼š š²š¾š¼š¼š°š½š³š."""
    ABOUT_TXT = """ā® š¼š š½š°š¼š“: {}
ā® š²šš“š°šš¾š: <a href=https://t.me/HoiChoiTvAddaa>įįį„įįį</a>
ā® š»šøš±šš°šš: šæššš¾š¶šš°š¼
ā® š»š°š½š¶šš°š¶š“: šæššš·š¾š½ š¹
ā® š³š°šš° š±š°šš“: PERSONAL š³š±
ā® š±š¾š šš“ššš“š: OWN PRIVATE SERVER
ā® š±ššøš»š³ ššš°ššš: v1.0.2 [ š±š“šš° ]"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and į©įį©į­ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. į©įį©į­ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
ā¾ /filter - <code>add a filter in chat</code>
ā¾ /filters - <code>list all the filters of a chat</code>
ā¾ /del - <code>delete a specific filter in chat</code>
ā¾ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- į©įį©į­ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. į©įį©į­ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/source00Devil)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
ā¾ /connect  - <code>connect a particular chat to your PM</code>
ā¾ /disconnect  - <code>disconnect from a chat</code>
ā¾ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of į©įį©į­

<b>Commands and Usage:</b>
ā¾ /id - <code>get id of a specifed user.</code>
ā¾ /info  - <code>get information about a user.</code>
ā¾ /imdb  - <code>get the film information from IMDb source.</code>
ā¾ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my OįÆįEįā”

<b>Commands and Usage:</b>
ā¾ /logs - <code>to get the rescent errors</code>
ā¾ /stats - <code>to get status of files in db.</code>
ā¾ /delete - <code>to delete a specific file from db.</code>
ā¾ /users - <code>to get list of my users and ids.</code>
ā¾ /chats - <code>to get list of the my chats and ids </code>
ā¾ /leave  - <code>to leave from a chat.</code>
ā¾ /disable  -  <code>do disable a chat.</code>
ā¾ /ban  - <code>to ban a user.</code>
ā¾ /unban  - <code>to unban a user.</code>
ā¾ /channel - <code>to get list of total connected channels</code>
ā¾ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ā® šš¾šš°š» šµšøš»š“š: <code>{}</code>
ā® šš¾šš°š» ššš“šš: <code>{}</code>
ā® šš¾šš°š» š²š·š°šš: <code>{}</code>
ā® ššš“š³ ššš¾šš°š¶š“: <code>{}</code> š¼šš±
ā® šµšš“š“ ššš¾šš°š¶š“: <code>{}</code> š¼šš±"""
    LOG_TEXT_G = """#ššš°šš«šØš®š©
ā® šš«šØš®š© āŗāŗ {}(<code>{}</code>)
ā® ššØš­šš„ ššš¦ššš«š¬ āŗāŗ <code>{}</code>
ā® ššššš šš² āŗāŗ {}
"""
    LOG_TEXT_P = """#ššš°šš¬šš«
ā® šš āŗāŗ <code>{}</code>
ā® ššš¦š āŗāŗ {}
"""
    CARBON_TXT = """ <b>š²š°šš±š¾š½ š¼š¾š³šš»š“</b>

<b>šš¾š š²š°š½ š±š“š°šššøšµš šš¾šš š²š¾š³š“š š±š šššøš½š¶ šš·š šµš“š°šššš“...</b>

<b>š²š¾š¼š¼š°š½š³.!</b>
<b>/carbon āŗāŗ šš“šæš»š šš¾ š°š½š šš“šš š¼š“ššš°š¶š“</b>

<b>šš¾ššŗš š¾š½ š±š¾šš· š¶šš¾ššæ š°š½š³ šæš¼</b>
<b>š²šš“š³šøšš āŗāŗ</b> <a href=https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA>š¾šæšš-šš“š²š·š</a></b>"""
