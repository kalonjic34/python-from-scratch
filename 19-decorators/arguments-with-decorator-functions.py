def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you! Im honored to execute your function for you!")
        # print(args)
        # print(kwargs)
        fn(*args, **kwargs)
        print("It was my pleasure execting your function! Have a nice day!")
        
    return inner

@be_nice
def complex_business_logic(stakeholder, position):
    print(f"Something complex for {position} {stakeholder}!")
    
complex_business_logic("Christian", "CEO")