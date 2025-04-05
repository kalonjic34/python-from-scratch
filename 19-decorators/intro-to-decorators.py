def be_nice(fn):
    def inner():
        print("Nice to meet you! Im honored to execute your function for you!")
        fn()
        print("It was my pleasure execting your function! Have a nice day!")
        
    return inner

@be_nice
def complex_business_logic():
    print("Something complex!")
    
@be_nice
def another_fancy_function():
    print("Random text")
    
# complex_business_logic() 
another_fancy_function()       