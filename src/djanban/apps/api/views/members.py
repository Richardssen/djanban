# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.http import JsonResponse

from djanban.apps.api.http import JsonResponseMethodNotAllowed
from djanban.apps.api.serializers import Serializer
from djanban.apps.base.decorators import member_required


# Get available members
@member_required
def get_members(request):

    if request.method != "GET":
        return JsonResponseMethodNotAllowed({"message": "HTTP method not allowed."})

    current_member = request.user.member
    members = current_member.viewable_members

    serializer = Serializer()

    response_json = [serializer.serialize_member(member) for member in members]
    return JsonResponse(response_json, safe=False)