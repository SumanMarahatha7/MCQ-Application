from django.contrib import admin
from .models import Quiz,Question,Answer,Response, QuizTaker
import nested_admin


class AnswerInline(admin.StackedInline):
    model = Answer
    max_num = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

# class ResponseInline(admin.TabularInline):
#  model = Response

# class QuizTakersAdmin(admin.ModelAdmin):
#     inlines = [
#     	ResponseInline,
#     ]

# class QuizAdmin(nested_admin.NestedModelAdmin):
#  	inlines = [
#  		QuestionInline,
#  	]

class AnswerInline(nested_admin.NestedTabularInline):
 model = Answer
 max_num = 4

class QuestionInline(nested_admin.NestedTabularInline):
 model = Question
 inlines = [AnswerInline,]
 extra = 1

class QuizAdmin(nested_admin.NestedModelAdmin):
 inlines = [QuestionInline,]

class ResponseInline(admin.TabularInline):
 model = Response

class QuizTakersAdmin(admin.ModelAdmin):
 inlines = [ResponseInline,]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(QuizTaker, QuizTakersAdmin)
admin.site.register(Response)

