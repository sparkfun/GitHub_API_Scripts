#Demo script showing basic functionality of [agithub](https://github.com/jpaugh/agithub) Python module
#Toni @SparkFun Electronics 2015
#Please review the LICENSE.md file for license information

import json
from agithub import Github

g = Github(token='<Access Token>')
UserInfo = g.users.<User Name>.get()

with open('User.json', 'w') as outfile:
	json.dump([UserInfo], outfile, separators=(',',':'), sort_keys=True, indent=4)