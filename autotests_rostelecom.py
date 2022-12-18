import pytest

from pages.auth_page import AuthPage
from pages.registration_page import RegPage


# Регистрация пользователя с пустым полем "Имя" № 1
def test_registration_page_with_empty_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Иванов")
    reg_page.email_or_mobile_phone_field.send_keys("psiholog@sibmail.com")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty123")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Регистрация пользователя с значением в поле "Имя"< 2 символов № 2
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('-')
    reg_page.last_name_field.send_keys("Иванов")
    reg_page.email_or_mobile_phone_field.send_keys("psiholog@sibmail.com")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty123")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Регестрация пользователя с значением в поле "Фамилия" >30 символов № 3
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("йцуфывячссиититьпроапрукенкенукеукецукуйцуйцуйцу")
    reg_page.email_or_mobile_phone_field.send_keys("psiholog@sibmail.com")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty123")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Регистрация пользователя с уже зарегистрированным номером № 4
def test_registration_of_an_already_registered_user(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иванов")
    reg_page.email_or_mobile_phone_field.send_keys("+79138152175")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty123")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible


# Проверка кнопки - закрытия всплывающего окна оповещения ('x') № 5
@pytest.mark.xfail(reason="Должна быть кнопка 'х'")
def test_notification_form(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иванов")
    reg_page.email_or_mobile_phone_field.send_keys("+79138152175")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty123")
    reg_page.continue_button.click()
    assert reg_page.login_button.get_text() == 'Войти'
    assert reg_page.recover_password_button.get_text() == 'Восстановить пароль'
    assert reg_page.close_button.get_text() == 'x'

# Корректное отображение cтраницы авторизации № 6
def test_start_page_is_correct(web_browser):
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert phone_tab_class == "rt-tab rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.auth_title.get_text() == "Авторизация"
    assert page.logo_lk.get_text() == "Личный кабинет"


# Проверка элементов в правом и левом блоках страницы № 7
@pytest.mark.xfail(reason="Расположение элементов на странице не соответсвует требованиям ТЗ")
def test_location_of_page_blocks(web_browser):
    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=1)
    assert page.lk_form.find(timeout=1)


# Проверка названия таб выбора "Номер" № 8
@pytest.mark.xfail(reason="Таб выбора 'Номер' не соответсвует ожидаемым требованиям ТЗ")
def test_phone_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"


# Корректное название кнопки "Продолжить" в форме "Регестрация" № 9
@pytest.mark.xfail(reason="Кнопка должна именоваться 'Продолжить'")
def test_registration_page_and_continue_button(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.name_field_text.get_text() == "Имя"
    assert reg_page.last_name_field_text.get_text() == "Фамилия"
    assert reg_page.region_field_text.get_text() == "Регион"
    assert reg_page.email_or_mobile_phone_field_text.get_text() == "E-mail или мобильный телефон"
    assert reg_page.password_field_text.get_text() == "Пароль"
    assert reg_page.password_confirmation_field_text.get_text() == "Подтверждение пароля"
    assert reg_page.continue_button.get_text() == "Продолжить"



# Некорректный пароль при регестрации пользователя (< 8 символов) № 10
def test_incorrect_password_during_registration(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иванов")
    reg_page.email_or_mobile_phone_field.send_keys("psiholog@sibmail.com")
    reg_page.password_field.send_keys("qwe123")
    reg_page.password_confirmation_field.send_keys("qwe123")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"


# Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль"
# выделяется оранжевым № 11
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79138152175')
    page.password.send_keys("1515")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')


# Спец символы в поле "Фамилия" № 12
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys(";%:;!!@")
    reg_page.email_or_mobile_phone_field.send_keys("psiholog@sibmail.com")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty123")
    reg_page.continue_button.click()
    assert reg_page.message_must_be_filled_in_cyrillic.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Поля ввода "Пароль" и "Подтверждение пароля" в форме "Регистрация" не совпадают № 13
def test_password_and_password_confirmation_do_not_match(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иванов")
    reg_page.email_or_mobile_phone_field.send_keys("psiholog@sibmail.com")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty321")
    reg_page.continue_button.click()
    assert reg_page.message_passwords_dont_match.get_text() == "Пароли не совпадают"


# Не корректный email в поле ввода "Email или мобильный телефон" № 14
def test_invalid_email_or_mobile_phone(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Иван")
    reg_page.last_name_field.send_keys("Иванов")
    reg_page.email_or_mobile_phone_field.send_keys("psiholog")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty123")
    reg_page.continue_button.click()
    assert reg_page.message_enter_the_phone_in_the_format.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или" \
                                                                        " +375XXXXXXXXX, или email в формате example@email.ru"

# Тестирование аутентификации зарегестрированного пользователя № 15
def test_authorisation_valid(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79138152175')
    page.password.send_keys("Qwerty123")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()
