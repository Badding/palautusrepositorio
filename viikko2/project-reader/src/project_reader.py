from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        deserialize = tomli.loads(content)

        name = deserialize['tool']['poetry']['name']
        description = deserialize['tool']['poetry']['description']
        license = deserialize['tool']['poetry']['license']
        authors = deserialize['tool']['poetry']['authors']
        dependencies = deserialize['tool']['poetry']['dependencies']
        dev_dependencies = deserialize['tool']['poetry']['group']['dev']['dependencies']

        return Project(name, description, license, authors, dependencies, dev_dependencies)

    def printProject(self, project):
        def _printLoop(label, arr):
            print()
            print(label)
            for item in arr:
                print(f"- {item}")
            print()
        
        print(f"Name: {project['tool']['poetry']['name']}")
        print(f"Description: {project['tool']['poetry']['description']}")
        print(f"Licese: {project['tool']['poetry']['license']}")

        _printLoop("Authors:", project['tool']['poetry']['authors'])
        
        _printLoop("Dependencies:", project['tool']['poetry']['dependencies'])

        _printLoop("Dev dependencies:", project['tool']['poetry']['group']['dev']['dependencies'])

        