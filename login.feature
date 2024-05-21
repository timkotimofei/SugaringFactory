# Created by timofeitimko at 5/16/24
Feature: Login page tests
  # Enter feature description here

  Scenario: Login
    Given Open "staging" environment
    Then Verify "login" page is exists
    Then Login as "tester"
    Then Verify "my account" page is exists
    Then Click on element "//a[contains(text(), 'Sugaring Store')]"
    And Scroll to element "//div[contains(text(), 'Soft')]"
    Then Click on element "//div[contains(text(), 'Soft')]"
    Then Click on element "//input[@value='Add to Cart']"
    Then Page contains element "//span[@class='latest-added']"
    Then Click on element "//span[contains(text(), 'Checkout')]"
    And Scroll to element "//a[contains(text(), 'Continue checkout')]"
    Then Click on element "//a[contains(text(), 'Continue checkout')]"
    And Scroll to element "//a[contains(text(), 'Add shipping address')]"
    Then Click on element "//a[contains(text(), 'Add shipping address')]"
    Then Type random name to "//input[@name='firstname']"
    Then Wait for "2" seconds