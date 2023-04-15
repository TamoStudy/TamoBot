<p align="center">
<img src="./README%20Assets/TamoBot.png" width="200px">
</p>

<p align="center">
<b>TamoBot</b> by <a href="https://github.com/narlock">narlock</a>
</p>

<!-- GitHub Shields-->
<p align="center">
  <a href="https://github.com/narlock/Kaizen/commits/main"><img src="https://img.shields.io/github/last-commit/TamoStudy/TamoBot"></a>
  <a href="https://discord.gg/eEbEYbXaNS"><img src="https://discordapp.com/api/guilds/821757961830793236/widget.png?style=shield"></a>
</p>

<!-- Social Links -->
<p align="center">
  <a href="https://youtube.com/narlock" style="padding:10px;"><img src="https://i.imgur.com/5npSWBq.png" alt="YouTube"></a>
  <a href="https://instagram.com/narlockdev" style="padding:10px;"><img src="https://i.imgur.com/DCFiEHr.png" alt="Instagram"></a>
  <a href="https://patreon.com/narlock" style="padding:10px;"><img src="https://i.imgur.com/iXAguWQ.png" alt="Patreon"></a>
  <a href="https://twitter.com/narlockDev" style="padding:10px;"><img src="https://i.imgur.com/W8iSkd5.png"></a>
<p>

<hr><br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

**TamoBot**, based off of <a href='https://github.com/narlock/TamoStudy/'>TamoStudy</a>, is a multi-functional Discord bot designed to provide a variety of useful features to users. It includes a study/focus tracker, allowing users to earn Tamo tokens and track their study time. Users can also earn roles and view statistics related to their study/focus time. Additionally, TamoBot offers mini arcade games and profile customization options, allowing users to spend their earned tokens in fun and interactive ways.

TamoBot is designed to complement the user's Discord experience rather than replace the TamoStudy desktop application's functionality. Given the various complexities associated with Discord servers and commands, TamoBot offers a simple and intuitive command list to assist users.

Join the official <a href='https://discord.gg/eEbEYbXaNS'>**TamoBot** Discord Server</a>! (If you are interested in adding this bot to your server, join here and contact the developer!)

Show support for this project by leaving a ⭐️ on our repository!

- [Features](#features)
    - [Focus Time Tracking](#focus-time-tracking)
    - [Shop](#shop)
    - [Arcade](#arcade)
    - [General](#general)
- [Software Design](#software-design)
- [Original Concept Idea](#original-concept-idea)

## **Features**

### **Focus Time Tracking**
- The Focus Time Tracking feature allows for users to track their focus time while using the Discord server. Users can view their daily focus time, monthly focus time, and all time focus time utilizing the `/stats` command.
- The `/stats` command will give the user a brief description of their profile in relation to their focus performance on the server. The Bot will display a Discord Embed containing the relevant user data.

<p align="center">
<img src="./README%20Assets/Stats.png" style="border-radius: 20px;">
</p>

- By default, every `144` seconds spent in a specified list of 'focus' voice channels will earn the user a single Tamo token. Tamo tokens can be utilized for the interactive and customization functions that are described later in this feature list. Server administrators will be able to change this value, as well as set specified 'focus' voice channels.

- Users can utilize the `/top` command to view the all time leaders in focus time on the server.

<p align="center">
<img src="./README%20Assets/Top.png" style="border-radius: 20px;">
</p>

- Additionally, users can add parameters to this command. `/top month` will display the top users during the current month.

### **Shop**
- The Shop allows users to purchase cosmetic customization options to add flair to their experience utilizing TamoBot. By using the `/shop` command, the list of shop options will appear to the user.

<p align="center">
<img src="./README%20Assets/Shop.png" style="border-radius: 20px;">
</p>

- *Embed Profile Color Customization*: Utilizing `/shop embed`, the user can purchase a custom color embed to change the color of the Discord embed when a profile related command is called. By default, this costs the user `1000` Tamo tokens. Server administrators can modify this value.

- *Color Role*: Utilizing `/shop color`, the user can purchase a custom color role from a given list of colors. By default, this costs the user `500` Tamo tokens. Server administrators can modify this value, as well as specify the roles that are included for purchase.

### **Arcade**
- In addition to using Tamo tokens as a means to enhance the flair of the user's experience, TamoBot also provides interactive 'arcade-style' games for the user to enjoy during their downtime. To view the list of games in the arcade, the user can type `/arcade`. This command will direct the user for the cost of each game, as well as the command to play it. By default, the cost to play any arcade game is `100` Tamo tokens. Server administrators can modify this value.

<p align="center">
<img src="./README%20Assets/Arcade.png" style="border-radius: 20px;">
</p>

- During the development of Phase 1 of TamoBot, the current available arcade games are limited to:
    - Trivia `/trivia` - answer fun and simple trivia questions. Utilize `/trivia top` to view the leaderboard for most answered trivia questions.

### **General**
- TamoBot also provides general commands that are useful for all Discord servers. The user can utilize the `/help` command to view all of the bot's command at any time.

<p align="center">
<img src="./README%20Assets/Help.png" style="border-radius: 20px;">
</p>

- The following are some general commands the user can utilize via TamoBot.
    - `/rules` - View the rules of the server.
    - `/roll [number, default = 100]` - Randomly roll a number between an inclusive set of numbers ranging from 1 to a specified number.
    - `/8ball [question]` - Ask a question to the Magic 8 ball.
    - `/motivation [user (optional)]` - Motivate yourself and other members.

## **Software Design**
- The high-level software architecture for Phase 1 of TamoBot is shown below.
<p align="center">
<img src="./README%20Assets/UMLPhase1.png" width="800px" style="border-radius: 20px;">
</p>

- The primary functionality lies inside of the `main.py` file, where the initialization of the Discord bot exists as well as the connection to the back-end MySQL database.

- The following shows the entity-relationship diagram for Phase 1 of TamoBot.
<p align="center">
<img src="./README%20Assets/ERDPhase1.png" width="800px" style="border-radius: 20px;">
</p>

## **Original Concept Idea**
