# Created by vadimzemlyanoy at 4/21/24
Feature: Target.com cart feature


  Scenario: User able to add product into the cart
    Given Open Target main page
    When Search for lamp
    Then Search results for lamp are shown
    When Click at Add to cart button under the image of product
    When Click at Add to cart button from right side navigation menu
    And Click at Decline coverage button
    When Click on the Cart icon
    Then Verify total price is shown