## You might need to install following packages:
# pip install "chatterbot==1.0.0"
# pip install pytz
## Might need this help if error prompts related to "clock" https://github.com/gunthercox/ChatterBot/issues/2159
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

cbot = ChatBot('Solent Chatbot')
trainer = ChatterBotCorpusTrainer(cbot)

## Train the chatbot with English langauge
trainer.train("chatterbot.corpus.english")
print(cbot.get_response("Hello"))
#print(cbot.get_response("What is AI"))

## Your Task-1: Train your chatbot with Greetings in English language
#trainer.train("chatterbot.corpus.english.greetings")

## Your Task-2: Train your chatbot with language of your choice based on
## languages given in data folder
#trainer.train("chatterbot.corpus.french")

## Your Task-3: Train your chatbot with AI topic only
#trainer.train("chatterbot.corpus.ai")

## Your Task-4: Train your chatbot with updated AI corpus (.yml file)
## Step-1: Double click on ai.yml file and add following and save:
##        - - what is ML?
##          - Machine learning
##          - It stands for machine learning and it is part of AI
## Step-2: Make changes and add your own data.
## Step-2: Use your own corpus to train your chatbot.
#trainer.train("chatterbot.corpus.myCorpus")

## Your Task-5: Train your chatbot with your own created corpus (.yml file)
## Step-1: Take any .yml file from Lib folder and make a copy and place it on root folder
## Step-2: Make changes and add your own data.
## Step-3: Use your own corpus to train your chatbot.
#trainer.train("myCorpus")

## Let's make our chatbot ask user multiple queries
#name = input("Enter your name: ")
#print("Hi "+name+"! Welcome to the Solent Bot! How can I help you?")
#while True:
#    query = input(""+name+": ")
#    print(cbot.get_response(query)) ## This line will give you following warning everytime: No value for search_text was available on the provided input
    #if query == 'Bye' or query == 'bye':
    #    print('Solent Bot: Bye!')
    #    break
    #else:
    #    print("Solent Bot: ",cbot.get_response(Statement(text=query, search_text=query)))  ## To avoid warning
