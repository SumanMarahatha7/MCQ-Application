from rest_framework import serializers
from .models import Quiz, QuizTaker, Answer,Question, Response

class QuizListSerializer(serializers.ModelSerializer):
	# questions = serializers.RelatedField(many=True)
	questions_count = serializers.SerializerMethodField()
	class Meta:
		model = Quiz
		fields = ['id','name','description','slug','questions_count','questions']
		read_only_fields=['questions_count']

	def get_questions_count(self,obj):
		return obj.question_set.all().count()

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ['id','question','text']

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'



class UsersAnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Response
		fields='__all__'




class QuizTakerSerializer(serializers.ModelSerializer):
	user_answer_set = UsersAnswerSerializer(many=True)

	class Meta:
		model = QuizTaker
		fields = '__all__'


class QuizDetailSerializer(serializers.ModelSerializer):
	quiztakers_set = serializers.SerializerMethodField()
	question_set = QuestionSerializer(many=True)

	class Meta:
		model = Quiz
		fields ="__all__"

	def get_quitakers_set(self,obj):
		try:
			quiz_taker = QuizTaker.objects.get(user=self.context['request'].user,quiz=obj)
			serializer = QuizTakerSerailizer(quiz_taker)
			return serializer.data
		except QuizTaker.DoesNotExist:
			return None
