# Welcome To Feed Dor's Addiction FPL League Repo


## Instructions to run the Weekly Matches Printer:
  1. install project requirements with 
```pip3 install -r requirements.txt``` 
  3. Set the follow variables as the environment variables:
  
    - EMAIL
    - FPL_PWD
    - H2H_LEAGUE_ID
    - GAME_WEEK
    - WHATSAPP_GROUP_ID (instructions can be found: https://www.alphr.com/whatsapp-find-group/)
    
  2. To run the project from IDEA: run  __main()__ from sendGameWeekReport.py.
### Instructions for schedule the "Game Week Report": 
1. run from the terminal the follow command:
   ```crontab -e```
2. this will open a vim editor for your scheduled jobs, past there the content of cron/crontab and replace the 
   environment variables.
   
