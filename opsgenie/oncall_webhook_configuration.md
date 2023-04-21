```json showLineNumbers
 {
    "identifier": "opsgenieOncallMapper",
    "title": "OpsGenie Oncall Mapper",
    "description": "A webhook configuration to map OpsGenie Oncall to Port",
    "icon": "OpsGenie",
    "mappings": [
        {
            "blueprint": "opsgenie_oncall",
            "entity": {
                "identifier": ".body.identifier",
                "title": ".body.title",
                "properties": {
                    "on_call": ".body.on_call",
                    "user_type": ".body.user_type"
                }
            }
        }
    ],
    "enabled": true,
    "security": {}
}
```