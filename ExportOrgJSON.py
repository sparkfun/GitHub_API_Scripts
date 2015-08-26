#Demo script showing basic functionality of [agithub](https://github.com/jpaugh/agithub) Python module
#Toni @SparkFun Electronics 2015
#Please review the LICENSE.md file for license information

import json
from agithub import Github

g = Github(token='<Access Token>')
OrgInfo = g.orgs.<Organziation Name>.get()

with open('Organization.json', 'w') as outfile:
	json.dump([OrgInfo], outfile, separators=(',',':'), sort_keys=True, indent=4)
