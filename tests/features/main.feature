Feature: Retirement Age Calculator
  As a United States citizen,
  I want to calculate when I am eligible for retirement benefits
  So that I may receive them as soon as I can.


  Scenario Outline: Calculate the age I retire
    Given I run the program
    When I enter my birth year
    Then using the "<year>" given, the program calculates how old I am in "<years>" and "<months>" when I can retire.
    
  # Here was a table in the same format as presented in the online video lecture.
  # My last attempt of the assignment involved trying to use pytest's parametrize instead.
