# Created by vadimzemlyanoy at 4/13/24
Feature: Target.com Sign in page

  Scenario: Logged out user can access Sign in
    Given Open Target main page
    When Click Sign In
    When From right side navigation menu, click Sign in
    Then Verify Sign In form opened

