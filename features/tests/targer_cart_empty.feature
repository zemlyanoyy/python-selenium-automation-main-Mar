# Created by vadimzemlyanoy at 4/13/24
Feature: Target.com cart feature


  Scenario: User able to see "Your cart is empty"
    Given Open Target main page
    When Click on the Cart icon
    Then Verify "Your cart is empty" message is shown



