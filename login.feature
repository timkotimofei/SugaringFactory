# Created by timofeitimko at 5/16/24
Feature: Login page tests
  # Enter feature description here

  Scenario: Login
    Given Open "staging" environment
    Then Verify "login" page is exists
    Then Login as "tester"
    Then Wait for "2" seconds
