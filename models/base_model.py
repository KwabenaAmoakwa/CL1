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
			vi = datetime.now()
			self.id = str(uuid.uuid4())
			self.created_at = vi.strftime('datetime.datetime(%Y, %m, %d, %H, %M, %S,)')
			self.updated_at = vi.strftime('datetime.datetime(%Y, %m, %d, %H, %M, %S,)')
	
	def __str__(self):
		return f"[{self.__class__.__name__}]({self.id}) {self.__dict__}"
	
	def save(self):
		self.updated_at = datetime.now()
	
	def to_dict(self):
		obj_dict = self.__dict__
		obj_dict['created_at'] = datetime.now().isoformat()
		obj_dict['updated_at'] = datetime.now().isoformat()
		obj_dict['__class__'] = self.__class__.__name__
		return obj_dict
	
if __name__ == "__main__":
    base_model_instance = BaseModel()
    print(base_model_instance)