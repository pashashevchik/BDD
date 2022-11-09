
Feature: Login to My Store

  Scenario: Authorization with valid data
    Given I visit the login page
    And I press account button
    When I login with valid data
    Then I should be on the main page

