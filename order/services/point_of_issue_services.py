from django.db import IntegrityError

from order.models import PointOfIssue


class PointOfIssueService:
    def create_address(self, point_of_issue_data):
        try:
            return PointOfIssue.objects.create(**point_of_issue_data)
        except IntegrityError:
            return self.get_address_by_title(title=point_of_issue_data['title'])

    def get_address_by_title(self, title):
        try:
            return PointOfIssue.objects.get(title=title)
        except PointOfIssue.DoesNotExist:
            return ''