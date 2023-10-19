Feature: Test the functionality of the Login Page

  Scenario: Check that "No customer account found" is displayed when the user tries to login with an unregistred email(fara param)
    Given I am on the Login Page
    When I insert an unregistred email in the mail input
    When I insert a passowrd in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error message contains "No customer account found" mesagge

  Scenario: Check that "Please enter your email" message is displayed when the user enters empty email address
    Given I am on the Login Page
    When I insert " " in the mail input
    When I click on the login button
    Then Email error message is displayed
    Then Email error text contains "Please enter your email"