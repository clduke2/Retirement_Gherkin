Feature: Retirement Age Calculator
  As a United States citizen,
  I want to calculate when I am eligible for retirement benefits
  So that I may receive them as soon as I can.


  Scenario Outline: Calculate the age I retire
    Given I run the program
    When I enter my birth year
    Then using the "<year>" given, the program calculates how old I am in "<years>" and "<months>" when I can retire.