import sys
import os
import csv
from master.models import *




class Loader:

    def __init__(self,sheetToLoad, file):
        self.sheetToLoad = sheetToLoad
        self.file = file

    def getDict(self,row,updateVals):
        dictToReturn = {}
        x = 4
        for val in updateVals:
            row[x]

            dictToReturn[val] = row[x]

            x += 1
        return dictToReturn




    def loadSheet(self):
        print(self.sheetToLoad)
        reader = csv.reader(self.file)
        if self.sheetToLoad != 'StandardsCodesandVerbiage' and self.sheetToLoad != 'StandardsinLessons' and self.sheetToLoad != 'SMPText' and self.sheetToLoad != 'SMPsinLessons' and self.sheetToLoad != 'StandardsinUnits':
            if self.sheetToLoad == "ActivitySheets":
                modelToUpdate = ActivitySheet.objects
                updateVals = ['activitySheetName']

            elif self.sheetToLoad == "AcademicVocabulary":
                modelToUpdate = AcademicVocabulary.objects
                updateVals = ['word', 'definition', 'wordFoundInGradeLevel', 'notes']

            elif self.sheetToLoad == "Progressions":
                modelToUpdate = Progression.objects
                updateVals = ['PrerequisiteLesson3',
                    'PrerequisiteLesson2','PrerequisiteLesson1',
                    'FutureLesson1','FutureLesson2']

            elif self.sheetToLoad == "DOK" or self.sheetToLoad == "DepthOfKnowledge":
                modelToUpdate = DepthOfKnowledge.objects
                updateVals = ['tgPage','dokitem','dok']

            elif self.sheetToLoad == 'AssessmentItemType':
                modelToUpdate = AssessmentItemType.objects
                updateVals = ['component','page','item','itemType']

            elif self.sheetToLoad == 'ContentObjectives':
                modelToUpdate = ContentObjective.objects
                updateVals = ['contentObjective']

            elif self.sheetToLoad == 'EnrichmentActivityList':
                modelToUpdate = EnrichmentActivities.objects
                updateVals = ['fileName','title']

            elif self.sheetToLoad == 'Contexts' or self.sheetToLoad == 'Contexts-FLonly' or self.sheetToLoad == 'Contexts—FLonly':
                modelToUpdate = Contexts.objects
                updateVals = ['page', 'item', 'context', 'issues']

            elif self.sheetToLoad == 'Cross-CurricularConnections':
                modelToUpdate = CrossCurricularConnections.objects
                updateVals = ['component', 'contentArea']

            elif self.sheetToLoad == 'DigitalTools':
                modelToUpdate = DigitalTools.objects
                updateVals = ['baseTenBlocksTool', 'perimeterAndAreaTool', 'fractionModelsTool', 'numberLineTool', 'multiplicationModelsTool', 'countersConnectingCubesTool']

            elif self.sheetToLoad == 'EthnicityGenderAbility' or self.sheetToLoad == 'Ethnicity,Gender,Ability':
                modelToUpdate = EthnicityGenderAbility.objects
                updateVals = ['page', 'item', 'type', 'ethnicity', 'gender', 'ability', 'correctOrIncorrect']

            elif self.sheetToLoad == 'FluencyActivities':
                modelToUpdate = FluencyActivities.objects
                updateVals = ['fluencyPracticeTitle']

            elif self.sheetToLoad == 'GraphicOrganizers':
                modelToUpdate = GraphicOrganizers.objects
                updateVals = ['page', 'graphicOrganizer']

            elif self.sheetToLoad == 'InteractiveTutorial':
                modelToUpdate = InteractiveTutorial.objects
                updateVals = ['interactiveTutorial', 'videoID', 'objective', 'estimatedTime']

            elif self.sheetToLoad == 'LanguageObjectives':
                modelToUpdate = LanguageObjectives.objects
                updateVals = ['languageObjective']

            elif self.sheetToLoad == 'LearningGames':
                modelToUpdate = LearningGames.objects
                updateVals = ['learningGame']

            elif self.sheetToLoad == 'LearningProgressionText':
                modelToUpdate = LearningProgressionText.objects
                updateVals = ['previousLearning', 'inThisLesson', 'subsequentLearning']

            elif self.sheetToLoad == 'LessonNames':
                modelToUpdate = LessonNames.objects
                updateVals = ['lessonName']

            elif self.sheetToLoad == 'Manipulatives':
                modelToUpdate = Manipulatives.objects
                updateVals = ['manipulativeUsed', 'quantity', 'use', 'required', 'lesson', 'activities']

            elif self.sheetToLoad == 'MathCenterActivities':
                modelToUpdate = MathCenterActivities.objects
                updateVals = ['title', 'fileName']

            elif self.sheetToLoad == 'Models':
                modelToUpdate = Models.objects
                updateVals = ['model']

            elif self.sheetToLoad == 'PrerequisiteInteractiveTutorial':
                modelToUpdate = PrerequisiteInteractiveTutorial.objects
                updateVals = ['prerequisiteInteractiveTutorial', 'prerequisiteVideoID', 'prerequisiteObjective', 'prerequisiteEstimatedTime']

            elif self.sheetToLoad == 'PrerequisiteLessons':
                modelToUpdate = PrerequisiteLessons.objects
                updateVals = ['prerequisiteLessonGrade', 'prerequisiteLessonNumber']

            elif self.sheetToLoad == 'PrerequisiteSkills':
                modelToUpdate = PrerequisiteSkill.objects
                updateVals = ['prerequisiteSkill']

            elif self.sheetToLoad == 'Rubrics':
                modelToUpdate = Rubrics.objects
                updateVals = ['page', 'component', 'typeOfRubric']

            elif self.sheetToLoad == 'SMPsInLessons':
                modelToUpdate = SMPsInLessons.objects
                updateVals = ['SMP']

            elif self.sheetToLoad == 'ToolsforInstruction' or self.sheetToLoad == 'ToolsforInstructionList':
                modelToUpdate = ToolsforInstruction.objects
                updateVals = ['toolForInstruction']

            elif self.sheetToLoad == 'VisualModels':
                modelToUpdate = VisualModels.objects
                updateVals = ['pagewithVisualModel']

            elif self.sheetToLoad == 'Vocabulary':
                modelToUpdate = Vocabulary.objects
                updateVals = ['academic', 'vocabularyTerm', 'definition', 'newOrReview', 'vocabularyBoxPage']



            ignoreNextRow = False
            readerList = list(reader)
            for i, row in enumerate(readerList):
                if(not ignoreNextRow):
                    try:
                        if(len(row) >= 4 + len(updateVals)):

                            (obj, created) = Master.objects.get_or_create(
                                id = row[0].strip() + "." + row[1].strip() + "." + row[2].strip() + "." + row[3].strip())
                            modelToUpdate.create(master = obj,**self.getDict(row,updateVals))
                        elif(i < len(readerList) - 1):
                            (obj, created) = Master.objects.get_or_create(
                                id = row[0].strip() + "." + row[1].strip() + "." + row[2].strip() + "." + row[3].strip())
                            modelToUpdate.create(master = obj,**self.getDict(row + readerList[i+1],updateVals))
                            ignoreNextRow = True
                    except Exception as e:
                        print(self.sheetToLoad + " \n" + str(e))
                else:
                    ignoreNextRow = False

        elif self.sheetToLoad == 'StandardsinLessons':
            for row in reader:
                (obj, created) = Master.objects.get_or_create(
                        id = row[0].strip() + "." + row[1].strip() + "." + row[2].strip() + "." + row[3].strip())
                standardToAdd = StandardCodesAndVerbiage.objects.filter(standard = row[4]).filter(standardVersion = row[0]).first()
                StandardsInLessons.objects.create(master = obj, standard = standardToAdd, standardCode = row[4])

        elif self.sheetToLoad == 'StandardsinUnits':
            for row in reader:
                (obj, created) = Master.objects.get_or_create(
                        id = row[0].strip() + "." + row[1].strip() + "." + row[2].strip() + "." + row[3].strip())
                standardToAdd = StandardCodesAndVerbiage.objects.filter(standard = row[6]).filter(standardVersion = row[0]).first()
                StandardsInUnits.objects.create(master = obj, standard = standardToAdd, component = row[4], item = row[5])


        elif self.sheetToLoad == 'StandardsCodesandVerbiage':
            for row in reader:
                (obj, created) = StandardCodesAndVerbiage.objects.get_or_create(standard = row[1], standardVersion = row[0],
                    standardWording = row[2], majorSuportingOrAdditional = row[3])

        elif self.sheetToLoad == 'SMPText':
            for row in reader:
                (obj, created) = SMPText.objects.get_or_create(version = row[0], smp = row[1],
                    SMPText = row[2])

        elif self.sheetToLoad == 'SMPsinLessons':
            for row in reader:
                (obj, created) = Master.objects.get_or_create(
                        id = row[0].strip() + "." + row[1].strip() + "." + row[2].strip() + "." + row[3].strip())
                smpToAdd = SMPText.objects.filter(smp = row[4]).filter(version = row[0]).first()
                SMPsInLessons.objects.create(master = obj, SMP = smpToAdd)
