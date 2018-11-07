from rasa_slack_connector import SlackInput
from rasa_core.channels.channel import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-462633319383-4617723817957-462990291990-0e9fe2873de8ea28051f3ecce978b08e', #app verification token
							'xoxb-462633319383-46178426864231-4hPvkcIFZDtvZbqHlc082i3Y', # bot verification token
							'8ajLnkhZaUxh6ATMJNl49v65avM', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))