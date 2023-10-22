from generateUniqueQuestions import generateUniqueQuestions

listOfQuestions = [
    "Have you been able to talk with your family recently?", 
    "Have you been sleeping well recently?", 
    "Have you felt satisfied at work recently?",
    "Have you been able to work towards personal goals outside of work?",
]

def generateQuestions (dailyQuestion, weekly):

    responseList = [dailyQuestion]

    if weekly:
        for question in listOfQuestions:
            responseList.append(question)

    return responseList