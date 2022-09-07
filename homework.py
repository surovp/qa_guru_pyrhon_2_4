def name_func_and_args(name_func, *args):
    # преобразовываем название функции
    name_func = name_func.__name__
    name_func = name_func.replace("_", " ").capitalize()
    print(name_func)
    # преобразовываем аргументы
    symbols = ["://", ".", "/", "-", "_"]
    for i in args:
        for symbol in symbols:
            if symbol in i:
                i = i.replace(symbol, " ").capitalize().strip()
        print(i)

def open_browser(browser_name):
    name_func_and_args(open_browser, browser_name)
    print()

def go_to_companyname_homepage(page_url):
    name_func_and_args(go_to_companyname_homepage, page_url)
    print()

def find_registration_button_on_login_page(page_url, button_text):
    name_func_and_args(find_registration_button_on_login_page, page_url, button_text)
    print()

open_browser("Microcoft_Edge")
go_to_companyname_homepage("https://demoqa.com/automation-practice-form")
find_registration_button_on_login_page("https://github.com/surovp/qa_guru_pyrhon_2_4", "Pull request")
