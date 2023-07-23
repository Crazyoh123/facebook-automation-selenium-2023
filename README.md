# Facebook Interaction Script using Selenium<br>

This is a Python script that uses Selenium to interact with Facebook. The script can perform the following tasks:<br>
<br>
1. Check if a given username is a Facebook Page or a Facebook ID.<br>
2. If the username is a Facebook Page, the script will log in to Facebook and perform a series of actions, such as liking a post and sending a direct message to the page.<br>
3. If the username is a Facebook ID, the script will log in to Facebook and perform a series of actions, such as sending a direct message to the user.<br>
<br>
## Requirements<br>

- Python 3<br>
- Selenium WebDriver<br>
- ChromeDriver (Make sure to have the appropriate version compatible with your Chrome browser)<br>

## Setup<br>

1. Clone this repository to your local machine.<br>
2. Install the required Python packages using the following command:<br>
        **pip install pandas selenium<br>
3. Download the appropriate ChromeDriver version for your Chrome browser and place it in the same directory as the script.<br>

## Usage:<br>

1. Make sure you have a valid Facebook account and login credentials.:<br>
2. Prepare a sample Excel file with a list of usernames (Facebook Pages or IDs) you want to interact with. The file should be in `.xls` format.:<br>
3. Update the file path to your sample Excel file in the script::<br>

```python:<br>
data = pd.read_excel('/path/to/your/sample.xls'):<br>

Run the script using the following command:<br>
python your_script_name.py<br>

Disclaimer<br>
This script is for educational and personal use only. It is against Facebook's terms of service to use automated scripts to interact with the platform. Use this script at your own risk, and be aware of the potential consequences of violating Facebook's policies.<br>
