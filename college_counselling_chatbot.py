import re
import response_sheet as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)



    # Responses 
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Our college name is \"NPTY College of Engineering and Technology\"',['name'],single_response=True,required_words=['name'])
    response('Chairman of this college is Mr.Thiru and Vice Chairman of this college is Mr.Yogesh',['chairman','vice chairman'],single_response=True,required_words=['chairman','vice chairman'])
    


    response(long.Admission,['admissions','admission'],single_response=True,required_words=['admission','admissions','open'])
    response(long.Department,['departments','department'],single_response=True,required_words=['departments','department'])
    response(long.Total_Seats,['total','seats' ],single_response=True,required_words=['total','seats'])
    response(long.Fees,['fee','fees'],single_response=True,required_words=['fees','fee'])
    response(long.Passspercentage,['pass', 'percentage'],single_response=True,required_words=['pass','percentage'])
    response(long.HPackage,['highest' ,'package' ],single_response=True,required_words=['highest','package'])
    response(long.LPackage,['lowest' ,'package'],single_response=True,required_words=['lowest','package'])
    response(long.Location,['located','location'],single_response=True,required_words=['located','location'])
    response(long.Faculty,['faculty','staffs' ,'members'],single_response=True,required_words=['faculty','staffs'])
    response(long.Lab,['lab' ,'facilities' ],single_response=True,required_words=['lab'])
    response(long.Transport,['transport','bus'],single_response=True,required_words=['transport','bus'])
    response(long.Food,['food'],single_response=True,required_words=['food'])
    response(long.FoodType,['both','veg','and','nonveg','are' ,'served'],single_response=True,required_words=['veg','non veg'])
    response(long.Eligiblity,['joining','join','requirement'],single_response=True,required_words=['requirement','join','joining'])
    response(long.Placement,[ 'placement','placements'],single_response=True,required_words=['placement','placements'])
    response(long.Dresscode,['dress','code'],single_response=True,required_words=['dress','code'])
    response(long.Specialtraining,['special','training','coaching'],single_response=True,required_words=['special','training','coaching'])
    response(long.Website,['website'],single_response=True,required_words=['website'])
    response(long.Company,['companies' , 'recruitment'],single_response=True,required_words=['reqcruitment','company'])
    response(long.Code,['councelling','code'],single_response=True,required_words=['counselling','code'])
    response(long.Work,['work','job'],single_response=True,required_words=['work','job'])
    response(long.Rank,['rank','position','ranking'],single_response=True,required_words=['rank','ranking','position'])


    best_match = max(highest_prob_list, key=highest_prob_list.get)
   
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
print("Please enter your Queries....\n" )
while True:
    print('\n','Bot: ' + get_response(input('You: ')))