posts = {
    1: {
        "title": "Hello World!",
        "Description": "This is my first post!"
    },
    2: {
        "title": "San Francisco",
        "Description": "I love this city!"
    },
    3: {"title": "New York",
        "Description": "I love this city too!"
        }
}

class Post():
    def __init__(self, title, content):
        self.title = title
        self.description = content
    def to_json(self):
        return {
            "title": self.title,
            "description": self.description
        }
    def from_json(self, json):
        self.title = json["title"]
        self.description = json["description"]