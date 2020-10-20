# ClockySAP

## How to import your Clockify time tracker entries to SAP

 * Create a CSV file to map ticket IDs to Clockify projects + activities. The file must have 2 columns:

| Ticket | Beschreibung |
|--------|--------------|
|ID of the ticket| Key consisting of "&lt;Clockify project> &lt;Clockify activity>"|


 * Install python 3.x on your system
   * MacOS 10.14+: Python 3 should already be installed
   * Debian/Ubuntu Linux: ```sudo apt-get install python3-pip```
   * SuSE/CentOS/RedHat Linux: ```sudo yum install python34-setuptools
&& sudo easy_install-3.4 pip```
   * Windows 10: Download Python from here: https://www.python.org/downloads/windows/, then install pip using this script: https://bootstrap.pypa.io/get-pip.py
   
* Install Google Chrome: https://www.google.com/chrome/
* Install Node.JS on your system. Refer to nodejs.org for instructions
* Install the Chrome driver for Selenium: ```npm install -g chromedriver``` 
* Install the script + required packages on your system

```pip3 install git+https://github.com/zudljk/clockysap.git```

* Run the script in a terminal / cmd:

```clockysap --clockify-apikey <APIKEY> --role <ROLE> --ticketmapping <TICKETMAPPING_FILE>```

| Parameter | Description |
|-----------|--------------|
|clockify-apikey|The API key for your Clockify account, get it here: https://clockify.me/user/settings|
|role|The role to use for the ticket entries, e.g. "02 Consultant"|
|ticketmapping|A CSV file containing the mapping from projects/activities to tickets (see above)|

* When you run the script, a Chrome window will appear, asking for your SAP credentials.

* After entering the credentials, you will be on the portal landing page.

* Select the time registration tile.

* The script will now start to import your time entries. You will need to confirm every creation of a time entry. To abort the procedure, simply close the Chrome window.

## Known issues

* It is currently not possible to resume an aborted import. You will need to delete all entries of the current month and start over.

* It is currently not possible to make incremental imports. The script ALWAYS imports a whole months. Run the script only once per month to avoid duplicates.

* All entries from the current month will be imported. There is currently no possibility to select a different time range.