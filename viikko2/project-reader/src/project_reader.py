from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_data = toml.loads(content)
        
        project = Project(
            name=parsed_data['tool']['poetry']['name'],
            description=parsed_data['tool']['poetry']['description'],
            license=parsed_data['tool']['poetry']['license'],  
            authors=parsed_data['tool']['poetry']['authors'],  
            dependencies=list(parsed_data['tool']['poetry']['dependencies'].keys()),
            dev_dependencies=list(parsed_data['tool']['poetry']['group']['dev']['dependencies'].keys())
        )
        
        return project 

class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def __str__(self):
        return f"""Name: {self.name}
Description: {self.description}
License: {self.license}

Authors:
{self.format_list(self.authors)}

Dependencies:
{self.format_list(self.dependencies)}

Development dependencies:
{self.format_list(self.dev_dependencies)}"""

    def format_list(self, items):
        return '\n'.join(f"- {item}" for item in items)
