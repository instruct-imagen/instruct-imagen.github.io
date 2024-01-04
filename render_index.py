import json
from jinja2 import Template

# Load webpage data
with open('data/metadata.json', 'r') as fd:
    metadata = json.load(fd)

# Load the template from a file or a string
with open('index.template.html', 'r') as fd:
    template = Template(fd.read())

# Render the template with the variables
output = template.render(**metadata)

# Output the resulting HTML
with open('index.html', 'w') as fd:
    fd.write(output)