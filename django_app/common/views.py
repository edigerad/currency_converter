from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import exception_handler


class DefaultAPIView(APIView):

    def get_response(self, context, response_status=status.HTTP_200_OK):
        return Response(context, status=response_status)

    def get_context(self, data=None, text='success'):
        context = {
            'message': {
                'text': text
            }
        }
        if data:
            context['data'] = data
        return context


def default_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        text = ''
        if response.data.get('non_field_errors'):
            text = response.data.get('non_field_errors')[0]
        if response.data.get('detail'):
            text = response.data.get('detail')
        response.data = {
            'message': {'text': text}
        }
        response.status_code = status.HTTP_400_BAD_REQUEST
    return response
