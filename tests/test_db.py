import unittest
from peewee import *
from app import TimelinePost
from playhouse.shortcuts import model_to_dict
import datetime

MODELS = [TimelinePost]

#use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list
        #of all models, we do not need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

        # self.first_post = TimelinePost.create(name='John Doe', email='john@example.com',
        # content='Hellow world, I\'m John!')
        # self.second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com',
        # content='Hello World, I\'m Jane!')

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only
        # live for the duration of the connection, and in the next step
        # we close the connection... but a good practice all the same

        test_db.drop_tables(MODELS)

        # close connection to db
        test_db.close()
    

    '''
    def test_timeline_post(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(name='John Doe', email='john@example.com',
        content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com',
        content='Hello World, I\'m Jane!')
        assert second_post.id == 2

        #get timeline posts and assert they are correct
    def test_timeline_get(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com',
        content='Hello world, I\'m John!')
        
        def get_time_line_post():
            return {
                'timeline_posts': [
                    model_to_dict(p)
                    for p in
                    TimelinePost.select().order_by(TimelinePost.created_at.desc())
                ]
            }
        # TimelinePost.created_at.replace(microsecond=0)
        first_get = get_time_line_post()
        expected_output = {
            'timeline_posts': 
            [
                {'id': 1, 
                'name': 'John Doe', 
                'email': 'john@example.com', 
                'content': "Hello world, I'm John!", 
                'created_at': datetime.datetime.now()
                }
            ]
            }
        #replace(second=0, microsecond=0)
        first_get["timeline_posts"][0]["created_at"] = first_get["timeline_posts"][0]["created_at"].replace(microsecond=0)
        expected_output["timeline_posts"][0]["created_at"] = expected_output["timeline_posts"][0]["created_at"].replace(microsecond=0)
        self.assertEqual(first_get, expected_output)

        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com',
        content='Hello World, I\'m Jane!')

        second_get = get_time_line_post()
        expected_output2 = {
            'timeline_posts': 
            [
                {'id': 2, 
                'name': 'Jane Doe', 
                'email': 'jane@example.com', 
                'content': "Hello World, I'm Jane!", 
                'created_at': datetime.datetime.now()
                },
                {'id': 1, 
                'name': 'John Doe', 
                'email': 'john@example.com', 
                'content': "Hello world, I'm John!", 
                'created_at': datetime.datetime.now()
                }
            ]
            }
        second_get["timeline_posts"][0]["created_at"] = second_get["timeline_posts"][0]["created_at"].replace(second=0,microsecond=0)
        second_get["timeline_posts"][1]["created_at"] = second_get["timeline_posts"][1]["created_at"].replace(second=0,microsecond=0)
        expected_output2["timeline_posts"][0]["created_at"] = expected_output2["timeline_posts"][0]["created_at"].replace(second=0,microsecond=0)
        expected_output2["timeline_posts"][1]["created_at"] = expected_output2["timeline_posts"][1]["created_at"].replace(second=0,microsecond=0)
        self.assertEqual(second_get, expected_output2)
    '''