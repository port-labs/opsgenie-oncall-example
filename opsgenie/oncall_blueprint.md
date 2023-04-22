```json showLineNumbers
{
  "identifier": "opsGenieMicroservice",
  "description": "This blueprint represents an OpsGenie on-call service in our software catalog",
  "title": "OpsGenie Service",
  "icon": "Microservice",
  "schema": {
    "properties": {
      "on_call_user": {
        "type": "string",
        "icon": "Okta",
        "title": "On Call User",
        "format": "email",
        "default": "developer@getport.io"
      },
      "on_call_team": {
        "type": "string",
        "icon": "Okta",
        "title": "On Call Team",
        "default": "Developer Team"
      },
      "language": {
        "type": "string",
        "icon": "Git",
        "title": "Language",
        "default": "Node",
        "enum": [
          "GO",
          "Python",
          "Node"
        ],
        "enumColors": {
          "GO": "red",
          "Python": "green",
          "Node": "blue"
        }
      },
      "url": {
        "type": "string",
        "title": "Github URL",
        "icon": "Github",
        "format": "url",
        "default": "https://git.com",
        "description": "the link to the repo in our github"
      }
    },
    "required": [
      "on_call_user"
    ]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```