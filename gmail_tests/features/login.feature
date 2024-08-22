Feature: Gmail Login

  Background:
    Given the Gmail app is launched
    When a new email address is entered
    And the correct password is provided

  Scenario: Add an account
    Then the account should be displayed in the addresses list
    When delete account

  Scenario: Log in for the first time
   And navigating to the inbox
   And permission is 'denied'
   And the pop-up news window is closed
   Then the inbox should be displayed


