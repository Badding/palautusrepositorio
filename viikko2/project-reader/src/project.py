class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.license = license
        self.authors = authors
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _arrToString(self, arr):
        return "\n".join(f"- {item}" for item in arr)
    
    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors:\n{self._arrToString(self.authors)}\n"
            f"\nDependencies:\n{self._arrToString(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n{self._arrToString(self.dev_dependencies)}"
        )
