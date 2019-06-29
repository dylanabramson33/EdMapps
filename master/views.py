import io
import csv
import time
import requests
from io import TextIOWrapper
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .loadcsv import loader

from .models import *
from .TableData import *
import datetime
from django.contrib.auth import logout
from natsort import natsorted, ns
from django.db.models import Count
import json



@login_required
def masterview(request):
    request.session['versionData'] = None
    request.session['gradeData'] = None
    request.session['unitData'] = None
    request.session['lessonData'] = None
    request.session['metadata'] = None
    return render(request, "master/masterview.html")


@login_required
def detail(request, key):
    return redirect("table")



def duplicate(request):
    """Duplicate all selected lesson values and related metadata. Change lesson version value
    to the value user inputs.

    """
    if request.method == 'GET':
        return render(request, "master/duplicate.html",
                      context=load_context_for_page(request, "Duplicate"))

    elif request.method == 'POST':
        lessons = select_lessons(request)
        newVersion = request.POST['newVersion']
        versionData = request.session['versionData']
        gradeData = request.session['gradeData']
        unitData = request.session['unitData']
        lessonData = request.session['lessonData']


        for lesson in lessons:
            progressionOrEmpty = Progression.objects.filter(unionkey=lesson)
            dokOrEmpty = DepthOfKnowledge.objects.filter(unionkey=lesson)
            activitySheetOrEmpty = ActivitySheet.objects.filter(unionkey=lesson)
            assessmentitemtypeOrEmpty = AssessmentItemType.objects.filter(unionkey=lesson)
            contentobjectiveOrEmpty = ContentObjective.objects.filter(unionkey=lesson)
            enrichmentactivitiesOrEmpty = EnrichmentActivities.objects.filter(unionkey=lesson)
            contextsOrEmpty = Contexts.objects.filter(unionkey=lesson)
            crosscurricularconnectionsOrEmpty = CrossCurricularConnections.objects.filter(unionkey=lesson)
            digitaltoolsOrEmpty = DigitalTools.objects.filter(unionkey=lesson)
            ethnicitygenderabilityOrEmpty = EthnicityGenderAbility.objects.filter(unionkey=lesson)
            fluencyactivitiesOrEmpty = FluencyActivities.objects.filter(unionkey=lesson)
            graphicorganizersOrEmpty = GraphicOrganizers.objects.filter(unionkey=lesson)
            interactivetutorialOrEmpty = InteractiveTutorial.objects.filter(unionkey=lesson)
            languageobjectivesOrEmpty = LanguageObjectives.objects.filter(unionkey=lesson)
            learninggamesOrEmpty = LearningGames.objects.filter(unionkey=lesson)
            learningprogressiontextOrEmpty = LearningProgressionText.objects.filter(unionkey=lesson)
            lessonnamesOrEmpty = LessonNames.objects.filter(unionkey=lesson)
            manipulativesOrEmpty = Manipulatives.objects.filter(unionkey=lesson)
            mathCenterActivitiesOrEmpty = MathCenterActivities.objects.filter(unionkey=lesson)
            modelsOrEmpty = Models.objects.filter(unionkey=lesson)
            prerequisitelessonsOrEmpty = PrerequisiteLessons.objects.filter(unionkey=lesson)
            prerequisiteinteractivetutorialOrEmpty = PrerequisiteInteractiveTutorial.objects.filter(unionkey=lesson)
            prerequisiteskillOrEmpty = PrerequisiteSkill.objects.filter(unionkey=lesson)
            rubricsOrEmpty = Rubrics.objects.filter(unionkey=lesson)
            standardsinlessonsOrEmpty = StandardsInLessons.objects.filter(unionkey=lesson)
            smpsinlessonsOrEmpty = SMPsInLessons.objects.filter(unionkey=lesson)
            toolsforinstructionOrEmpty = ToolsforInstruction.objects.filter(unionkey=lesson)
            vocabularyOrEmpty = Vocabulary.objects.filter(unionkey=lesson)
            visualmodelsOrEmpty = VisualModels.objects.filter(unionkey=lesson)

            splitKey = lesson.unionedkey.split('.')
            splitMaster = lesson.master.split('.')
            newKey = newVersion + '.' + splitKey[1] + '.' + splitKey[2] + '.' + splitKey[3]
            newMaster = newVersion + '.' + splitMaster[1] + '.' + splitMaster[2] + '.' + splitMaster[3]
            newLesson = Lesson.objects.create(unionedkey=newKey, master=newMaster)
            (newMasterObj, created) = Master.objects.get_or_create(id=newMaster)
            for progression in progressionOrEmpty:
                progression.pk = None
                progression.unionkey = newLesson
                progression.master = newMasterObj
                progression.save(edit=True)
            for dok in dokOrEmpty:
                dok.pk = None
                dok.unionkey = newLesson
                dok.master = newMasterObj
                dok.save(edit=True)
            for activitySheet in activitySheetOrEmpty:
                activitySheet.pk = None
                activitySheet.unionkey = newLesson
                activitySheet.master = newMasterObj
                activitySheet.save(edit=True)
            for assessmentitemtype in assessmentitemtypeOrEmpty:
                assessmentitemtype.pk = None
                assessmentitemtype.unionkey = newLesson
                assessmentitemtype.master = newMasterObj
                assessmentitemtype.save(edit=True)
            for contentobjective in contentobjectiveOrEmpty:
                contentobjective.pk = None
                contentobjective.unionkey = newLesson
                contentobjective.master = newMasterObj
                contentobjective.save(edit=True)
            for enrichmentactivities in enrichmentactivitiesOrEmpty:
                enrichmentactivities.pk = None
                enrichmentactivities.unionkey = newLesson
                enrichmentactivities.master = newMasterObj
                enrichmentactivities.save(edit=True)
            for contexts in contextsOrEmpty:
                contexts.pk = None
                contexts.unionkey = newLesson
                contexts.master = newMasterObj
                contexts.save(edit=True)
            for crosscurricularconnections in crosscurricularconnectionsOrEmpty:
                crosscurricularconnections.pk = None
                crosscurricularconnections.unionkey = newLesson
                crosscurricularconnections.master = newMasterObj
                crosscurricularconnections.save(edit=True)
            for digitaltools in digitaltoolsOrEmpty:
                digitaltools.pk = None
                digitaltools.unionkey = newLesson
                digitaltools.master = newMasterObj
                digitaltools.save(edit=True)
            for ethnicitygenderability in ethnicitygenderabilityOrEmpty:
                ethnicitygenderability.pk = None
                ethnicitygenderability.unionkey = newLesson
                ethnicitygenderability.master = newMasterObj
                ethnicitygenderability.save(edit=True)
            for fluencyactivities in fluencyactivitiesOrEmpty:
                fluencyactivities.pk = None
                fluencyactivities.unionkey = newLesson
                fluencyactivities.master = newMasterObj
                fluencyactivities.save(edit=True)
            for graphicorganizers in graphicorganizersOrEmpty:
                graphicorganizers.pk = None
                graphicorganizers.unionkey = newLesson
                graphicorganizers.master = newMasterObj
                graphicorganizers.save(edit=True)
            for interactivetutorial in interactivetutorialOrEmpty:
                interactivetutorial.pk = None
                interactivetutorial.unionkey = newLesson
                interactivetutorial.master = newMasterObj
                interactivetutorial.save(edit=True)
            for languageobjectives in languageobjectivesOrEmpty:
                languageobjectives.pk = None
                languageobjectives.unionkey = newLesson
                languageobjectives.master = newMasterObj
                languageobjectives.save(edit=True)
            for learninggames in learninggamesOrEmpty:
                learninggames.pk = None
                learninggames.unionkey = newLesson
                learninggames.master = newMasterObj
                learninggames.save(edit=True)
            for learningprogressiontext in learningprogressiontextOrEmpty:
                learningprogressiontext.pk = None
                learningprogressiontext.unionkey = newLesson
                learningprogressiontext.master = newMasterObj
                learningprogressiontext.save(edit=True)
            for lessonnames in lessonnamesOrEmpty:
                lessonnames.pk = None
                lessonnames.unionkey = newLesson
                lessonnames.master = newMasterObj
                lessonnames.save(edit=True)
            for manipulatives in manipulativesOrEmpty:
                manipulatives.pk = None
                manipulatives.unionkey = newLesson
                manipulatives.master = newMasterObj
                manipulatives.save(edit=True)
            for mathcenteractivities in mathCenterActivitiesOrEmpty:
                mathcenteractivities.pk = None
                mathcenteractivities.unionkey = newLesson
                mathcenteractivities.master = newMasterObj
                mathcenteractivities.save(edit=True)
            for models in modelsOrEmpty:
                models.pk = None
                models.unionkey = newLesson
                models.master = newMasterObj
                models.save(edit=True)
            for prerequisitelessons in prerequisitelessonsOrEmpty:
                prerequisitelessons.pk = None
                prerequisitelessons.unionkey = newLesson
                prerequisitelessons.master = newMasterObj
                prerequisitelessons.save(edit=True)
            for prerequisiteinteractivetutorial in prerequisiteinteractivetutorialOrEmpty:
                prerequisiteinteractivetutorial.pk = None
                prerequisiteinteractivetutorial.unionkey = newLesson
                prerequisiteinteractivetutorial.master = newMasterObj
                prerequisiteinteractivetutorial.save(edit=True)
            for prerequisiteskill in prerequisiteskillOrEmpty:
                prerequisiteskill.pk = None
                prerequisiteskill.unionkey = newLesson
                prerequisiteskill.master = newMasterObj
                prerequisiteskill.save(edit=True)
            for rubrics in rubricsOrEmpty:
                rubrics.pk = None
                rubrics.unionkey = newLesson
                rubrics.master = newMasterObj
                rubrics.save(edit=True)
            for standard in standardsinlessonsOrEmpty:
                standard.pk = None
                standard.unionkey = newLesson
                standard.master = newMasterObj
                standard.save(edit=True)
            for smpsinlessons in smpsinlessonsOrEmpty:
                smpsinlessons.pk = None
                smpsinlessons.unionkey = newLesson
                smpsinlessons.master = newMasterObj
                smpsinlessons.save(edit=True)
            for toolsforinstruction in toolsforinstructionOrEmpty:
                toolsforinstruction.pk = None
                toolsforinstruction.unionkey = newLesson
                toolsforinstruction.master = newMasterObj
                toolsforinstruction.save(edit=True)
            for vocabulary in vocabularyOrEmpty:
                vocabulary.pk = None
                vocabulary.unionkey = newLesson
                vocabulary.master = newMasterObj
                vocabulary.save(edit=True)
            for visualmodels in visualmodelsOrEmpty:
                visualmodels.pk = None
                visualmodels.unionkey = newLesson
                visualmodels.master = newMasterObj
                visualmodels.save(edit=True)

        DuplicationLog.objects.create(versionList = ', '.join(versionData),gradeList = ', '.join(gradeData), unitList = ', '.join(unitData),lessonList = ', '.join(lessonData))
        logs = DuplicationLog.objects.all()

        return render(request, "master/duplicationlogs.html", context={'lessons' : lessons, 'logs': logs})

def clone_related_items(item_set, newLesson, newMasterObj):
    for item in item_set:
        item.pk = None
        item.unionedkey = newLesson
        item.master = newMasterObj
        item.save()

def duplicationLogs(request):
    logs = DuplicationLog.objects.all()
    return render(request, "master/duplicationlogs.html", context={'logs' : logs})


def table(request):
    """Shows selection screen for get method and selected metadata for Post."""
    if request.method == 'GET':
        lessons = get_session_lessons(request)
        if(request.session["metadata"] is not None):
            metadata = request.session["metadata"]
            return render(request, "master/table.html",
                context={**load_context_for_page(request, 'Table'),
                        **{'lessons' : lessons, 'table' : True, 'metadata' : metadata}})
        else:
            return render(request, "master/table.html", context=load_context_for_page(request, 'Table'))



    elif request.method == 'POST':
        if request.POST.get('export'):
            return export(request)

        else:
            lessons = select_lessons(request)
            metadata = request.POST.getlist('Meta')

            if "StandardsInLessons" in metadata:
                lessons = lessons.prefetch_related("StandardsInLessons__standard")

            if "StandardsInUnits" in metadata:
                lessons = lessons.prefetch_related("StandardsInUnits__standard")


            if "SMPsInLessons" in metadata:
                lessons = lessons.prefetch_related("SMPsInLessons__SMP")

            lessons = lessons.prefetch_related(*metadata)
            filters = {}
            for modelString in metadata:
                filters[modelString + '__isnull'] = True



            setToItersect = lessons.filter(**filters)
            lessons = lessons.difference(setToItersect)



            return render(request, "master/table.html",
                      context={**load_context_for_page(request, 'Table'),
                               **{'lessons' : lessons, 'table' : True, 'metadata' : metadata}})

def export(request):
    lessons = get_session_lessons(request)
    metadata = request.session['metadata']
    modelFields = {}

    with io.open("output.csv", "w", encoding="utf-8", newline='') as myfile:

        wr = csv.writer(myfile)
        row = []
        row.append('Version')
        row.append('Grade')
        row.append('Unit')
        row.append('Lesson')
        for modelString in metadata:
            print(metadata)
            if modelString == "StandardsInLessons":
                row.append("Standard")
                row.append("Focus Developing Or Applied")
                row.append("Standard Wording")
            else:
                model = apps.get_model('master', modelString)
                fields = [(f.verbose_name, f.name) for f in model._meta.get_fields()[4:]]
                modelFields[modelString] = fields

                for field in fields:
                    row.append("\t" + field[0])

        wr.writerow(row)

        for lesson in lessons:
            row = []
            if lesson.version:

                row.append("\t" + lesson.version)
                if lesson.grade != None:
                    row.append("\t" + str(lesson.grade))
                else:
                    row.append("")

                if lesson.unit != None:
                    row.append("\t" + str(lesson.unit))
                else:
                    row.append("")
                if lesson.lesson != None:
                    row.append("\t" + str(lesson.lesson))
                else:
                    row.append("")

                for modelString in metadata:
                    if modelString == "StandardsInLessons":
                        standardInLesson = lesson.StandardsInLessons.all().first()
                        if standardInLesson:
                            row.append(standardInLesson.standardCode)
                            row.append(standardInLesson.focusDevelopingOrApplied)
                            if standardInLesson.standard:
                                row.append(standardInLesson.standard.standardWording)
                            else:
                                row.append("")
                        else:
                            row.append("")
                            row.append("")
                            row.append("")

                    else:
                        relatedset = lesson.get_related_set(modelString)
                        if relatedset:
                            for field in modelFields[modelString]:
                                row.append("\t" + getattr(relatedset[0], field[1]))
                        else:
                            for field in modelFields[modelString]:
                                row.append('')


                wr.writerow(row)



    with open('output.csv', 'r') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=output.csv'
        return response

def CreateLesson(request):
    return render(request, "master/createlesson.html")

def Visualize(request):
    versionData = request.session.get('versionData',None)
    gradeData = request.session.get('gradeData',None)
    unitData = request.session.get('unitData',None)
    lessonData = request.session.get('lessonData',None)
    metadata = request.session.get('metadata',None)

    if metadata is not None:
        lessons = Lesson.objects.all()

        if versionData:
            lessons = lessons.filter(version__in=versionData)
        if gradeData:
            lessons = lessons.filter(grade__in=gradeData)
        if unitData:
            lessons = lessons.filter(unit__in=unitData)
        if lessonData:
            lessons = lessons.filter(lesson__in=lessonData)

    metadata = request.session["metadata"]
    "A dictionary with aggregate count of values"
    fieldWithValueCounts = []
    valueCounts = []

    for modelString in metadata:
        model = apps.get_model('master', modelString)
        fields = [(f.verbose_name, f.name) for f in model._meta.get_fields()[4:]]
        tempLessons = lessons.filter(**{modelString + '__isnull': False})

        for field0,field1 in fields:
            valueCounts = []
            distinctValues = tempLessons.values_list(modelString + "__" + field0, flat=True).distinct().order_by()
            for value in distinctValues:
                count = tempLessons.filter(**{modelString + "__" + field0 : value}).count()
                valueCounts.append([str(value),count])

            fieldWithValueCounts.append((field0,valueCounts))



    return render(request, 'master/visualize.html', context = {"fields" : fieldWithValueCounts})






def modify(request):
    """Handles metadata file upload"""
    form = UploadFileForm()
    app_models = apps.get_app_config('master').get_models()
    modelList = []

    for model in app_models:
        if model != Lesson and  model != Master:
            modelList.append(str(model).split('.')[2].split("'")[0])

    half_modelList = len(modelList) / 2

    if request.method == 'GET':
        return render(request, 'master/modify.html',
                      context={'form': form, 'modelList' : modelList,
                               'half_modelList' : half_modelList})

    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if request.POST.get('upload_submit'):

            if form.is_valid():

                fileType = request.POST['MetaDownload']
                file = TextIOWrapper(request.FILES['file'].file, encoding='UTF-8', errors='replace')
                load = loader.Loader(fileType, file)
                load.loadSheet()

                return render(request, 'master/modify.html',
                              context={'form': form, 'modelList' : modelList,
                                       'half_modelList' : half_modelList})

        else:
            request.session['Meta'] = request.POST.get('Meta')
            metadata = request.POST.get('Meta')

            if "StandardsInLessons" in metadata:
                lessons = Lesson.objects.all().prefetch_related(
                    "StandardsInLessons__StandardCodesAndVerbiage"
                )

            else:
                lessons = Lesson.objects.all().prefetch_related(metadata)




            return render(request, "master/modify.html",
                          context={'form': form, 'lessons' : lessons,
                                   'modelList' : modelList, 'half_modelList' : half_modelList,
                                   'metadata' : metadata, 'table' : True})


def TableEdit(request):
    return render(request, "master/tableedit.html")

def Delete(request):
    """Handles deletion at the lesson level"""
    if request.method == 'GET':
        return render(request, "master/delete.html",
                      context=load_context_for_page(request, "Delete"))

    elif request.method == 'POST':
        lessons = select_lessons(request)

        lessons.delete()


        return render(request, "master/delete.html", context=load_context_for_page(request,"Delete"))

#load_context_for_page() = a dictionary with objects to display for selection
def load_context_for_page(request, page):
    if (page in ["Table", "Export"]):
        app_models = apps.get_app_config('master').get_models()
        modelList = []
        versionList = Lesson.objects.order_by('version').values_list('version', flat=True).distinct()
        gradeList = natural_sort(Lesson.objects.filter(grade__isnull=False).values_list('grade', flat=True).distinct())
        unitList = natural_sort(Lesson.objects.filter(unit__isnull=False).values_list('unit', flat=True).distinct())
        lessonList = natural_sort(Lesson.objects.filter(lesson__isnull=False).values_list('lesson', flat=True).distinct())

        print(unitList)

        for model in app_models:
            if model != Lesson and  model != Master and model != StandardCodesAndVerbiage:
                modelList.append(str(model).split('.')[2].split("'")[0])

        half_modelList = len(modelList) / 2

        try:
            previouslyCheckedVersion = request.session['versionData']
            previouslyCheckedGrade = request.session['gradeData']
            previouslyCheckedUnit = request.session['unitData']
            previouslyCheckedLesson = request.session['lessonData']
            previouslyCheckedMetadata = request.session['metadata']
        except:
            previouslyCheckedVersion = []
            previouslyCheckedGrade = []
            previouslyCheckedUnit = []
            previouslyCheckedLesson = []
            previouslyCheckedMetadata = []


        return {'modelList' : modelList, 'half_modelList' : half_modelList,
                'versionList': versionList,'gradeList': gradeList,
                'unitList':unitList, 'lessonList':lessonList,
                'previouslyCheckedVersion' : previouslyCheckedVersion,
                'previouslyCheckedGrade' : previouslyCheckedGrade,
                'previouslyCheckedUnit' : previouslyCheckedUnit,
                'previouslyCheckedLesson' : previouslyCheckedLesson, 'previouslyCheckedMetadata' : previouslyCheckedMetadata}

    elif (page in ["Delete", "Duplicate"]):
        versionList = Lesson.objects.values_list('version', flat=True).distinct()
        gradeList = natural_sort(Lesson.objects.filter(version__isnull=False).values_list('grade', flat=True).distinct())
        unitList = natural_sort(Lesson.objects.filter(unit__isnull=False).values_list('unit', flat=True).distinct())
        lessonList = natural_sort(Lesson.objects.filter(lesson__isnull= False).values_list('lesson', flat=True).distinct())

        return {'versionList': versionList, 'gradeList': gradeList, 'unitList':unitList, 'lessonList':lessonList}

def select_lessons(request):
    versionData = request.POST.getlist('Version')
    gradeData = request.POST.getlist('Grade')
    unitData = request.POST.getlist('Unit')
    lessonData = request.POST.getlist('Lesson')
    metadata = request.POST.getlist('Meta')

    request.session['versionData'] = versionData
    request.session['gradeData'] = gradeData
    request.session['unitData'] = unitData
    request.session['lessonData'] = lessonData
    request.session['metadata'] = metadata
    lessons = Lesson.objects.all()

    if versionData:
        lessons = lessons.filter(version__in=versionData)
    if gradeData:
        lessons = lessons.filter(grade__in=gradeData)
    if unitData:
        lessons = lessons.filter(unit__in=unitData)
    if lessonData:
        lessons = lessons.filter(lesson__in=lessonData)

    return lessons


def natural_sort(qs):
    return natsorted(list(qs), key=lambda y: y.lower())

def get_session_lessons(request):
    versionData = request.session.get('versionData',None)
    gradeData = request.session.get('gradeData',None)
    unitData = request.session.get('unitData',None)
    lessonData = request.session.get('lessonData',None)
    metadata = request.session.get('metadata',None)

    if metadata is not None:
        lessons = Lesson.objects.all()

        if versionData:
            lessons = lessons.filter(version__in=versionData)
        if gradeData:
            lessons = lessons.filter(grade__in=gradeData)
        if unitData:
            lessons = lessons.filter(unit__in=unitData)
        if lessonData:
            lessons = lessons.filter(lesson__in=lessonData)


        if "StandardsInLessons" in metadata:
            lessons = lessons.prefetch_related("StandardsInLessons__standard")

        if "StandardsInUnits" in metadata:
            lessons = lessons.prefetch_related("StandardsInUnits__standard")


        if "SMPsInLessons" in metadata:
            lessons = lessons.prefetch_related("SMPsInLessons__SMP")

        lessons = lessons.prefetch_related(*metadata)
        filters = {}
        for modelString in metadata:
            filters[modelString + '__isnull'] = True

        setToItersect = lessons.filter(**filters)
        lessons = lessons.difference(setToItersect)
        return lessons

def logout_view(request):
    logout(request)
    redirect('masterview')

def faq(request):
    return render(request, "master/faq.html")

def support(request):
    return render(request, "master/support.html")


def improve(request):
    return render(request, "master/improve.html")

def lessonProfiles(request):
    return render(request, "master/lessonprofiles.html")

def reports(request):
    return render(request, "master/reports.html")
