import uuid
from datetime import datetime
vi = datetime.now()
created_at = vi.strftime('datetime.datetime(%Y, %m, %d, %H, %M, %S,)')
#created_at = f"datetime.datetime({vi.year}, {vi.month}, {vi.day}, {vi.hour}, {vi.minute}, {vi.second}, {vi.microsecond})"
x = uuid.uuid4()

print(created_at)