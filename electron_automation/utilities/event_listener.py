from selenium.webdriver.support.events import AbstractEventListener

class EventListener(AbstractEventListener):
    button_text = None

    def before_navigate_to(self, url, driver):
        print("before navigate to:", url)

    def after_navigate_to(self, url, driver):
        print("after navigate to:", url)

    def before_navigate_back(self, driver):
        print("before navigate back:", driver.current_url)

    def after_navigate_back(self, driver):
        print("after navigate back:", driver.current_url)

    def before_navigate_forward(self, driver):
        print("before navigate forward:", driver.current_url)

    def after_navigate_forward(self, driver):
        print("after navigate forward:", driver.current_url)

    def before_find(self, by, value, driver):
        print("before find element:", value)

    def after_find(self, by, value, driver):
        print("after find element:", value)

    def before_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print("before change value:", element.get_attribute("value"))
        else:
            print("before change value:", element.text)

    def after_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print("after change value:", element.get_attribute("value"))
        else:
            print("after change value:", element.text)

    def before_click(self, element, driver):
        EventListener.button_text = element.get_attribute("value")
        if element.tag_name == "input":
            print("before click:", EventListener.button_text)
        else:
            print("before click:", EventListener.button_text)

    def after_click(self, element, driver):
        print("after click:", EventListener.button_text)

    def before_execute_script(self, script, driver):
        print("before execute script:", script)

    def after_execute_script(self, script, driver):
        print("after execute script:", script)

    def before_close(self, driver):
        print("before closing tab")

    def after_close(self, driver):
        print("after closing tab")

    def before_quit(self, driver):
        print("before quit")

    def after_quit(self, driver):
        print("after quit")

    def on_exception(self, exception, driver):
        print("On exception: "+str(exception) )














