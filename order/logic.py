from order.services.order_services import OrderService
from order.services.point_of_issue_services import PointOfIssueService


class OrderLogic:
    order_service = OrderService()
    point_of_issue_service = PointOfIssueService()   

    def create_order(self, order_data, point_of_issue_data):
        order = self.order_service.create_order(order_data)
        for address in point_of_issue_data:
            if not address:
                continue
            address = self.point_of_issue_service.create_address(address)
            order.addresses.add(address)
        return order.save()


        
