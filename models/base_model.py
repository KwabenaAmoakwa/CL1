#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():
	
	def __init__(self, *args, **kwargs):
		if kwargs:
			for key, value in kwargs.items():
				if key != '__class__':
					if key in ['created_at', 'updated_at']:
						setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
					else:
						setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = str(datetime.now())
			self.updated_at = str(datetime.now())
		
	
	def __str__(self):
		print(f"[{self.__class__.__name__}]({self.id}) {self.__dict__}")
	
	def save(self):
		self.updated_at = datetime.now()
	
	def to_dict(self):
		obj_dict = self.__dict__
		obj_dict['created_at'] = self.created_at.isoformat()
		obj_dict['updated_at'] = self.updated_at.isoformat()
		obj_dict['__class__'] = self.__class__.__name__
		return obj_dict
	
if __name__ == "__main__":
    base_model_instance = BaseModel()
    print(base_model_instance)