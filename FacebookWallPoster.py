"""
Created by Gotham on 10-06-2018.
"""
import facebook


class FacebookWallPoster:
    def __init__(self, access_token, version='2.7', profile_id='me'):
        self.profile_id = profile_id
        self.graph = facebook.GraphAPI(access_token=access_token, version=version)

    def construct_post(self, message, **kwargs):
        attachment = {key: value for key, value in kwargs.items() if value is not None}
        return {'message': message, 'attachment': attachment, 'profile_id': self.profile_id}

    def post_to_wall(self, message=None, name=None, link=None, caption=None, description=None, picture=None, id=None):
        """

        :param message: Message that should go along with the post
        :param name: name of attachment
        :param link: link of attachment
        :param caption: caption of attachment
        :param description: description of attachment
        :param picture: link of picture of attachment
        """
        kwargs = {
            'name': name,
            'link': link,
            'caption': caption,
            'description': description,
            'picture': picture
        }
        post = self.construct_post(message, **kwargs)
        self.graph.put_wall_post(**post)
        print(id)
