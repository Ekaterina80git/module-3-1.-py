calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return tuple([len(string), string.upper(), string.lower()])
def is_contains(str_,list_to_search):
    count_calls()
    for i in list_to_search:
         if str_.lower() == i .lower():
          return True
    return False

print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban",["ban","BaNaN","urBAN"]))# Urban ~ urBAN
print(is_contains("sysle",["resysling",'syslik'])) # No matches
print(calls)







