
from first_web.www import orm
from first_web.www.models import User, Blog, Comment
import asyncio

async def test_save(loop):
    await orm.create_pool(loop=loop, user='root', password='password', db='awesome')
    u = User(name='Test1', email='test1@exmple.com',passwd='888888', image='about:blank')
    await u.save()

async def test_get(loop):
    await orm.create_pool(loop, user='root', password='password', db='awesome')
    U = await User().findAll()
    print(U)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [test_save(loop), test_get(loop)]
    loop.run_until_complete(asyncio.wait(tasks))
    print('Test finished')
