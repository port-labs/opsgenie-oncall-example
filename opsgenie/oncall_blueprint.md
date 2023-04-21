```json showLineNumbers
{
    "identifier": "opsgenie_oncall",
    "description": "This blueprint represents an OpsGenie on-call user in our software catalog",
    "title": "OpsGenie Oncall",
    "icon": "OpsGenie",
    "schema": {
      "properties": {
        "on_call": {
          "title": "Oncall User",
          "type": "string",
          "format": "user"
        },
        "user_type": {
          "title": "User Type",
          "type": "string",
          "enum": [
            "user",
            "team",
            "escalation"
          ]
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "relations": {}
  }
```