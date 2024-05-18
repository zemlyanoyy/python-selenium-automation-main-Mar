
Feature: Target.com search tests

  Scenario: User can search for a product on target
    Given Open Target main page
    When Search for lamp
    Then Search results for lamp are shown

Scenario: User can search for a car on target
    Given Open Target main page
    When Search for car
    Then Search results for car are shown

Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image