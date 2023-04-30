from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from time import sleep
from selene import have

class ANSWEAR:
    def __init__(self):
        self.base_url = 'https://answear.ua/'

    def open(self):
        browser.open('https://answear.ua/')
        browser.driver.maximize_window()
        sleep(1)
        return self
    def cookie_accept(self):
        browser.element('[class="btn btn--primary CookiesInfo__cookiesInfoBtnWrapperAccept__nyIJU"').click()
        return self
    def authorize(self):
        s('[class="Header__iconsSvg__AsfGv"]').click()
        s('#_username').set_value('makemef4mous@gmail.com')
        sleep(1)
        s('#_password').set_value('Des19961975')
        sleep(1)
        s('[class="btn xs-12 l-12 btn--primary btn--fluid"]').click()
        sleep(1)
        return self
    def search(self, text: str):
        s('[class="Header__logo__gUHw7"]').click()
        s('[href="/c/vin"]').click()
        s('#productsSearch').type('кеди').press_enter()
        sleep(2)
        s('[class="Modal__close__C40RR"]').click()
        sleep(2)
        return self
    def filters(self):
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[2]/div/i').click()
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[2]/div/div/ul/div[2]/div/div/div/div/label').click()
        s('[class="btn xs-12 m-6 m-offset-3 l-12 l-offset-0 btn--fluid btn--filtersSubmit btn--spaced-bottom"]').click()
        sleep(1)
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[3]/div/i').click()
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[3]/div/div/ul/div[15]/div/div/div/div/label').click()
        s('[class="btn xs-12 m-6 m-offset-3 l-12 l-offset-0 btn--fluid btn--filtersSubmit btn--spaced-bottom"]').click()
        sleep(1)
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[4]/div/i').click()
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[4]/div/div/ul/div[23]/div/div/div/div/label').click()
        s('[class="btn xs-12 m-6 m-offset-3 l-12 l-offset-0 btn--fluid btn--filtersSubmit btn--spaced-bottom"]').click()
        sleep(1)
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[5]/div/i').click()
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[5]/div/div/ul/div[3]/div/div/div/div/label').click()
        s('[class="btn xs-12 m-6 m-offset-3 l-12 l-offset-0 btn--fluid btn--filtersSubmit btn--spaced-bottom"]').click()
        sleep(1)
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[6]/div/i').click()
        s('//*[@id="root"]/main/div/div[2]/div[3]/div/div/div/div/form/div[1]/div[6]/div/div/ul/li/div/div[2]/div[1]/div/div/div/label').click()
        s('[class="btn xs-12 m-6 m-offset-3 l-12 l-offset-0 btn--fluid btn--filtersSubmit btn--spaced-bottom"]').click()
        sleep(1)
        return self
    def add_to_bag(self):
        s('//*[@id="root"]/main/div/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[1]/button').click()
        s('//*[@id="root"]/main/div/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[1]/ul/li[2]/div').click()
        s('[class="btn xs-12  l-12 l-offset-0 btn--fluid btn--filtersSubmit btn--spaced-bottom"]').click()
        sleep(1)
        s('[href="/mii-vybir"]').click()
        sleep(1)
        s('//*[@id="root"]/main/div/div[3]/div/div/section/div[1]/div[2]/div[1]/div/div/div/label').click()
        sleep(1)
        s('//*[@id="root"]/main/div/div[2]/div/div[1]/div/div[2]/button/div').click()
        sleep(1)
        s('[href="/cart"]').click()
        sleep(1)
        s('[class="answear-icon answear-icon-plus QuantitySelectorTemplate__quantityButtonIcon__Gpwiq"]').click()
        sleep(2)
        s('[class="answear-icon answear-icon-minus QuantitySelectorTemplate__quantityButtonIcon__Gpwiq"]').click()
        sleep(2)
        return self

    def delete_from_bag(self):
        s('//*[@id="root"]/main/div/div/div[1]/div[1]/div/div[3]/div/div/div[2]/div[3]/button[1]').click()
        sleep(2)
        return self
    def back_to_start_page(self):
        s('[class="btn btn--default EmptyCart__emptyCartButton__d-FxX"]').click()
        sleep(2)
        return self
    def profile_logout(self):
        s('[class="Header__iconsSvg__AsfGv"]').click()
        s('[class="MyAccount__logout__+gOL6 active"]').click()
        sleep(2)

    def negative_test(self):
        s('#_username').set_value('makemef4mous')
        s('#_password').set_value('Des19961975')
        s('[class="btn xs-12 l-12 btn--primary btn--fluid"]').click()
        error_msg = s('#root > main > div > div > div.l-9.xs-12 > div:nth-child(2) > div.xs-12.l-5.LoginPanelTemplate__mobileContent__sR6AZ.LoginPanelTemplate__activeMobileContent__ZNENx > form > div.dynamicField.DynamicField__dynamicField__J84AZ.undefined > span.fieldError.FieldError__error__ZiVkd')
        assert error_msg.should(have.text('Будь ласка, введіть електронну адресу правильно'))
        sleep(2)
        s('#_username').set_value('makemef4mous@gmail.com')
        s('#_password').set_value('%$&_')
        s('[class="btn xs-12 l-12 btn--primary btn--fluid"]').click()
        error_msg = s('div > ul > li > div > p')
        assert error_msg.should(have.text('Неправильна електронна пошта або пароль'))
        sleep(2)

