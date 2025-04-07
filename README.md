
# OpenTicket

Almost fully customizable Discord bot for ticket management on a single Discord server
Features:
- Use of Discord modals to provide a good user interface
- Ticket archiving (Not implemented)
- Simplified ticket moderation




## Screenshots

![Help Category Selection](https://github.com/simonchanay/OpenTicket/blob/main/statics/images/screenshot1.png)

![Modal example](https://github.com/simonchanay/OpenTicket/blob/main/statics/images/screenshot2.png)
## Installation

Installing the Discord bot:
- Download the project
- Create a virtual environment
- Create a .config file at the root level and add the line `TOKEN = "YourBotTokenHere"`
- In the config.json file, replace the IDs of the two Discord categories with your own
## Usage/Examples

- To generate the help category selection menu, issue the command `/sendselection <room name>` (Administrator permissions required)
- To close a ticket, click the red button or run the command `/closeticket <name of the ticket>`(Administrator permissions required)


## FAQ

#### Can it be used on multiple different servers?

For now no, it can only be used for one server!

#### How does ticket archiving work?

This feature is not implemented yet.





## Authors

- [@simonchanay](https://www.github.com/simonchanay)

