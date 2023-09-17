# 📅 Add batches of tasks to Your Google Calendar

## 📝 Introduction

This repository provides a simple script to add courses and other events to your Google Calendar using the Google Calendar API. By following the steps below, you can easily configure the API, install the necessary requirements, and customize the script to fit your needs.

## 🚀 Getting Started

### Step 1: Configure the Google Calendar API

Before proceeding, make sure you have properly configured the Google Calendar API. If you haven't done so, please refer to this [short guide](https://telegra.ph/Configure-Google-Calendar-REST-API-09-17) for detailed instructions.

### Step 2: Install Requirements

To install the required dependencies, run the following command:

```shell
pip install -r requirements.txt
```

Note: If you prefer working within a virtual environment, you can create one using the command `python -m venv <virtual environment name>`. It is recommended for more experienced users, but if you are a novice, the direct installation method is sufficient.

### Step 3: Customize the Script

Open the "add_courses.py" file and make the following changes:

- Replace `my_email` with your own email address.
- Modify the parameters in the "add_courses.py" according to your preferences.

### Step 4: Run the Script

To add the courses to your Google Calendar, execute the following command:

```shell
python add_courses.py
```

That's it! The script will now add the specified courses and events to your Google Calendar. Enjoy your organized schedule! 🎉
