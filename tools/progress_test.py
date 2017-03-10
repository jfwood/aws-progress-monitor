import redis
import random
from progressmagician import RedisProgressManager, ProgressMagician, ProgressTracker


pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
rpm = RedisProgressManager(RedisConnection=r)
pm = ProgressMagician(DbConnection=rpm)
def create_children(t, n):
    r = random.randint(0, 10)
    i = 0
    while i < n:
        c = ProgressTracker()
        t.with_tracker(c)
        # if r == 0:
        #    c.start(Parents=True)
        i = i + 1


t = ProgressTracker()
pm.with_tracker(t)
create_children(t, 100)
for c in t.all_children:
    create_children(c, 50)
print t.all_children_count
print t.in_progress_count
print t.in_progress_pct
print 'updating;'
pm.update_all()
print 'updating again;'
pm.update_all()
l = pm.load(pm.id)
print pm.all_children_count
print l.all_children_count
