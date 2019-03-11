import datetime
import json

import discord
from discord import *

MuteDataFilePath = "mute.json"

muteList = []
class Muted:
	def __init__(self, user, when):
		self.user = user
		self.endOfMute = when
	
	def __lt__ (self, other):
		if(endOfMute != other.endOfMute):
			return endOfMute < other.endOfMute
		return self.user.id < other.user.id
	
	def __gt__ (self, other):
		if(endOfMute != other.endOfMute):
			return endOfMute > other.endOfMute
		return self.user.id > other.user.id
	
	def increase_mute_length(penalty):
		endOfMute = endOfMute + penalty;
	
	def toJSON(self):
		return json.dumps(self, default=lambda o : o.__dict__, sort_keys=True, indent=4)

def encode_datetime(dt):
	if isinstance(dt, datetime.datetime):
		return (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
	else:
		raise TypeError("Object of type {dt.__class__.__name__} is not compatible with encode_datetime")
def encode_Muted(x):
	if isinstance(x, Muted):
		return (x.user, encode_datetime(x.endOfMute))
	else:
		raise TypeError("Object of type {dt.__class__.__name__} is not compatible with encode_Muted")


def save():
	with open(MuteDataFilePath, "w") as write_file:
		for x in muteList:
			json.dump(x, write_file, default=encode_Muted, sort_keys=True, indent=2)

muteList.append(Muted(1234, datetime.datetime(2009, 3, 10).now()))
save()

