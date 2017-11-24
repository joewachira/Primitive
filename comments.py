__author__ = 'joe'

import requests


def add_comment(self, post_id, title, body):
	# This method will make an API call to add a comment to a given post

	data = {"id": post_id, "title": title, "body": body}
	try:
		resp = requests.post('http://34.207.10.230:3000/comments', json=data)
		if resp.status_code == 200:
			# this means the post was made successfully
			return {"content": resp.content,
					"message": "post added successfully"}
		else:
			return {"content": resp.content,
					"message": "failed to add a comment"}

	except requests.exceptions.RequestException as e:
		return {"content": None, "message": "Error: {}".format(e)}