from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return obj.author.email


class ThinNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'url')

    url = serializers.HyperlinkedIdentityField(view_name='notes-detail')  # url для перехода к записи

# class NoteSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=255)
#     text = serializers.CharField(required=False, allow_blank=True)
#
#     def create(self, validated_data):
#         return Note.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('title', instance.text)
#         instance.save()
#         return instance


# Serialization
# from rest_framework.renderers import JSONRenderer
# import io
# from rest_framework.parsers import JSONParser
# s = Serializer(Model.objects.all(), many=True)
# s.data -> OrderedDict
# json_content = JSONRenderer().render(s.data) -> JSON

# Deserialization
# stream = io.BytesIO(json_content)
# data = JSONParser().parse(stream) -> [{'id': 1, 'title': 'title1', 'text': 'text1'}]
# s = Serializer(data=data)
# s.is_valid() -> True
# s.validated_data -> {'id': 1, 'title': 'title1', 'text': 'text1')}
