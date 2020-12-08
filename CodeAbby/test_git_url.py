import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import collections


def get_versions_from_git(token, release):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    header = {"Authorization": "Bearer {}".format(token),
              "Content-Type": "application/json"}
    url = "https://fsstash.evry.com/projects/ENTERPRISE_CR_AUTOTEST/repos/system-version-sync/raw/release-{}.json?at=refs%2Fheads%2Fdeployment".format(release)
    #url = "https://fsstash.evry.com/projects/ENTERPRISE_CR_AUTOTEST/repos/system-version-sync/raw/release-candidate.json?at=refs%2Fheads%2Fdeployment"
    try:
        r = requests.get(url, verify=False, headers=header)
    except Exception as err:
        print('Was not able to get versions: {}'.format(err))
        return None
    try:
        output = r.json()
    except Exception as err:
        print('Versions are not in proper JSON format: {}'.format(err))
    return collections.OrderedDict(output)

a = get_versions_from_git('NjgyMzcyMTA5MDA5OizC4o4ZojKLaYZgAjsS5k0QluP3', 2020.4)

print(a['versions'])




