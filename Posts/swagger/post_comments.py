from drf_yasg.utils import swagger_auto_schema
from Posts.serializers.post_comments import *


class PostCommentSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Post Comment"],
            operation_summary="Creates a New Comment",
            operation_description="Creates Comment using the details provided by the user",
            request_body=PostCommentCreateSerializer,
            responses={'200': PostCommentSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Post Comment"],
            operation_summary="Delete Comment",
            operation_description="Delete Comment using the details provided by the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Post Comment"],
            operation_summary="Update Comment",
            operation_description="Update Comment using the details provided by the user",
            request_body=PostCommentSerializer,
            responses={'200': PostCommentSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Post Comment"],
            operation_summary="List Comment",
            operation_description="list Comment using the details provided by the user",
            responses={200: PostCommentSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Post Comment"],
            operation_summary="Get Comment",
            operation_description="Get Comment using the details provided by the user",
            responses={200: PostCommentSerializer}
        )
        return doc
