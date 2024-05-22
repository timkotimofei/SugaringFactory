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
    Then Type random "first_name" to "//input[@name='firstname']"
    Then Type random "last_name" to "//input[@name='lastname']"
    Then Type random "company" to "//input[@name='company']"
    Then Type random "address_1" to "//input[@name='address_1']"
    Then Type random "address_2" to "//input[@name='address_2']"
    Then Type random "city" to "//input[@name='city']"
    Then Type random "postcode" to "//input[@name='postcode']"
    Then Click on element "//select[@name='zone_id']"
    Then Click on element "//option[contains(text(), 'Illinois')]"
    And Scroll to element "//a[contains(text(), 'Continue')]"
    Then Click on element "//a[contains(text(), 'Continue')]"
    Then Click on element "//a[contains(text(), 'Logout')]"
    Then Click on element "//span[contains(text(), 'Continue')]"
    Then Wait for "5" seconds