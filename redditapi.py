import requests
import os
# secret for the API

class redditAPI():
    def __init__(self,subreddit:str) -> None:
        self.outputPath = os.path.dirname(__file__)
        self.token = ""
        self.headers = {"Authorization" : f"Bearer {self.token}"}
        self.subreddit = subreddit
        pass

    def getRequst(self):
        url = ""
        response = requests.get(url,headers=self.headers)
        if response.status_code == 200:
            return response.json
        else:
            return 'Bad Request'

    def downloadImages(self) -> None:
        pass
        
    def getOutputPath(self) -> str:
        return self.outputPath

def main():
    test = redditAPI()
    # test.getFolderOutputLocation()
    pass

if __name__ == "__main__":
    main()