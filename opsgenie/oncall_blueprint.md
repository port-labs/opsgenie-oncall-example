```json showLineNumbers
{
  "identifier": "service",
  "description": "This blueprint represents a service in our software catalog",
  "title": "Service",
  "icon": "Service",
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
        "title": "GitLab URL",
        "icon": "GitLab",
        "format": "url",
        "default": "https://gitlab.com",
        "description": "the link to the repo in our GitLab"
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