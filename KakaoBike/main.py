from textwrap import dedent
import json
import requests
from config import BASE_URL, X_AUTH_TOKEN

def start(problem, base_url, x_auth_token):
    response = requests.post(url= f'{base_url}/start', json= {'problem': problem},
                             headers={'X-Auth-Token': x_auth_token})
    return response.json()

class KakaoBike:
    def __init__(self, base_url, x_auth_token, problem = 1):
        self.base_url = base_url
        self.x_auth_token = x_auth_token
        self.problem = problem
        start_info = self.start()
        self.auth_key = start_info['auth_key']
        self.time = start_info['time']
        self.default_header = {'Authorization': self.auth_key}

    def start(self):
        response = requests.post(url=f'{self.base_url}/start',
                                 json= {'problem': self.problem},
                                 headers= {'X-Auth-Token': self.x_auth_token})
        return response.json()

    def locations(self):
        response = requests.get(url=f'{self.base_url}/locations',
                                headers= self.default_header)
        return response.json()

    def trucks(self):
        response = requests.get(url=f'{self.base_url}/trucks',
                                headers= self.default_header)
        return response.json()

    def score(self):
        response = requests.get(url=f'{self.base_url}/score',
                                headers= self.default_header)
        return response.json()

    def simualte(self, commands: list[(int, list[int])]):
        commands_mapped = list(map(lambda tup: {'truck_id': tup[0], 'command': tup[1]},
                              commands))
        response = requests.put(url=f'{self.base_url}/simulate',
                                json= {'commands': commands_mapped },
                                headers= self.default_header)
        return response.json()

    def __str__(self):
        return dedent(f"""
            [Kakaobike]
                base_url: {self.base_url}
                x_auth_token: {self.x_auth_token}
                auth_key: {self.auth_key}
                problem: {self.problem}
                time: {self.time}""".strip('\n'))


if __name__ == '__main__':
    kakaoBike = KakaoBike(BASE_URL, X_AUTH_TOKEN)
    print(kakaoBike)
    print()
    print(json.dumps(kakaoBike.locations(), sort_keys=True, indent=2))
    print(json.dumps(kakaoBike.trucks(), sort_keys=True, indent=2))
    print(json.dumps(kakaoBike.score(), sort_keys=True, indent=2))
    print(json.dumps(kakaoBike.simualte([
        (0, [2, 5, 4, 1, 6])
    ])))
