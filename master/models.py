from django.db import models


#https://github.cainc.com/iready/ReadyMetaData


def cal_key(master, modelToUpdate):
        present_keys = modelToUpdate.objects.filter(master=master).order_by('-key').values_list('key',flat=True)
        if present_keys:
            return present_keys[0] + 1

        else:
            return 1

class Master(models.Model):
    id = models.CharField(max_length = 200, primary_key = True, default = 'default')



    def __str__(self):
        return self.id



class Lesson(models.Model):
    master = models.CharField(max_length = 200, primary_key = False)
    unionedkey = models.CharField(max_length = 200, primary_key = True)

    version = models.CharField(max_length = 200, null = True)
    grade = models.CharField(null = True, max_length = 255)
    unit = models.CharField(null = True, max_length = 255)
    lesson = models.CharField(null = True, max_length = 255)


    def save(self, *args, **kwargs):
        currentString = str(self.master)
        splitString = currentString.split('.')
        self.version = splitString[0]
        self.grade = splitString[1] if splitString[1] else None
        self.unit = splitString[2] if splitString[2] else None
        self.lesson = splitString[3] if splitString[3] else None
        super(Lesson, self).save(*args, **kwargs)





    def get_related_set(self,modelName):
            if modelName == 'Progression':
                return self.Progression.all()

            elif modelName == 'DepthOfKnowledge':
                return self.DepthOfKnowledge.all()

            elif modelName == 'ActivitySheet':
                return self.ActivitySheet.all()

            elif modelName == 'AssessmentItemType':
                return self.AssessmentItemType.all()

            elif modelName == 'ContentObjective':
                return self.ContentObjective.all()

            elif modelName == 'Enrichmentctivities':
                return self.EnrichmentActivities.all()

            elif modelName == 'Contexts':
                return self.Contexts.all()

            elif modelName == 'CrossCurricularConnections':
                return self.CrossCurricularConnections.all()

            elif modelName == 'DigitalTools':
                return self.DigitalTools.all()

            elif modelName == 'EthnicityGenderAbility':
                return self.EthnicityGenderAbility.all()

            elif modelName == 'FluencyActivities':
                return self.FluencyActivities.all()

            elif modelName == 'GraphicOrganizers':
                return self.GraphicOrganizers.all()

            elif modelName == 'InteractiveTutorial':
                return self.InteractiveTutorial.all()

            elif modelName == 'LanguageObjectives':
                return self.LanguageObjectives.all()

            elif modelName == 'LearningGames':
                return self.LearningGames.all()

            elif modelName == 'LearningProgressionText':
                return self.LearningProgressionText.all()

            elif modelName == 'LessonNames':
                return self.LessonNames.all()

            elif modelName == 'Manipulatives':
                return self.Manipulatives.all()

            elif modelName == 'Models':
                return self.Models.all()

            elif modelName == 'PrerequisiteLessons':
                return self.PrerequisiteLessons.all()

            elif modelName == 'PrerequisiteInteractiveTutorial':
                return self.PrerequisiteInteractiveTutorial.all()

            elif modelName == 'PrerequisiteSkill':
                return self.PrerequisiteSkill.all()

            elif modelName == 'Rubrics':
                return self.Rubrics.all()

            elif modelName == 'SMPsInLessons':
                return self.SMPsInLessons.all()

            elif modelName == 'ToolsforInstruction':
                return self.ToolsforInstruction.all()

            elif modelName == 'Vocabulary':
                return self.Vocabulary.all()

            elif modelName == 'VisualModels':
                return self.VisualModels.all()




class Progression(models.Model):
    key = models.PositiveIntegerField()
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "Progression")
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "Progression")
    PrerequisiteLesson3 = models.CharField(max_length = 255, blank = True)
    PrerequisiteLesson2 = models.CharField(max_length = 255, blank = True)
    PrerequisiteLesson1 = models.CharField(max_length = 255, blank = True)
    FutureLesson1 = models.CharField(max_length = 255, blank = True)
    FutureLesson2 = models.CharField(max_length = 255, blank = True)
    FutureLesson3 = models.CharField(max_length = 255, blank = True)

    def Meta(self):
        unique_together = ("key", "master")

    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,Progression)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj

        super(Progression, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.Progression" % self.master


class DepthOfKnowledge(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "DepthOfKnowledge")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "DepthOfKnowledge")
    tgPage = models.CharField(max_length = 255, blank = True)
    dokitem = models.CharField(max_length = 255, blank = True)
    dok = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,DepthOfKnowledge)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(DepthOfKnowledge, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.DepthOfKnowledge" % self.master.id

class AcademicVocabulary(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "AcademicVocabulary")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "AcademicVocabulary")
    word = models.CharField(max_length = 255, blank = True)
    definition = models.CharField(max_length = 255, blank = True)
    wordFoundInGradeLevel = models.CharField(max_length = 255, blank = True)
    notes = models.CharField(max_length = 255, blank = True)

    def save(self, edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,AcademicVocabulary)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(AcademicVocabulary, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.AcademicVocabulary" % self.master.id

class ActivitySheet(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "ActivitySheet")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "ActivitySheet")
    activitySheetName = models.CharField(max_length = 255, blank = True)

    def save(self, edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,ActivitySheet)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(ActivitySheet, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.ActivitySheet" % self.master.id

class AssessmentItemType(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "AssessmentItemType")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "AssessmentItemType")
    component = models.CharField(max_length = 255, blank = True)
    page = models.CharField(max_length = 255, blank = True)
    item = models.CharField(max_length = 255, blank = True)
    itemType = models.CharField(max_length = 255, blank = True)

    def save(self, edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,AssessmentItemType)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(AssessmentItemType, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.AssessmentItemType" % self.master.id

class ContentObjective(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "ContentObjective")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "ContentObjective")
    contentObjective = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,ContentObjective)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(ContentObjective, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.ContentObjective" % self.master.id

class EnrichmentActivities(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "EnrichmentActivities")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "EnrichmentActivities")
    fileName = models.CharField(max_length = 255, blank = True)
    title = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,EnrichmentActivities)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(EnrichmentActivities, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.EnrichmentActivities" % self.master.id

class Contexts(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "Contexts")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "Contexts")
    page = models.CharField(max_length = 255, blank = True)
    item = models.CharField(max_length = 255, blank = True)
    context = models.CharField(max_length = 255, blank = True)
    issues = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,Contexts)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(Contexts, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.Contexts" % self.master.id

class CrossCurricularConnections(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "CrossCurricularConnections")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "CrossCurricularConnections")
    component = models.CharField(max_length = 255, blank = True)
    contentArea = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,CrossCurricularConnections)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(CrossCurricularConnections, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.CrossCurricularConnections" % self.master.id

class DigitalTools(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "DigitalTools")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "DigitalTools")
    baseTenBlocksTool = models.CharField(max_length = 255, blank = True)
    perimeterAndAreaTool = models.CharField(max_length = 255, blank = True)
    fractionModelsTool = models.CharField(max_length = 255, blank = True)
    numberLineTool = models.CharField(max_length = 255, blank = True)
    multiplicationModelsTool = models.CharField(max_length = 255, blank = True)
    countersConnectingCubesTool = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,DigitalTools)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(DigitalTools, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.DigitalTools" % self.master.id

class EthnicityGenderAbility(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "EthnicityGenderAbility")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "EthnicityGenderAbility")
    page = models.CharField(max_length = 255, blank = True)
    item = models.CharField(max_length = 255, blank = True)
    type = models.CharField(max_length = 255, blank = True)
    ethnicity = models.CharField(max_length = 255, blank = True)
    gender = models.CharField(max_length = 255, blank = True)
    ability = models.CharField(max_length = 255, blank = True)
    correctOrIncorrect = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,EthnicityGenderAbility)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(EthnicityGenderAbility, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.EthnicityGenderAbility" % self.master.id

class FluencyActivities(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "FluencyActivities")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "FluencyActivities")
    fluencyPracticeTitle = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,FluencyActivities)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(FluencyActivities, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.FluencyActivities" % self.master.id

class GraphicOrganizers(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "GraphicOrganizers")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "GraphicOrganizers")
    page = models.CharField(max_length = 255, blank = True)
    graphicOrganizer = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,GraphicOrganizers)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(GraphicOrganizers, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.GraphicOrganizers" % self.master.id

class InteractiveTutorial(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "InteractiveTutorial")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "InteractiveTutorial")
    interactiveTutorial = models.CharField(max_length = 255, blank = True)
    videoID = models.CharField(max_length = 255, blank = True)
    objective = models.TextField(blank = True)
    estimatedTime = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,InteractiveTutorial)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(InteractiveTutorial, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.InteractiveTutorial" % self.master.id

class LanguageObjectives(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "LanguageObjectives")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "LanguageObjectives")
    languageObjective = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,LanguageObjectives)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(LanguageObjectives, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.LanguageObjectives" % self.master.id

class LearningGames(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "LearningGames")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "LearningGames")
    learningGame = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,LearningGames)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(LearningGames, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.LearningGames" % self.master.id

class LearningProgressionText(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "LearningProgressionText")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "LearningProgressionText")
    previousLearning = models.TextField(blank = True)
    inThisLesson = models.TextField(blank = True)
    subsequentLearning = models.TextField(blank = True)

    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,LearningProgressionText)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(LearningProgressionText, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.LearningProgressionText" % self.master.id

class LessonNames(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "LessonNames")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "LessonNames")
    lessonName = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,LessonNames)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(LessonNames, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.LessonNames" % self.master.id

class Manipulatives(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "Manipulatives")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "Manipulatives")
    manipulativeUsed = models.CharField(max_length = 255, blank = True)
    quantity = models.CharField(max_length = 255, blank = True)
    use = models.CharField(max_length = 255, blank = True)
    required = models.CharField(max_length = 255, blank = True)
    lesson = models.CharField(max_length = 255, blank = True)
    activities = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,Manipulatives)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(Manipulatives, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.Manipulatives" % self.master.id

class MathCenterActivities(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "MathCenterActivities")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "MathCenterActivities")
    title = models.CharField(max_length = 255, blank = True)
    fileName = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,MathCenterActivities)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(MathCenterActivities, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.MathCenterActivities" % self.master.id

class Models(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "Models")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "Models")
    model = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,Models)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(Models, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.Models" % self.master.id

class PrerequisiteLessons(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "PrerequisiteLessons")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "PrerequisiteLessons")
    prerequisiteLessonGrade = models.CharField(max_length = 255, blank = True)
    prerequisiteLessonNumber = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,PrerequisiteLessons)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(PrerequisiteLessons, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.PrerequisiteInteractiveTutorial" % self.master.id

class PrerequisiteInteractiveTutorial(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "PrerequisiteInteractiveTutorial")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "PrerequisiteInteractiveTutorial")
    prerequisiteInteractiveTutorial = models.CharField(max_length = 255, blank = True)
    prerequisiteVideoID = models.CharField(max_length = 255, blank = True)
    prerequisiteObjective = models.TextField(blank = True)
    prerequisiteEstimatedTime = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,PrerequisiteInteractiveTutorial)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(PrerequisiteInteractiveTutorial, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.PrerequisiteInteractiveTutorial" % self.master.id

class PrerequisiteSkill(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "PrerequisiteSkill")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "PrerequisiteSkill")
    prerequisiteSkill = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,PrerequisiteSkill)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(PrerequisiteSkill, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.PrerequisiteSkill" % self.master.id

class Rubrics(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "Rubrics")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "Rubrics")
    page = models.CharField(max_length = 255, blank = True)
    component = models.CharField(max_length = 255, blank = True)
    typeOfRubric = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,Rubrics)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(Rubrics, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.Rubrics" % self.master.id


class ToolsforInstruction(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "ToolsforInstruction")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "ToolsforInstruction")
    toolForInstruction = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,ToolsforInstruction)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(ToolsforInstruction, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.ToolsforInstruction" % self.master.id

class Vocabulary(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "Vocabulary")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "Vocabulary")
    academic = models.CharField(max_length = 255, blank = True)
    vocabularyTerm = models.CharField(max_length = 255, blank = True)
    definition = models.CharField(max_length = 255, blank = True)
    newOrReview = models.CharField(max_length = 255, blank = True)
    vocabularyBoxPage = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,ToolsforInstruction)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(Vocabulary, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.Vocabulary" % self.master.id

class VisualModels(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "VisualModels")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "VisualModels")
    pagewithVisualModel = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,VisualModels)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(VisualModels, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.VisualModels" % self.master.id

class StandardCodesAndVerbiage(models.Model):
    code = models.CharField(primary_key = True, max_length = 255, blank = True)
    standard = models.CharField( max_length = 255, blank = True)
    standardVersion = models.CharField(max_length = 255, blank = True)
    standardWording = models.TextField(blank = True)
    majorSuportingOrAdditional = models.CharField(max_length = 255, blank = True)

    def save(self,edit=False, *args, **kwargs):
        self.code = self.standard + "_" + self.standardVersion
        super(StandardCodesAndVerbiage, self).save(*args, **kwargs)


    def __str__(self):
        return "%s.StandardCodesAndVerbiage" % self.standard


class StandardsInLessons(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete=models.CASCADE, related_name = "StandardsInLessons")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "StandardsInLessons")
    standardCode = models.CharField(max_length = 255, blank = True)
    standard = models.ForeignKey(StandardCodesAndVerbiage,on_delete=models.DO_NOTHING, related_name = "StandardInLessons", null = True)
    focusDevelopingOrApplied = models.CharField(max_length = 255, blank = True)

    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,StandardsInLessons)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj

        if(edit):
            self.standard = StandardCodesAndVerbiage.objects.filter(standard = self.standardCode).first()

        super(StandardsInLessons, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.StandardsInLessons" % self.master.id



class SMPText(models.Model):
    code = models.CharField(primary_key = True, max_length = 255, blank = True)
    version = models.CharField(max_length = 255, blank = True)
    smp = models.CharField( max_length = 255, blank = True)
    SMPText = models.CharField(max_length = 255, blank = True)


    def save(self,edit=False, *args, **kwargs):
        self.code = self.smp + "_" + self.version
        super(SMPText, self).save(*args, **kwargs)


    def __str__(self):
        return "%s.SMP" % self.smp





class SMPsInLessons(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete = models.CASCADE, related_name = "SMPsInLessons")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "SMPsInLessons")
    SMP = models.ForeignKey(SMPText,on_delete = models.CASCADE, related_name = "SMPsInLessons", null = True)


    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,SMPsInLessons)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj
        super(SMPsInLessons, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.SMPsInLessons" % self.master.id


class StandardsInUnits(models.Model):
    key = models.PositiveIntegerField()
    master = models.ForeignKey(Master,on_delete=models.CASCADE, related_name = "StandardsInUnits")
    unionkey = models.ForeignKey(Lesson,on_delete=models.CASCADE, related_name = "StandardsInUnits")
    component = models.CharField(max_length = 255, blank = True)
    standard = models.ForeignKey(StandardCodesAndVerbiage,on_delete=models.DO_NOTHING, related_name = "StandardsInUnits", null = True)
    item = models.CharField(max_length = 255, blank = True)

    def save(self,edit=False, *args, **kwargs):
        if (not edit):
            key = cal_key(self.master,StandardsInUnits)
            masterid = str(self.master.id)
            (obj,created) = Lesson.objects.get_or_create(unionedkey=masterid + "#" + str(key),master=masterid)
            self.key = key
            self.unionkey = obj


        super(StandardsInUnits, self).save(*args, **kwargs)

    def __str__(self):
        return "%s.StandardsInUnits" % self.master.id

class DuplicationLog(models.Model):
    versionList =  models.TextField(blank = True)
    gradeList =  models.TextField(blank = True)
    unitList =  models.TextField(blank = True)
    lessonList =  models.TextField(blank = True)
    timeCreated = models.DateTimeField(auto_now_add = True, blank = True)
