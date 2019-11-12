from django.shortcuts import render


from .models import network_communication_career, multimedia_career, Fields_of_study_or_course_name, minimum_admission_requirement,applications_development_career, GuidanceView
# Create your views here.

def guidance(request):
    context = {
        'university': GuidanceView.objects.all(),
        'network_communication_career': network_communication_career.objects.all(),
        'multimedia_career': multimedia_career.objects.all(),
        'Fields_of_study_or_course_name': Fields_of_study_or_course_name.oabjects.all(),
        'minimum_admission_requirement': minimum_admission_requirement.objects.all(),
        'applications_development_career': applications_development_career.objects.all(),
    }
    return render(request, 'guidance/guidance.html', context)