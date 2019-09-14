import requests

class SMS:
    def __init__(self, url='http://66.45.237.70/api.php', username='forhad', password='forhad12'):
        self.url = url
        self.username = username
        self.password = password
    
    def validate(self):
        if not self.url:
            raise ValueError('url cannot be None')

        if not self.username:
            raise ValueError('username cannot be empty')

        if not self.password:
            raise ValueError('password cannot be empty')
    
    def send(self, number=None, text=None):
        data = {}
        self.validate()
        data['username'] = self.username
        data['password'] = self.password
        
        if not number:
            raise ValueError('number is required')

        data['number'] = number
        data['message'] = text

        response = requests.post(self.url, data=data)
        response.raise_for_status()
        print(response.status_code)
        return True

