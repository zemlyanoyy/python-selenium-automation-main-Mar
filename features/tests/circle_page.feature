# Created by vadimzemlyanoy at 4/21/24
Feature: Target Circle page

  Scenario: User able to see 6 benefit boxes
    Given Open Target Circle page
    When Search the benefit boxes
    Then Verify 10 benefit boxes are shown