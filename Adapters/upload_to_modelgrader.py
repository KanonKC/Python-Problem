from .ports import problem_to_elabsheet, elabsheet_to_modelgrader, modelgrader_uploader
filename = input()

text = problem_to_elabsheet.convert(filename)
modelgraderDict = elabsheet_to_modelgrader.convert(text)
modelgrader_uploader.upload(modelgraderDict)