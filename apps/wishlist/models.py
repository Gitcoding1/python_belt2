from __future__ import unicode_literals
from ..login.models import User
from django.db import models

class WishManager(models.Manager):
	def validate(self, form_data):
		errors = []
		description = form_data['description']

		if len(description) == 0:
			errors.append(" must insert a product name")
		if len(description) < 3:
			errors.append(" The item has to be 3 characters long")

		return errors

	def add_wish(self, wish_id, user_id):
		user = User.objects.get(id= user_id)
		item = Wish.objects.get(id= wish_id)
		user.wishes.add(item)


	def remove_wish(self, wish_id, user_id):
		user = User.objects.get(id= user_id)
		item = Wish.objects.get(id= wish_id)
		user.wishes.remove(item)


	def create_wish(self, form_data, user_id):
		user = User.objects.get(id=user_id)
		wish = self.create(
		description = form_data['description'],
		added_by = user
		)
		return wish

	def delete_wish(self, wish_id):
		item = Wish.objects.get(id= wish_id).delete()


class Wish(models.Model):
	description = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	added_by = models.ForeignKey(User, related_name="added_items")
	wished_by = models.ManyToManyField(User, related_name="wishes")
	objects = WishManager()

	def __str__(self):
		return "{} {} {}".format(self.description, self.added_by, self.wished_by)
