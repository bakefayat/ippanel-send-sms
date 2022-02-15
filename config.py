from decouple import config
# rename the .env-sample file to .env and replace your information.
api_key = config("API_KEY")
# pattern id -> unique id of pattern. ask sms panel provider.
pid = config("PID")
sender = '3000505'
