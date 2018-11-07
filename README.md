# Foodie Restaurant Bot

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. 

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. 

Zomato apis are used for searching the restaurants. https://developers.zomato.com/documentation#/


YOUTUBE VIDEO LINK: https://youtu.be/VLCtS9yszFg



### Prerequisites

python 3.6.x(except 3.6.6)
Visual studio for python development 
Rasa_nlu version 0.13.7 (latest) 
Rasa_core version 0.12.0a4 

### Installing ---- How to Run:


## What to Install

#### Install Rasa NLU

`$pip install rasa_nlu`

#### Install Rasa Core

I am installing from Git.

```

$git clone https://github.com/RasaHQ/rasa_core.git
$cd rasa_core
$pip install -r requirements.txt
$pip install -e .
```

#### How to find rasa_core and rasa_nlu version

```
$python -c "import rasa_nlu; print(rasa_nlu.__version__);"
$python -c "import rasa_core; print(rasa_core.__version__);"
```

## Train the nlu data & train the core conversational flow using command line

cd path <path to project>

### train the NLU
$python .\nlu_model.py

### train Core
$python .\train_init.py

### Run Dialogue management
	
	Step 1: run the action server
	```
		python -m rasa_core_sdk.endpoint --actions actions
	```
	Step 2: run the RASA Core
	```
		python -m rasa_core.run --nlu models/nlu/default/restaurantnlu --core models/dialogue --endpoints endpoints.yml
	```

### Slack Integration
	```
	python -m rasa_core.run -d models/dialogue -u models/nlu/default/restaurantnlu --endpoints endpoints.yml --port 5002 --connector slack --credentials slack_credentials.yml
	```


## Train the nlu data & train the core conversational flow using python code

cd path <path to project>
$python .\nlu_model.py

$python .\train_init.py

### verify the bot command line

$python .\dialogue_management_model.py

```

### train dialogue flow online and add the strories

$python .\train_online.py

```
Generated stories can be exported to a path and then added to stories.md. Retrain the model and check dialogue flow.
```

## Deployment to slack

run the bot on local sever and integrate with slack.

Using ngrok (https://ngrok.com/download) as a webhook deploy the bot on slack(https://slack.com/). Create a bot in slack and integrate the credentials in run_app.py program.

$python .\run_app.py  

Bot can be accessed from slack. 

 

## Built With

* Rasa
* Keras Framework
* Tensorflow
* Slack


## Authors

* **Anurag Singh**

## License

 ---- NA ----------
