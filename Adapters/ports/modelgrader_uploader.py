import requests

PORT = 8004

def upload(modelGraderDict):
    try:
        print(f"Uploading {modelGraderDict['title']} Response...",end="")
        response = requests.post(f'http://localhost:{PORT}/api/accounts/4/problems',json=modelGraderDict)
        print(f"{response}")
    except Exception as err:
        print(f"<Error []>\n{err}")