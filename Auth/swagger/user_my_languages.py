from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_my_languages import MyLanguageSerializer, MyLanguageCreateSerializer


class MyLanguageSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["My Languages"],
            operation_summary="Add a User Language",
            operation_description="Add a language by the user",
            request_body=MyLanguageCreateSerializer,
            responses={200: MyLanguageSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["My Languages"],
            operation_summary="Delete a User Language",
            operation_description="Deletes a language by the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["My Languages"],
            operation_summary="Updates a User Language",
            operation_description="Updates a language by the user",
            request_body=MyLanguageCreateSerializer,
            responses={200: MyLanguageSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["My Languages"],
            operation_summary="Lists All User Languages",
            operation_description="Lists all languages added by the user",
            responses={200: MyLanguageSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["My Languages"],
            operation_summary="Retireve a User Language",
            operation_description="Retrieve a language by the user",
            responses={200: MyLanguageSerializer}
        )
        return doc
