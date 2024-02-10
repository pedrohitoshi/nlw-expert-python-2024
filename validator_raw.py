from cerberus import Validator

body = {
    "data": {
        "elemento1": 123.90,
        "elemento2": "Olá Mundo",
        "elemento3": [123, '456', 12.98]
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": { "type": "float", "required": True, "empty": False },
            "elemento2": { "type": "string", "required": True, "empty": True },
            "elemento3": { "type": "list", "required": False, "empty": False }
        }
    }
})


response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print('Body OK')
