from datetime import datetime

def sample_responses(input_text):
	user_message= str(input_text).lower()
	if user_message in ('hello','hi','hey','hii'):
		return "Hey!, How doing!!"
	if user_message in ('who are you?','who are you'):
		return "I am AI_Mini_Project_Bot !!!"
	if user_message in ('time','time?','date'):
		now = datetime.now()
		date_time = now.strftime("%d/%m/%y, %H:%M:%S")
		return str(date_time)
	return "I don't understand you" 