#schemas.py 

REVIEW_SCHEMA = {
  '$schema': 'http://json-schema.org/schema#', 
  'type': 'object', 
  'properties': {
      "text": {
          'type': 'string',
          'minLength': 1,
          'maxLength': 1024, 
      },
      "grade": {
          'type': 'integer',
          'minimum': 1, 
          'maximum': 10 
      },
  },
  'required': ['text', 'grade']
}

