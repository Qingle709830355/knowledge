from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from index.models import UserModel


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        统一验证登录

        :param request:
        :return:
        """
        a = request.path
        if request.path == '/uauth/logout/' or request.path == '/uauth/login/':
            return None
        ticket = request.COOKIES.get('ticket')
        if request.path == '/axf/cart/':
            if not ticket:
                return HttpResponseRedirect('/uauth/login')
        else:

            if not ticket:
                return None

        users = UserModel.objects.filter(u_ticket=ticket)

        if not users:
            response = HttpResponseRedirect('/axf/mine')
            ticket = request.COOKIES.get('ticket')
            response.delete_cookie('ticket')
            return response

        request.user = users[0]
