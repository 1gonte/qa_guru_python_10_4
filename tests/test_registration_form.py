from selene import browser, be, have


def test_fill_registration_form():

    # 1. open form
    browser.open('https://demoqa.com/automation-practice-form')

    # 2. find and type in field First Name
    browser.element('#firstname').should(be.blank).type('Georgii')

    # 3. find and type in field Last Name
    browser.element('#lastname').should(be.blank).type('Sergeev')

    # 4. find and type in field Email
    browser.element('#userEmail').should(be.blank).type('example@gmail.com')

    # 5. find and toggle check-box Gender
    browser.element('#gender-radio-1').click()

    # 6. find and type in field Mobile
    browser.element('#userNumber').should(be.blank).type('0123456789')

    # 7. find and fill field Date of Birth
    browser.element('#dateOfBirthInput').click().\
        element('.react-datepicker__month-select').click().\
        element('.react-datepicker__month-select>[value="1"]').click()

    browser.element('.react-datepicker__year-select').click().type('2001').press_enter()

    browser.element('.react-datepicker__day--016').click()

    # 8. find and type in field Subjects
    browser.element('#subjectsContainer').should(be.blank).type('Computer Science').press_enter()

    # 9. find and toggle check-box Hobbies
    browser.element('#hobbies-checkbox-1').click()
    browser.element('#hobbies-checkbox-2').click()
    browser.element('#hobbies-checkbox-3').click()

    # 10. find and fill the Picture field

    # 11. find and fill Current Address
    browser.element('#currentAddress').should(be.blank).type('some random address')

    # 12. find and choose State and City
    browser.element('#state').type('NCR').press_enter()
    browser.element('#city').type('Delhi').press_enter()

    # 13. zoom out the page so the 'submit' btn is visible
    browser.execute_script("document.body.style.zoom='65%'")

    # 14. press Submit
    browser.element('#submit').click()
