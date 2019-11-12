from django.contrib import admin

# Register your models here.

from .models import network_communication_career, multimedia_career, Fields_of_study_or_course_name, minimum_admission_requirement,applications_development_career
# Register your models here.
admin.site.register(applications_development_career)
admin.site.register(network_communication_career)
admin.site.register(multimedia_career)
admin.site.register(Fields_of_study_or_course_name)
admin.site.register(minimum_admission_requirement)
