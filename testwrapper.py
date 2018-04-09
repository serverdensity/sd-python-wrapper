from serverdensity.wrapper import ApiClient
from serverdensity.wrapper import Alert
from serverdensity.wrapper import Metrics
import datetime

token = '8dacb989701647c8c5aaf81713f8442b'
payload = {
        'metric': 'system.disk.free',
        'section': 'system',
        'comparison': 'gte',
        'enabled': True,
        'value': 50,
        'recipients': 
            [],
        'wait':
            {
                "seconds": 60,
                "enabled": True,
                "displayUnits": "s"
            },
        'repeat':
            {
                "seconds": 300,
                "enabled": True,
                "displayUnits": "s"
            },
        'scope':
        	{
        		"type": "device", "value": "5a4e2768b03e85fe048b456b"
        	},
        'tags':
        	{
        		"device_name": {"type": "eq", "value": "/dev"}
        	},

        'fix': '1'
    }

client = ApiClient(token)
device = client.metrics.available(start=datetime.datetime(2018, 03, 28, 12, 0), end=datetime.datetime(2018, 03, 29, 12, 0), filtering=[{"metric":"system.load.1","aggregation":"avg"}])

print device