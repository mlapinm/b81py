#schemas.py 

ITEM_SCHEMA = {
  '$schema': 'http://json-schema.org/schema#', 
  'type': 'object', 
  'properties': {
      "title": {
          'type': 'string',
          'minLength': 1,
          'maxLength': 64, 
      },
      "description": {
          'type': 'string',
          'minLength': 1,
          'maxLength': 1024, 
      },
      "price": {
          'type': 'integer',
          'minimum': 1, 
          'maximum': 1000000 
      },
  },
  'required': ['title', 'description', 'price']
}





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



